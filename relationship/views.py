from flask import Blueprint, abort, session, redirect, url_for

from user.models import User
from relationship.models import Relationship
from user.decorators import login_required

relationship_app = Blueprint('relationship_app', __name__)

@relationship_app.route('/add_friend/<to_username>', methods=('GET', 'POST'))
@login_required
def add_friend(to_username):
    logged_user = User.objects.filter(username=session.get('username')).first()
    to_user = User.objects.filter(username=to_username).first()
    if to_user:
        rel = Relationship.get_relationship(logged_user, to_user)
        to_username = to_user.username
        if rel == "REVERSE_FRIENDS_PENDING":
            # Check if there's a pending invitation to_user -> from_user
            # so then we confirm the friendship
            Relationship(
                from_user=logged_user, 
                to_user=to_user,
                rel_type=Relationship.FRIENDS,
                status=Relationship.APPROVED
                ).save()
            reverse_rel = Relationship.objects.get(
                from_user=to_user,
                to_user=logged_user)
            reverse_rel.status=Relationship.APPROVED
            reverse_rel.save()
        elif rel == None:
            # Otherwise, just do the initial request
            Relationship(
                from_user=logged_user, 
                to_user=to_user, 
                rel_type=Relationship.FRIENDS, 
                status=Relationship.PENDING
                ).save()
        return redirect(url_for('user_app.profile', username=to_username))
    else:
        abort(404)
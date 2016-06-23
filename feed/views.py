from flask import Blueprint, request

from user.decorators import login_required

feed_app = Blueprint('feed_app', __name__)

@feed_app.route('/message/add', methods=('POST'))
@login_required
def add_message():
    ref = request.referrer
    if request.method == 'POST':
        return request.post.get('text')
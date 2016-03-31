from wand.image import Image
import os

# from settings import UPLOADED_IMAGES_DEST, AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_BUCKET
from settings import UPLOADED_IMAGES_DEST
from utilities.common import utc_now_ts as now

def thumbnail_process(file, content_type, content_id, sizes=[("sm", 50), ("lg", 75), ("xlg", 200)]):

    image_id = now()
    original_filename = UPLOADED_IMAGES_DEST + '/' + file
    filename_template = UPLOADED_IMAGES_DEST + '/' + content_type + '/' + content_id + '.%s.%s.png'
    key_template = content_id + '.%s.%s.png'

    # original
    with Image(filename=original_filename) as img:
        crop_center(img)
        img.format = 'png'
        img.save(filename=filename_template % (image_id, 'raw'))

    # sizes
    for (name, size) in sizes:
        with Image(filename=original_filename) as img:
            crop_center(img)
            img.sample(size, size)
            img.format = 'png'
            img.save(filename=filename_template % (image_id, name))

    if AWS_BUCKET:
        k = get_aws_key()
        k.key = content_type + '/' + content_id + '.%s.%s.png' % (image_id, 'raw')
        k.set_contents_from_filename(filename_template % (image_id, 'raw'))
        k.set_acl('public-read')
        os.remove(filename_template % (image_id, 'raw'))

        for (name, size) in sizes:
            k.key = content_type + '/' + content_id + '.%s.%s.png' % (image_id, name)
            k.set_contents_from_filename(filename_template % (image_id, name))
            k.set_acl('public-read')
            os.remove(filename_template % (image_id, name))

    os.remove(original_filename)

    return image_id

def crop_center(image):
    dst_landscape = 1 > image.width / image.height
    wh = image.width if dst_landscape else image.height
    image.crop(
        left=int((image.width - wh) / 2),
        top=int((image.height - wh) / 2),
        width=int(wh),
        height=int(wh)
    )

def get_aws_key():
    from boto.s3.connection import S3Connection
    from boto.s3.key import Key
    conn = S3Connection(AWS_ACCESS_KEY, AWS_SECRET_KEY)
    bucket = conn.get_bucket(AWS_BUCKET)
    return Key(bucket)
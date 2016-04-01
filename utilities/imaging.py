from wand.image import Image
import os
import boto3
from boto3.s3.transfer import S3Transfer

from utilities.common import utc_now_ts as now
from settings import UPLOAD_FOLDER, AWS_BUCKET

def thumbnail_process(file, content_type, content_id, sizes=[("sm", 50), ("lg", 75), ("xlg", 200)]):

    image_id = now()
    filename_template = content_id + '.%s.%s.png'

    # original
    with Image(filename=file) as img:
        crop_center(img)
        img.format = 'png'
        img.save(filename=os.path.join(UPLOAD_FOLDER, content_type, filename_template % (image_id, 'raw')))

    # sizes
    for (name, size) in sizes:
        with Image(filename=file) as img:
            crop_center(img)
            img.sample(size, size)
            img.format = 'png'
            img.save(filename=os.path.join(UPLOAD_FOLDER, content_type, filename_template % (image_id, name)))

    if AWS_BUCKET:
        s3 = boto3.client('s3')
        transfer = S3Transfer(s3)
        transfer.upload_file(
            os.path.join(UPLOAD_FOLDER, content_type, filename_template % (image_id, 'raw')), 
            AWS_BUCKET, 
            os.path.join(content_type, filename_template % (image_id, 'raw')),
            extra_args={'ACL': 'public-read', 'ContentType': 'image/png'}
            )
        os.remove(os.path.join(UPLOAD_FOLDER, content_type, filename_template % (image_id, 'raw')))

        # for (name, size) in sizes:
        #     k.key = content_type + '/' + content_id + '.%s.%s.png' % (image_id, name)
        #     k.set_contents_from_filename(filename_template % (image_id, name))
        #     k.set_acl('public-read')
        #     os.remove(filename_template % (image_id, name))

    os.remove(file)

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

from django.db import models
from django.conf import settings
import os
import time
import PIL
from PIL import Image, ImageOps, ImageFont, ImageDraw


# Create your models here.
class Document(models.Model):
        relative_upload_path = 'documents/%Y/%m/%d'
        docfile = models.ImageField(upload_to=relative_upload_path)
        heading = models.CharField(max_length=256, default='Figure 1 ....')
        footer = models.CharField(max_length=256, default='Source .....')

        def save(self, *args, **kwargs):
            #image_object = Image.open(os.path.join(settings.STATIC_ROOT, 'test0.png'))
            #self.docfile =
            img_path = os.path.join(os.path.dirname(self.docfile.path),
                                    time.strftime(self.relative_upload_path),
                                    os.path.basename(self.docfile.path))

            super(Document, self).save(*args, **kwargs)
            img = process_image(Image.open(self.docfile), self.heading, self.footer)
            img.save(img_path)
            #img_ext = os.path.splitext(self.docfile.path)[1]
            #if img_ext not in PIL.Image.EXTENSION:
            #    PIL.Image.init()
            #img_format = PIL.Image.EXTENSION[img_ext]
            #with tempfile.SpooledTemporaryFile() as tmp_img_file:
            #    img.save(tmp_img_file, img_format)
            #    self.save(self.docfile.path, File(tmp_img_file))

            #self.save(*args, **kwargs)
            #response = HttpResponse(content_type="image/jpeg")
            #img.save(response, "JPEG")
            #return response
            #return render(request, 'index.html')


def process_image(img, heading, footer, frame_size=20, iborder_size=2, oborder_size=4, heading_font_size=11, footer_font_size=8, max_width=1000.0, max_height=600.0):
    """ Processes an image, adding borders, frame, heading, footer and resizing"""
    # Resize image if needed
    ideal_size = right_size(*img.size)
    if ideal_size != img.size:
        img = img.resize(ideal_size, PIL.Image.ANTIALIAS)

    heading_font = ImageFont.truetype(os.path.join(settings.STATIC_ROOT, 'fonts/Roboto-Regular.ttf'), heading_font_size)
    footer_font = ImageFont.truetype(os.path.join(settings.STATIC_ROOT, 'fonts/Roboto-Regular.ttf'), footer_font_size)
    img = ImageOps.expand(img, border=iborder_size, fill='black')
    img = ImageOps.expand(img, border=frame_size, fill='white')
    img = ImageOps.expand(img, border=oborder_size, fill='black')

    heading_width, heading_height = heading_font.getsize(heading)
    footer_width, footer_height = footer_font.getsize(footer)
    heading_position = (img.size[0] / 2 - heading_width / 2, (frame_size - heading_height) / 2 + oborder_size)
    footer_position = (oborder_size + frame_size, img.size[1] - (oborder_size + (frame_size - ((frame_size - footer_height) / 2))))
    img_draw = ImageDraw.Draw(img)
    img_draw.text(heading_position, heading, (0, 0, 0), font=heading_font)
    img_draw.text(footer_position, footer, (0, 0, 0), font=footer_font)
    return img


def right_size(width, height, max_width=1000.0, max_height=600.0):
    """
    Figures out the width and height of a photo given the max width/height so
    that dimentions are preserved.
    """
    new_width = float(width)
    new_height = float(height)
    if width > max_width:
        new_height = (max_width / width) * new_height
        new_width = max_width
    if new_height > max_height:
        new_width = (max_height / height) * new_width
        new_height = max_height
    return (int(new_width), int(new_height))

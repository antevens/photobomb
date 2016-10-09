from django.conf import settings
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from photobomb.imagine.models import Document
from photobomb.imagine.forms import DocumentForm

import os
import PIL
from PIL import Image, ImageOps, ImageFont, ImageDraw


# Create your views here.

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )

def index(request):
    #return HttpResponse('Hello from Python!')
    image_object = Image.open(os.path.join(settings.STATIC_ROOT, 'test0.png'))
    img = process_image(image_object, 'Figure 1 ....', 'Source .....')
    response = HttpResponse(content_type="image/jpeg")
    img.save(response, "JPEG")
    return response
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

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .form import BaraForm
from .models import Bara
from barcode.writer import ImageWriter
import barcode
from PIL import Image, ImageDraw, ImageFont


# Create your views here.
def start(request):

    if request.method == 'POST':
        form = BaraForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            ba = Bara(
                bara=form.cleaned_data['bara'],
                name=form.cleaned_data['name'],
                art=form.cleaned_data['art']
            )
            ba.save()
            bar(ba.bara, ba.name, ba.art)
            return HttpResponseRedirect('/done')
    else:
        form = BaraForm()
    return render(request, 'gen_bara/start.html', context={'form': form})


def done(request):
    return render(request, 'gen_bara/done.html')


def bar(code, name, art):
    ean = barcode.get_barcode_class('ean13')
    ean2 = ean(code, writer=ImageWriter())
    ean2.save('Штрих-код_00')

    img = Image.new('RGB', (1370, 708), 'white')
    img.save('test1.jpg')

    im1 = Image.open('test1.jpg')
    im2 = Image.open('Штрих-код_00.png')

    im2 = im2.resize(size=(1200, 400))
    im1.paste(im2, (60, 15))
    im1.save('fon_pillow_paste.jpg', quality=190)

    im1.close()
    im2.close()

    img = Image.open('fon_pillow_paste.jpg')
    font = ImageFont.truetype("arial.ttf", size=72)
    idraw = ImageDraw.Draw(img)
    idraw.text((300, 420), 'Бирюлина А.С.', 'black', font=font)
    idraw.text((300, 500), name, 'black', font=font)
    idraw.text((300, 580), ('Арткул: ' + art), 'black', font=font)
    img.save('gen_bara/static/gen_bara/001.jpg')


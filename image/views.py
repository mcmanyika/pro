from django.shortcuts import render

from image.models import Flower

def index(request):

	flowers = Flower.objects.all()

	return render(request, 'image/img.html', {'flowers': flowers })
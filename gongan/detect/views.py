from django.shortcuts import render
from django.http import HttpResponse
from django import forms

class ImgForm(forms.Form):
	Img = forms.ImageField()

def index(request):
	return render(request, 'home.html')

def nothing_to_show(request):
	return render(request, 'no.html')

def detect_bang(request):
	if request.method == 'POST':
		UpLoadImg = ImgForm(request.POST, request.FILES)
		if UpLoadImg.is_valid():
			img = ImgForm(request.FILES['Img'].read())
			return HttpResponse("成功!")
		else:
			UpLoadImg = ImgForm()
			return render(request, 'DetectBang_wrong.html', {'form': UpLoadImg})
	else:
		UpLoadImg = ImgForm()
	
	return render(request, 'DetectBang.html', {'form': UpLoadImg})
	
# Create your views here.

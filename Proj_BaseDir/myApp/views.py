from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def HelloApp(request):
    return HttpResponse(
        "<head><title>Web App</title></head>"
        "<br><br>"
        "<div><center><h2>Hello Django World!!</h2></center></div>"
        "<hr style='width:50%; text-align:center; margin: center;'>"
        "<p><center><h3>My First Django Web App.</h3></center></p>"
        )

def show(request):
	return render(request,'index.html')

def address(request):
	return render(request,'contact.html')

from django.shortcuts import render
from Dari_Mooch_Products.models import Products
from Dari_Mooch_Carousels.models import Carousels
from Dari_Mooch_Central_Images.models import Central_Images
from Contact_Us.models import Contact_Us





def homePage(request):
    Products_Data = Products.objects.all()
    Carousels_Data = Carousels.objects.all()
    Central_Images_Data =  Central_Images.objects.all()
    Data= {
        "products": Products_Data,
        "carousels":Carousels_Data,
        'Central_images':Central_Images_Data
    }
    return render(request, 'index.html', Data)



def aboutPage(request):
    return render(request, 'about.html')

def loginPage(request):
    return render(request, 'login.html')



def contactPage(request):

    Firstname = request.GET.get('firstname')
    Lastname = request.GET.get('lastname')
    Email = request.GET.get('email')
    Phone = request.GET.get('phone')
    Message = request.GET.get('message')
    contact = Contact_Us(firstname=Firstname, lastname=Lastname, email=Email, phone=Phone, message=Message)
    contact.save()
    return render(request, 'contact.html')

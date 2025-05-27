from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse


def django_mail(request):
    send_mail(
        subject='Hii How are you ',
        message='Can we go out tommorow',
        from_email='velpulabhanuprasad@gmail.com',
        recipient_list=['vikasjadhav9505@gmail.com', 'bhanubanu2101@gmail.com', 'pathanmouserkhan786@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse("Email sent successfully")

 

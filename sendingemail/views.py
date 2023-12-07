from django.http import HttpResponse
from django.core.mail import send_mail, get_connection, EmailMessage
from django.conf import settings

def sendmail(request):
    send_mail(
        subject='Men test qilmoqchi edim😁😁😁😁...', 
        message='Amir Temur Tomonidan yozildi spam bolsa uzur😝😝😝😝😝...', 
        from_email='bahtiyormurotaliyev552@gmail.com',
        recipient_list=['abdulahatrixsibo@gmail.com'],
        fail_silently=False)
    return HttpResponse('Email has been sent!!...')
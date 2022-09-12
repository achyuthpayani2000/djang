from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from product.forms import emailsendform


def sendEmail(request):
    if(request.method=='POST'):
        email_id = 'achyuthpayani@gmail.com'
        email_subject = request.POST['subject']
        email_message = request.POST['body']
        res = send_mail(email_subject, email_message, '1ms17ee038@gmail.com', [email_id], fail_silently=False)
        return redirect('/', permanent=True)
    fo = emailsendform()
    return render(request,'mail/sendmail.html',{'form':fo})
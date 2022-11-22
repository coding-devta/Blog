from django.utils.text import slugify
import string
import random

def random_string_generator(N):
   
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))

    return res
  

def slug_generator(text):
    
    new_slug = slugify(text)
    from home.models import blogmodel 
    if blogmodel.objects.filter(slug=new_slug).first():
        return slug_generator(text + random_string_generator(5))
    return new_slug

from django.conf import settings
from django.core.mail import send_mail

def  send_mail_to_user(token , email):
    subject = f'your accounts need to be verified'
    message = f'hi paste the link to verify account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list =[email]
    send_mail(subject, message, email_from, recipient_list)
    return True
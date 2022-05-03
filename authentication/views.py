from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.hashers import make_password

#html email required stuff
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import os
from django.conf import settings
import base64
import hashlib 
import hmac 
import math 
import time
import qrcode
import string
import random


# Create your views here.
def randomstring(length):
    secret_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))
    return secret_key

@login_required(login_url="/login")
def update_profile(request):
    return HttpResponse('login hogya')

def two_step(request, token):
    try:
        user = Users.objects.get(login_token=token)
    except:
        messages.error(request, "Invalid URL! Please try again")
        return redirect('/login')

    if request.user.is_authenticated:
        return redirect("/update_profile")

    if request.method=="POST":
        code = request.POST.getlist("digit")
        code_string = ''.join([str(digit) for digit in code])

        t = math.floor(time.time() // 30)
        key = bytes(str(user.secret_code), 'utf-8')
        hmac_object = hmac.new(key, t.to_bytes(length=8, byteorder="big"), hashlib.sha1)
        hmac_sha1 = hmac_object.hexdigest()
        offset = int(hmac_sha1[-1], 16)
        binary = int(hmac_sha1[(offset * 2):((offset * 2) + 8)], 16) & 0x7fffffff
        totp = str(binary)[-6:]

        if code_string == totp:
            login(request, user)
            return redirect('/update_profile')
       
    params = {'token':token}
    return render(request, "authentication/two_step.html", params)

def handlelogin(request):
    if request.method=="POST":
        # Get the post parameters
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(email= email, password= password)
        if user:
            login_token = randomstring(30)
            user.login_token = login_token
            user.save()
            return redirect('/two_step/'+login_token)
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/login")
    elif request.user.is_authenticated:
        return redirect("activity_list")
    else:
        #params = {'redirect_page': request.GET.get("next", "off")}
        return render(request, "authentication/login.html")

def send_email(mydata, page, subject):
    #mail_setting = Mail_settings.objects.get(priority=2)
    html_content = render_to_string("email_templates/"+page, mydata)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        # subject
        subject,
        # msg
        text_content,
        # from email
        'mayank.kumar@integertel.com',
        # recipient list
        [mydata['email']]
    )
    email.attach_alternative(html_content,"text/html")
    email.send()



def signup(request):
    last = request.META.get("HTTP_REFERER")
    #form = RegisterForm()
    if request.method == 'POST':

        #form = RegisterForm(request.POST)

        password=request.POST['password']
        #print(request.POST)
        confirm_password=request.POST['confirm_password']
        cell_number=request.POST['mobile']
        user_name=request.POST['email']
        email_domain=request.POST['email_domain']
        if '@' not in user_name:
            user_name=user_name
        else:
            user_name = user_name.replace('@', '')
        user_name = user_name.lower()
        user_name = user_name.replace(' ', '')
        email_id = user_name+'@'+email_domain
        email_exists = Users.objects.filter(email=email_id).exists()
        if email_exists:
            messages.error(request, "Email "+email_id+" is already saved in our records.")
            return redirect("signup")
        elif password!=confirm_password:
            messages.error(request, "Password and Confirm Password is not same.")
            return redirect("sign_up")
        
        
        
        password   = make_password(password)
        key_length = 20
        #secret_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
        secret_code = randomstring(key_length)
        
        # print result
        #print("The generated random string : " + str(secret_code))
        secret_code = str(secret_code)

        key = bytes(secret_code, 'utf-8')
        token = base64.b32encode(key)
        print(token.decode("utf-8"))

        image_path = os.path.join(settings.MEDIA_ROOT,"user_qr",user_name+".png")
        qr_string = "otpauth://totp/"+email_id+"?secret=" + token.decode("utf-8") +"&algorithm=SHA1&digits=6&period=30"
        print(qr_string)
        img = qrcode.make(qr_string)
        img.save(image_path)

        mydata = {'email':email_id, 'secret_key':secret_code, 'qr_code':user_name+'.png'}
        #send_email(mydata, 'signup.html', 'Your account has been created successfully')

        user_data = Users(email=email_id,password=password, cell_number=cell_number, secret_code=secret_code)
        user_data.save()
        messages.success(request, "Account created successfully.")
        return redirect('/login')
        '''else:
            return redirect(last)'''

    
    return render(request, 'authentication/sign_up.html')

@login_required(login_url="/login")
def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login')
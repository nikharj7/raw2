from django.shortcuts import render, redirect, HttpResponse
import razorpay
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Add_College_and_University, member
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from Student.models import *
from Member_Wait_List.models import *
from Notification.models import *
from Email.models import *
import requests
import json
import urllib.request 
from Home.models import *
from urllib.parse import urlencode
import http.client as ht
from django.template.loader import render_to_string
from django.http import JsonResponse
from csv import reader
import csv, io
from django.contrib.auth import get_user_model
import random, math
import string


def Member(request):
    
    return render(request, 'member_theme/login2.html')

def handleLogin(request):
    if request.method == 'POST':
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        if student.objects.filter(user=loginusername).exists():
            messages.warning(request, 'You are not authenticate to access this page !!!') 
        else:
            user1 = authenticate(username=loginusername, password=loginpassword)

            if user1 is not None:
                login(request, user1)
                
                return redirect('Member_Dashboard')

            else:
                
                return redirect('Member')
    return HttpResponse('404 - Not Found')

def Member_login(request):
    if request.method == "POST":
        first_name = request.POST['First_Name']
        last_name = request.POST['Last_Name']
       
        username = request.POST['priph']
        primary_phone = request.POST['priph']
        pwd = request.POST['DOB']
        email = request.POST['Email']
        Birth_Date = request.POST['DOB']
        Gender = request.POST['Gender']
        Address = request.POST['Address']
        Pin_Code = request.POST['Pin_Code']
        newjjj = request.FILES['docs']
        pack = request.POST['mampack']
        amount = int(request.POST.get('amount'))*100
        country = request.POST['country']
        city = request.POST['City']
        state = request.POST['state']
        client = razorpay.Client(auth=("rzp_test_5snNkaBKoKrJ9w", "UnuX5rqIO6LYe8vjptNidex3"))
        payment = client.order.create({ 'amount':amount, 'currency':'INR', 'payment_capture':'1'} )
        print(payment)
        if member.objects.filter(pin_code=Pin_Code).exists():
            messages.warning(request, 'This Pin Code is already assign to a member you are in our wait list')
            wait = Member_Wait_list(first_name=first_name, last_name=last_name, primary_phone=primary_phone, pin_code=Pin_Code)
            wait.save()
            return render( request,'member_theme/member_signup.html')
        if member.objects.filter(email=email).exists():
            messages.warning(request, 'This Email address is already exist please enter another one !!!')
        
        else:
            usr = User.objects.create_user(username, email, pwd)
            usr.first_name = first_name
            usr.last_name = last_name
            usr.save()
          
            abc = member(Country=country, city=city, state=state, user=usr, payment_id = payment['id'], first_name=first_name, document=newjjj, last_name=last_name, primary_phone=primary_phone, email=email, birth_date=Birth_Date, gender=Gender, address_1=Address, pin_code=Pin_Code, amount=amount, package=pack)
            abc.save()

            return render(request, 'member_theme/member_signup.html', {'payment':payment})
    return render(request, 'member_theme/member_signup.html')

def Member_signup(request):
    st = State.objects.all()
    context = {'st':st}
    return render(request, 'member_theme/member_signup.html', context)

@csrf_exempt
def Success(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
        user2 = member.objects.filter(payment_id=order_id).first()
        user2.Paid = True
        user2.save()
            
        abc = user2.primary_phone
        bcd = user2.primary_phone
        deg = str(user2.birth_date)
                
        api_url = requests.get("http://msg.pwasms.com/app/smsapi/index.php?key=460FE96D69C13A&campaign=0&routeid=69&type=text&contacts="+abc+"&senderid=SJSMTH&msg=Thank+you+for+Registration+with+us.+Your+username+is: "+bcd+" and+password+is: "+deg)
        return render(request, 'member_theme/success.html')
    return render(request, 'member_theme/success.html')


def Member_Dashboard(request):
    if request.user.is_authenticated:
        if student.objects.filter(user=request.user).exists():
                messages.warning(request, 'You are not authenticate to access this page !!!') 
                return redirect('Member_logout')
        else:
            if request.user.is_authenticated:

                if request.method == "POST":

                    obj = member.objects.filter(Terms_and_Conditions=False).first()
                    checking = request.POST['tcc']
                    print(checking)
                    for a in checking:
                        
                        obj.Terms_and_Conditions = True
                        obj.save()
                        return redirect('Member_Profile')
                    


               
                aaa = Member_Notification.objects.all().order_by("-id")[0:5]
                bbb = Member_Email.objects.all().order_by("-id")[0:5]
                n = Notification.objects.filter(user=request.user, viewd=False)
                context = {'aaa':aaa, 'bbb':bbb, 'notifications':n}
                return render(request, 'member_theme/dashboard.html', context)
            else:
                return redirect('home')
    else:
        return redirect('Member')
    return redirect('Member')


def Member_Profile(request):
    if request.user.is_authenticated:
        
        aaa = Member_Notification.objects.all().order_by("-id")[0:5]
        bbb = Member_Email.objects.all().order_by("-id")[0:5]
        data = member.objects.get(user__id=request.user.id)
        context = {'aaa':aaa, 'bbb':bbb, 'data':data}
        
        result_str = ''.join((random.choice(string.digits) for i in range(6)))
        # api_url = requests.get("http://msg.pwasms.com/app/smsapi/index.php?key=260BDF3842037F&campaign=0&routeid=51&type=text&contacts="+priph+"&senderid=SJSMTH&msg=Your+Otp+is"+OTP)
        print(result_str)
        if request.method == "POST":
            profile = request.FILES['pro']
            first_name = request.POST['fn']
            middle_name = request.POST['mn']
            last_name = request.POST['ln']
            priph = request.POST['priph']
            secph = request.POST['secph']
            email = request.POST['email']
            address1 = request.POST['address1']
            address2 = request.POST['address2']
            gender = request.POST['gender']
            dob = request.POST['dob']
            Usr = User.objects.get(id=request.user.id)
            Usr.first_name = first_name
            Usr.last_name = last_name
            Usr.email = email
            Usr.save()

            data.profile = profile
            data.first_name = first_name
            data.middle_name = middle_name
            data.last_name = last_name
            data.primary_phone = priph
            data.secondry_phone = secph
            data.email = email
            data.dob = dob
            data.gender = gender
            data.address_1 = address1
            data.address_2 = address2
            data.save()
        else:
            messages.warning(request, "Please enter a valid OTP !!!")
        return render(request, 'member_theme/Profile.html', context)
    else:
        return redirect('home')

def Add_College_or_University(request):
    if request.user.is_authenticated:
        aaa = Member_Notification.objects.all().order_by("-id")[0:5]
        bbb = Member_Email.objects.all().order_by("-id")[0:5]
        
        cor = Courses.objects.all()
        strm = Streams.objects.all()
        
        context = {'cor':cor, 'strm':strm, 'aaa':aaa, 'bbb':bbb}

        if request.method == "POST":
            user222 = request.user
            user = user222
            abcd = request.FILES['abcd']
            col = request.POST['col']
            Course = request.POST.getlist('Course')
            Stream = str(request.POST.getlist('Stream'))
            City = request.POST['City']
            Pin_Code = request.POST['pin']
            slug = request.POST['City']
            Stream_list = []
            print(Stream_list)
            for streams in Stream:
                Stream_list.append(streams)

            Course_list = []
            print(Course_list)
            for course in Course:
                Course_list.append(course)

            
            kuch = Add_College_and_University(user=user, slug=slug, Profile_Picture=abcd,  College_or_University_Name=col, Course=Course, Stream=Stream, City=City, Pin_Code=Pin_Code)
            kuch.save()
            
        return render(request, 'member_theme/Add_col_uni.html', context)
    else:
        return redirect('home')
    
    

def College_University_List(request):
    if request.user.is_authenticated:
        Clist = Add_College_and_University.objects.all()
        cor = Courses.objects.all()
        strm = Streams.objects.all()
        aaa = Member_Notification.objects.all().order_by("-id")[0:5]
        bbb = Member_Email.objects.all().order_by("-id")[0:5]
        lists = Add_College_and_University.objects.filter(user=request.user)
        context = {'Clist':Clist, 'lists':lists, 'cor':cor, 'strm':strm, 'aaa':aaa, 'bbb':bbb}
        return render(request, 'member_theme/col_uni_list.html', context)
    else:
        return redirect('home')

def Student_Enroll(request):
    if request.user.is_authenticated:
        aaa = Member_Notification.objects.all().order_by("-id")[0:5]
        bbb = Member_Email.objects.all().order_by("-id")[0:5]
        context = {'aaa':aaa, 'bbb':bbb}
        if request.method == "POST":
            std = request.FILES['std']
            mmmm = request.POST['from']
            user333 = request.user
            user = user333
            new = New_Student( File=std, name=mmmm, user=user)
            new.save()

        if request.method == "POST":
           obj = New_Student.objects.get(activated=False)
           with open(obj.File.path, 'r') as f:
            reader = csv.reader(f, delimiter=',', quotechar='|')

            for row in reader:
                hello = row
                result_str = ''.join((random.choice(string.ascii_letters + string.digits) for i in range(8)))
                



   
        
                newst = User.objects.create_user(
                    username = row[3],
                    email = row[0],
                    password = result_str,
                    first_name = row[1],
                    last_name = row[2],
                )
                msg_std = student.objects.create(
                    user = newst,
                    First_Name = row[1],
                    Last_Name = row[2],
                    Email = row[0],
                    Course = row[4],
                    Mobile = row[3],
                    University_Name = row[5]
                )
                pawe = result_str
                msg_passo = newst.username
                msg_mob = msg_std.Mobile
                
            
                msg_url = requests.get("http://msg.pwasms.com/app/smsapi/index.php?key=460FE96D69C13A&campaign=0&routeid=69&type=text&contacts="+msg_mob+"&senderid=SJSMTH&msg=Thank+you+for+Registration+with+us.+Your+username+is: "+msg_passo+" and+password+is: "+pawe)

                
            obj.activated = True
            obj.save()
            context = {'hello':hello}

        return render(request, 'member_theme/Student_Enroll.html', context)
    else:
        return redirect('home')


def Member_Notifications(request):
    if request.user.is_authenticated:
        aaa = Member_Notification.objects.all().order_by("-id")[0:5]
        bbb = Member_Email.objects.all().order_by("-id")[0:5]
        context = {'aaa':aaa, 'bbb':bbb}
        return render(request, 'member_theme/notifications.html', context)
    else:
        return redirect('home')

def Member_Inbox(request):
    if request.user.is_authenticated:
        aaa = Member_Notification.objects.all().order_by("-id")[0:5]
        bbb = Member_Email.objects.all().order_by("-id")[0:5]
        context = {'aaa':aaa, 'bbb':bbb}
        return render(request, 'member_theme/inbox.html', context)
    else:
        return redirect('home')

def Member_Account_Settings(request):
    if request.user.is_authenticated:
        aaa = Member_Notification.objects.all().order_by("-id")[0:5]
        bbb = Member_Email.objects.all().order_by("-id")[0:5]
        context = {'aaa':aaa, 'bbb':bbb}
        return render(request, 'member_theme/account-settings.html', context)
    else:
        return redirect('home')

def handleLogout(request):
    logout(request)
    return redirect('home')


def profile_update(request):
    pass

def student_list(request, id):
    post = Add_College_and_University.objects.filter(id=id)
    
    final = student.objects.all()
    context = {'post':post, 'final':final}


    return render(request, 'member_theme/employee-detail.html', context)
	
def Pin_Code_availiblity(request):
    if request.method == "POST":
        fn = request.POST["fn"]
        ln = request.POST["ln"]
        mobile = request.POST["mobile"]
        pincode = request.POST["pincode"]
        if Pin_Code.objects.filter(Pin_Code=pincode).exists():
            if member.objects.filter(pin_code=pincode).exists():
                messages.warning(request, 'This Pin Code is already assign to a member you are in our wait list')
                wait = Member_Wait_list(first_name=fn, last_name=ln, primary_phone=mobile, pin_code=pincode)
                wait.save()
                return render( request,'member_theme/pincode.html')
            else:
                
                return redirect('Member_signup')
                messages.success(request, "This pincode is available you can continue your signup process")
        else:
            messages.warning(request, "Please enter a valid Pincode !!!")
    return render(request, 'member_theme/pincode.html')

def search(request):
    query = request.GET['query']
    if len(query)>80:
        messages.warning(request, 'No results found!!!! Please refine your Query.')
    else:
        Student_search = Student.objects.filter(First_Name__icontains=query)

    if Student_search.count() == 0:
        messages.warning(request, "No search results. Please refine your query.")
    params = {'Student_search': Student_search, 'query':query}
    return render(request, 'member_theme/search.html', params)

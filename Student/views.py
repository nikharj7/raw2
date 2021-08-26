from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Home.models import *
from Notification.models import *
from Email.models import *
from Company.models import *
from .models import *
from django.core import serializers

# Create your views here.


def Student(request):
	return render(request, 'student/login2.html')

def handleLogout(request):
    logout(request)
    return redirect('home')
    return HttpResponse('handleLogout')

def handleLogin(request):
    if request.method == 'POST':
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        
        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
                
            return redirect('Student_Dashboard')

        else:   
            return redirect('Student')
    return HttpResponse('404 - Not Found')

def Student_Dashboard(request):
    if member.objects.filter(user=request.user).exists():
            messages.warning(request, 'You are not authenticate to access this page !!!') 
            return redirect('handleLogout')
    else:
        if request.user.is_authenticated:

            if request.method == "POST":
               
                data = student.objects.filter(Terms_and_Conditions=False).first()
                checking = request.POST['tcc']
                print(checking)
                for a in checking:
                    data.Terms_and_Conditions = True
                    data.save()
                    return redirect('Student_Profile')
            latest = Internships.objects.all().order_by("-id")[0:5]
            atleast = Jobs.objects.all().order_by("-id")[0:5]
            noti = Student_Notification.objects.all().order_by("-id")[0:5]
            Em = Student_Email.objects.all().order_by("-id")[0:5]
            context = {'noti':noti, 'Em':Em, 'latest':latest, 'atleast':atleast}
            return render(request, 'student/dashboard.html', context)
        else:
            return redirect('home')
    return redirect('Student')

def Student_Profile(request):
    if request.user.is_authenticated:
        AOI = Student_Activity_Email.objects.filter(user=request.user)
        # zhmru = Student_Activity_Email.objects.all()
        noti = Student_Notification.objects.all().order_by("-id")[0:5]
        Em = Student_Email.objects.all().order_by("-id")[0:5]
        data = student.objects.get(user__id=request.user.id)
        context = {'noti':noti, 'Em':Em, 'data':data, 'AOIS':AOI}
        if request.method == "POST":
            profile = request.FILES['picture']
            first_name = request.POST['fn']
            middle_name = request.POST['mn']
            last_name = request.POST['ln']
            phone = request.POST['phone']
            email = request.POST['email']
            dob = request.POST['dob']
            fb = request.POST['fb']
            linkd = request.POST['linkd']
            tweet = request.POST['tweet']
            address1 = request.POST['address1']
            address2 = request.POST['address2']
            city = request.POST['city']
            state = request.POST['state']
            pin = request.POST['pin']
            
            gender = request.POST['gender']
                
                
            Usr = User.objects.get(id=request.user.id)
            Usr.first_name = first_name
            Usr.last_name = last_name
            Usr.email = email
            Usr.save()
             
            data.Profile = profile
            data.First_Name = first_name
            data.Middle_Name = middle_name
            data.Last_Name = last_name
            data.Mobile = phone
            data.Facebook_Profile = fb
            data.Linkedin = linkd
            data.Twitter_Profile = tweet
            data.City = city
            data.State = state
                
            data.Email = email
            data.DOB = dob
            data.Gender = gender
            data.Address_1 = address1
            data.Address_2 = address2
            data.Pin_Code = pin
            data.save()
        return render(request, 'student/Profile.html', context)
    else:
        return redirect('Student')

    return render(request, 'student/Profile.html')

def Academics(request):

    if request.user.is_authenticated:
        noti = Student_Notification.objects.all().order_by("-id")[0:5]
        Em = Student_Email.objects.all().order_by("-id")[0:5]
        cor = Courses.objects.all()
        strm = Streams.objects.all()
        states = State.objects.all()
        data = student.objects.get(user__id=request.user.id)
        context = {'cor':cor, 'strm':strm, 'noti':noti, 'Em':Em, 'states':states, 'data':data}
        if request.method == 'POST':
            ye = request.POST['ye']
            ys = request.POST['ys']
            
            University_address = request.POST['address1']
            University_address2 = request.POST['address2']
            University_City = request.POST['city']
            University_State = request.POST['select']
            University_Pin_Code = request.POST['pin']
            

            data.Year_Start = ys
            data.Year_End = ye
            data.University_address = University_address
            data.University_address2 = University_address2
            data.University_City = University_City
            data.University_State = University_State
            data.University_Pin_Code = University_Pin_Code
            data.save()

        return render(request, 'student/academics.html', context)
    else:
        return redirect('home')

def Area_of_Interest(request):
    if request.user.is_authenticated:
        noti = Student_Notification.objects.all().order_by("-id")[0:5]
        Em = Student_Email.objects.all().order_by("-id")[0:5]
        edu = Education.objects.all()
        sport = Sport.objects.all()
        perform = Performing_Art.objects.all()
        context = {'noti':noti, 'Em':Em, 'edu':edu, 'sport':sport, 'perform':perform}
        json_serializer = serializers.get_serializer("json")()
        sporta = json_serializer.serialize(Sport.objects.all(), ensure_ascii=False)
        performa = json_serializer.serialize(Performing_Art.objects.all(), ensure_ascii=False)
        edua = json_serializer.serialize(Education.objects.all(), ensure_ascii=False)
        if request.method == "POST":
            user111 =  request.user
            user = user111
            education = request.POST['education']
            sporty = request.POST['sporty']
            exlel = request.POST['exlel']
            nmed = request.POST['nmed']
            nms2 = request.POST['nms2']
            certi = request.FILES.get('docs')
            parts = request.POST['parts']
            achiv = request.POST['achiv']
            ssome = Student_Activity_Email(user=user,Education=education, Sports=sporty, Level=exlel, Medal=nmed, Number_of_Medals=nms2, Certificate=certi, Performing_Arts=parts, Performing_Arts_if_any=achiv )
            ssome.save()

        return render(request, 'student/Area_of_intrest.html', context)
	   
    else:
        return redirect('home')

def Notifications(request):
    if request.user.is_authenticated:
        noti = Student_Notification.objects.all().order_by("-id")[0:5]
        Em = Student_Email.objects.all().order_by("-id")[0:5]
        context = {'noti':noti, 'Em':Em}
        return render(request, 'student/notifications.html', context)
	   
    else:
        return redirect('home')

def Inbox(request):
    if request.user.is_authenticated:
        noti = Student_Notification.objects.all().order_by("-id")[0:5]
        Em = Student_Email.objects.all().order_by("-id")[0:5]
        context = {'noti':noti, 'Em':Em}
        return render(request, 'student/inbox.html', context)

    else:
        return redirect('home')

def Account_Settings(request):
    if request.user.is_authenticated:
        noti = Student_Notification.objects.all().order_by("-id")[0:5]
        Em = Student_Email.objects.all().order_by("-id")[0:5]
        context = {'noti':noti, 'Em':Em}
        return render(request, 'student/account-setting.html', context)
    else:
        return redirect('home')


def search(request):
    query = request.GET['query']
    if len(query)>80:
        messages.warning(request, 'No results found!!!! Please refine your Query.')
    else:
        internship_search = Internships.objects.filter(Title__icontains=query)
        job_search = Jobs.objects.filter(Title__icontains=query)


    if Student_search.count() == 0:
        messages.warning(request, "No search results. Please refine your query.")
    params = {'internship_search': internship_search, 'job_search':job_search, 'query':query}
    return render(request, 'student/search.html', params)



 
        
   
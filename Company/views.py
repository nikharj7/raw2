from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from Home.models import *
from Notification.models import *
from Email.models import *
from .models import *
from Student.models import *

# Create your views here.

def Company(request):
    return render(request, 'company_theme/login2.html')

def Company_login(request):
    if request.method == 'POST':
        # Get the post parameters
        comapnyuser = request.POST['comapnyuser']
        companypass = request.POST['companypass']
        user786 = authenticate(request, username=comapnyuser, password=companypass)
        if user786 is not None:
            login(request, user786) 
            print(login) 
            return redirect('Company_Dashboard')

        else:   
            return redirect('Company')
    return HttpResponse('404 - Not Found')

def Company_Dashboard(request):
    if student.objects.filter(user=request.user).exists():
            messages.warning(request, 'You are not authenticate to access this page !!!') 
            return redirect('handleLogout')
    if member.objects.filter(user=request.user).exists():
            messages.warning(request, 'You are not authenticate to access this page !!!') 
            return redirect('handleLogout')
    else:   
        if request.user.is_authenticated:
            if request.method == "POST":
                data = company.objects.filter( Terms_and_Conditions=False).first()
                checking = request.POST['tcc']
                print(checking)
                for a in checking:
                        
                    data.Terms_and_Conditions = True
                    data.save()
                    return redirect('Company_Profile')
            bbb = Company_Email.objects.all().order_by("-id")[0:5]
            aaa = Company_Notification.objects.all().order_by("-id")[0:5]
            context = {'bbb':bbb, 'aaa':aaa}
            return render(request, 'company_theme/dashboard.html', context)
        else:
            return redirect('home')
    return redirect('Company')
    

def Company_Profile(request):
    if request.user.is_authenticated:
        aaa = Company_Notification.objects.all().order_by("-id")[0:5]
        bbb = Company_Email.objects.all().order_by("-id")[0:5]
        state = State.objects.all()
        pin = Pin_Code.objects.all()
        ins = Industry.objects.all()
        orgj = Orgnization.objects.all()
        data = company.objects.get(user__id=request.user.id)
        context = {'state':state, 'pin':pin, 'data':data, 'ins':ins, 'orgj':orgj}
        if request.method == "POST":
            pro = request.FILES['picture']
            cm = request.POST['cm']
            indus = request.POST['indus']
            org = request.POST['org']
            address1 = request.POST['address1']
            address2 = request.POST['address2']
            city = request.POST['city']
            state = request.POST['state']
            pin = request.POST['pin']
            email = request.POST['email']
            mobile = request.POST['mob']
            
            Usr = User.objects.get(id=request.user.id)
            Usr.first_name = cm
            Usr.email = email
            Usr.save()

            data.Profile = pro
            data.email = email
            data.Mobile = mobile
            data.Company_Name = cm
            data.Industry = indus
            data.Orgnization = org
            data.Address_1 = address1
            data.Address_2 =address2
            data.City = city
            data.State = state
            data.Pin_Code = pin
           
            data.save()
        return render(request, 'company_theme/Profile.html', context)
    else:
        return redirect('home')

def Internship(request):
    if request.user.is_authenticated:
        aaa = Company_Notification.objects.all().order_by("-id")[0:5]
        bbb = Company_Email.objects.all().order_by("-id")[0:5]
        cor = Courses.objects.all()
        strm = Streams.objects.all()

        context = {'cor':cor, 'strm':strm, 'aaa':aaa, 'bbb':bbb}
        

        if request.method == "POST":
            titles = request.POST['title']
            desc = request.POST['desc']
            Course = request.POST['Course']
            quali = request.POST['quali']
            opening = request.POST['opening']
            wowe = request.POST['experience']
            salary = request.POST['salary']
            process = request.POST['process']

            ins = Internships(  Description=desc, Course=Course, Title=titles, Qualification=quali, Number_of_Openings=opening, Experience=wowe, Salary=salary, Application_Process=process)
            ins.save()
        return render(request, 'company_theme/Internship.html', context)
    else:
        return redirect('home')

	

def Job(request):
    if request.user.is_authenticated:
        aaa = Company_Notification.objects.all().order_by("-id")[0:5]
        bbb = Company_Email.objects.all().order_by("-id")[0:5]
        cor = Courses.objects.all()
        strm = Streams.objects.all()

        context = {'cor':cor, 'strm':strm, 'aaa':aaa, 'bbb':bbb}
        if request.method == "POST":
            title = request.POST['title']
            desc = request.POST['desc']
            cus = request.POST['Course']
            quali = request.POST['quali']
            opening = request.POST['opening']
            exp = request.POST['exp']
            salary = request.POST['salary']
            process = request.POST['process']

            ins = Jobs(Title=title, Description=desc, Course=cus, Qualification=quali, Number_of_Openings=opening, Experience=exp, Salary=salary, Application_Process=process)
            ins.save()
        return render(request, 'company_theme/Job.html', context)
    else:
        return redirect('home')

def Company_Account_Settings(request):
    if request.user.is_authenticated:
        aaa = Company_Notification.objects.all().order_by("-id")[0:5]
        bbb = Company_Email.objects.all().order_by("-id")[0:5]
        context = {'aaa':aaa, 'bbb':bbb}
        return render(request, 'company_theme/account-setting.html', context)
    else: 
        return redirect('home')

def handleLogout(request):
    logout(request)
    return redirect('home')

def register_company(request):
    
    if request.method == 'POST':
        username = request.POST['fn']
        password = request.POST['pass']
        email = request.POST['email']
        cname = request.POST['cname']
        

        crush = User.objects.create_user(username, email, password)
        crush.first_name = cname
        crush.save()

        happy = company(user=crush,  email=email, Company_Name=cname)
        happy.save()
        messages.success(request, "Company Registered Succesfully")
        return render(request, 'company_theme/compnyr.html')
    else:
       
        return render(request, 'company_theme/compnyr.html')
   
    return render(request, 'company_theme/compnyr.html', context)

def search(request):
    query = request.GET['query']
    if len(query)>80:
        messages.warning(request, 'No results found!!!! Please refine your Query.')
    else:
        Student_search = Student.objects.filter(First_Name__icontains=query)

    if Student_search.count() == 0:
        messages.warning(request, "No search results. Please refine your query.")
    params = {'Student_search': Student_search, 'query':query}
    return render(request, 'company_theme/search.html', params)

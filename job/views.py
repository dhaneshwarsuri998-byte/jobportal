from datetime import date


from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from .models import Recruiter,Job,StudentUser
# Create your views here.

def index(request):
    return render(request, 'index.html')

def admin_login(request):
    error = None
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except Exception as e:
            print("ERROR:", e)
            error = "yes"

    d = {'error': error}

    return render(request, 'admin_login.html', d)

def user_login(request):
    error = None
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)

        if user:
            try:
                user1 = StudentUser.objects.get(user=user)

                if user1.type == "student":
                    login(request, user)
                    error = "no"
                else:
                    error = "yes"


            except StudentUser.DoesNotExist:

                error = "yes"
        else:
            error = "yes"

        d = {'error': error}
        return render(request, 'user_login.html', d)

    return render(request, 'user_login.html')

def recruiter_login(request):
    error = None
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)

        if user:
            try:
                user1 = Recruiter.objects.get(user=user)

                if user1.type == "recruiter" and user1.status != "pending":
                    login(request, user)
                    error = "no"
                else:
                    error = "not"


            except Recruiter.DoesNotExist:

                error = "yes"
        else:
            error = "yes"

        d = {'error': error}
        return render(request, 'recruiter_login.html', d)
    return render(request, 'recruiter_login.html')

def recruiter_signup(request):
    error = None

    if request.method == "POST":
        f = request.POST.get('fname')
        l = request.POST.get('lname')
        p = request.POST.get('pwd')
        e = request.POST.get('email')
        con = request.POST.get('contact')
        gen = request.POST.get('gender')
        company = request.POST.get('company')
        i = request.FILES.get('image')

        try:
            user = User.objects.create_user(
                first_name=f,
                last_name=l,
                username=e,
                password=p
            )

            Recruiter.objects.create(
                user=user,
                mobile=con,
                image=i,
                gender=gen,
                company=company,
                type="recruiter",
                status="pending"
            )

            error = "no"

        except Exception as err:
            print("ERROR:", err)
            error = "yes"

    d = {'error': error}
    return render(request, 'recruiter_signup.html', d)

def user_signup(request):
    error = None
    if request.method == "POST":
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES.get('image')
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        gen = request.POST['gender']

        try:
            user = User.objects.create_user(
                first_name=f,
                last_name=l,
                username=e,
                password=p
            )

            StudentUser.objects.create(
                user=user,
                mobile=con,
                image=i,
                gender=gen,
                type="student",

            )

            error = "no"



        except Exception as e:

            print("ERROR:", e)

            error = "yes"

    d = {'error': error}
    return render(request, 'user_signup.html', d)

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request, 'user_home.html')

def Logout(request):
    logout(request)
    return redirect('index')

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    d = {'recruiter': recruiter}
    return render(request, 'recruiter_home.html',d)

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')

def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = StudentUser.objects.all()
    d = {'data': data}
    return render(request, 'view_users.html',d)

def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student = User.objects.get(id=pid)
    student.delete()
    return redirect('view_users')

def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status="pending")
    d = {'data': data}
    return render(request, 'recruiter_pending.html',d)

def change_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=None
    recruiter = Recruiter.objects.get(id=pid)
    if request.method == "POST":
        s = request.POST['status']
        recruiter.status = s
        try:
            recruiter.save()
            error = "no"
        except:
            error = "yes"
    d = {'recruiter': recruiter, 'error': error}
    return render(request, 'change_status.html',d)

def recruiter_accepted(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status="Accept")
    d = {'data': data}
    return render(request, 'recruiter_accepted.html',d)

def recruiter_rejected(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status="Reject")
    d = {'data': data}
    return render(request, 'recruiter_rejected.html',d)

def recruiter_all(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.all()
    d = {'data': data}
    return render(request, 'recruiter_all.html',d)

def delete_recruiter(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    recruiter= User.objects.get(id=pid)
    recruiter.delete()
    return redirect('view_users')

def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=None
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u =User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'change_passwordadmin.html',d)

def add_job(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')

    error = None

    if request.method == "POST":
        title = request.POST['title']
        salary = request.POST['salary']
        location = request.POST['location']
        skills = request.POST['skills']
        description = request.POST['description']
        experience = request.POST['experience']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        user = request.user
        recruiter = Recruiter.objects.get(user=user)

        try:
            Job.objects.create(
                recruiter=recruiter,
                title=title,
                salary=salary,
                location=location,
                skills=skills,
                description=description,
                experience=experience,
                start_date=start_date,
                end_date=end_date,
                creation_date=date.today()
            )
            error = "no"

        except Exception:
            error = "yes"

    d = {'error': error}
    return render(request, 'add_job.html', d)



def job_list(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    job = Job.objects.filter(recruiter=recruiter)
    d = {'job': job}

    return render(request, 'job_list.html',d)

def edit_jobdetail(request, pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')

    error = None
    job = Job.objects.get(id=pid)

    if request.method == "POST":
        title = request.POST.get('title')
        salary = request.POST.get('salary')
        location = request.POST.get('location')
        skills = request.POST.get('skills')
        description = request.POST.get('description')
        experience = request.POST.get('experience')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        job.title = title
        job.salary = salary
        job.location = location
        job.skills = skills
        job.description = description
        job.experience = experience

        if start_date:
            job.start_date = start_date

        if end_date:
            job.end_date = end_date

        try:
            job.save()
            error = "no"
        except Exception:
            error = "yes"

    d = {'error': error, 'job': job}
    return render(request, 'edit_jobdetail.html', d)

def latest_jobs(request):
    job = Job.objects.all()
    d = {'job': job}
    return render(request, 'latest_jobs.html',d)





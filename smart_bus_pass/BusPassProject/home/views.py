from django.shortcuts import render , HttpResponse
from home import models

# Create your views here.
# Website page starts
def home(request):
    return render(request, 'home.html')

def login_student(request):
    content = {'type':'1'}
    return render(request, 'login.html',content)
def register(request):
    college = models.College.objects.all().values()
    context = {'college_data': college }
    return render(request,'register.html',context)
# Website page ends

# Student dashboard starts

def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def profile(request):

    if request.method == "POST":
        name = request.POST['name'],
        fathername = request.POST['fathername'],
        college = request.POST['collegename'],
        roll = request.POST['roll'],
        course = request.POST['course'],
        aadhar_number = request.POST['aadhar'],
        previous_pass = request.POST['previous_pass'],
        pass_number = request.POST['pass_number']

        content = models.Student(
            name=name[0],
            fathername= fathername[0],
            college=models.College.objects.get(college_id = college[0]),
            roll=roll[0],
            course=course[0],
            aadhar_number=aadhar_number[0],
            previous_pass=bool(previous_pass[0]),
            pass_number=pass_number[0])
        content.save()

    college = models.College.objects.all().values()
    std = models.Student.objects.first()
    context = {'college_data': college ,'student_data': std }
    return render(request, 'profile.html',context)

def set_route(request):

    college = models.Route.objects.all().values()
    context = {'route_data': college }
    return render(request,'set_route.html',context)

def view_route(request):
    return render(request,'view_route.html')

def verification(request):
    return render(request,'verification.html')

def generate_pass(request):
    return render(request,'generate_pass.html')

# Student dashboard ends

# College dashboard starts
def college_dashboard(request):
    return render(request,'college_dashboard.html')

def student_verification(request):
    return render(request,'student_verification.html')

def verified_student(request):
    return render(request,'verified_student.html')

# College dashboard ends

# Manager dashboard starts
def manager_dashboard(request):
    return render(request,'manager_dashboard.html')

def approval(request):
    if request.POST=="paid":
        print("approved")
    return render(request,'approval.html')

def generate(request):
    return render(request,'generate.html')

def report(request):
    return render(request,'report.html')

# Manager dashboard ends

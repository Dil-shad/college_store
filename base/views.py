from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy

from .models import Department, Course, Purpose, Material, Profile
from django.http import JsonResponse
# Create your views here.


def index(request):
    return render(request, 'home.html')
def profile(request):
    user_profile = None  # Initialize user_profile here

    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department', '')
        course = request.POST.get('course')
        purpose = request.POST.get('purpose')

        try:
            department = Department.objects.get(id=department)
            course = Course.objects.get(id=course)
            purpose = Purpose.objects.get(id=purpose)
            material_names = request.POST.getlist('materials')
            
            user_profile = Profile(
                name=name,
                dob=dob,
                age=age,
                gender=gender,
                phone_number=phone,
                mail_id=email,
                address=address,
                department=department,
                course=course,
                purpose=purpose,
            )
            user_profile.save()

            for material_name in material_names:
                material, created = Material.objects.get_or_create(name=material_name)
                user_profile.materials.add(material)

            messages.success(request, f"Request '{purpose}' is submitted successfully")
            return redirect('profile')

        except (Department.DoesNotExist, Course.DoesNotExist, Purpose.DoesNotExist):
            messages.error(request, "Invalid department, course, or purpose selected. Please try again.")
        except Exception as e:
            messages.error(request, f"Invalid inputs: {str(e)}. Please try again.")

    departments = Department.objects.all()
    purpose = Purpose.objects.all()
    context = {
        'departments': departments,
        'purpose': purpose,
    }
    return render(request, 'profile.html', context)


def get_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id)
    course_data = [{'id': course.id, 'name': course.name}
                   for course in courses]
    return JsonResponse(course_data, safe=False)

def logout(request):
    auth.logout(request)
    return redirect('index')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                # Use redirect instead of reverse_lazy
                return redirect('profile')
            else:
                messages.error(
                    request, 'Invalid username or password. Please try again.')
        else:
            messages.error(
                request, 'Invalid input. Please check your username and password fields.')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('confirm_password')

        if username and password and password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            else:
                user = User.objects.create_user(
                    username=username, password=password)
                user.save()
                messages.success(
                    request, 'Registration successful. You can now log in.')
                return redirect('login')
        else:
            messages.error(
                request, 'Invalid input. Please check your username and password fields.')

    return render(request, 'register.html')

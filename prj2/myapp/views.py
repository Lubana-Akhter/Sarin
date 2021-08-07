from django.shortcuts import render, redirect
from myapp.models import Student
from myapp.forms import StudentForm, EmailForm
from django.core.paginator import Paginator
from django.contrib import messages

from django.core.mail import EmailMessage #send_mail
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'homemap.html', {'title':'Home'})

def index(request):
    std = Student.objects.order_by('-id') 
    paginator = Paginator(std, 20)
    page = request.GET.get('page')
    students =  paginator.get_page(page)
    context = {'title': 'List of students', 'students':students}
    return render(request, 'student/index.html',context)

def show(request,id):
    student = Student.objects.get(pk = id)
    form = StudentForm(request.POST or None, instance = student)
    context = {'title':'Detais', 'student':student}
    return render(request, 'student/details.html', context)

def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Student inserted successfully !")
            return redirect('student:index') 
    else:
        form = StudentForm()    
    context = {'title':'Detais', 'form': form}  #this is dictionary
    return render(request, 'student/create.html', context)

def edit(request,id):
    student = Student.objects.get(pk = id)
    form = StudentForm(request.POST or None, instance = student)
    context = {'title':'edit', 'student':student, 'form': form}
    return render(request, 'student/edit.html', context)


def update(request,id):
    student = Student.objects.get(pk = id)
    form = StudentForm(request.POST or None, instance = student)
    if form.is_valid():
        form.save()
        messages.success(request,"Student updated successfully !")
        return redirect('student:index') 
    else:
        print('invalid data')  
    context = {'title':'edit', 'form':form}
    return render(request, 'student/edit.html', context)

def delete(request,id):
    student = Student.objects.get(pk = id)
    student.delete()
    messages.add_message(request, messages.SUCCESS,"Student delete successfully !")
    return redirect('student:index')

def sendEmail(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            sub = form.cleaned_data['subject']
            mes = form.cleaned_data['message']
            email = form.cleaned_data['email']
            try:
                mail = EmailMessage(sub, mes, settings.EMAIL_HOST_USER,[email])
                if request.FILES:
                    files = request.FILES.getlist('attach')
                    for f in files:
                        mail.attach(f.name, f.read(), f.content_type)
                    mail.send()
                    messages.success(request, 'Email sent successfully')
                    return redirect('student:index')
            except:
                messages.error(request, 'sorry  !!!  Email not sent !!')
    else:
        form = EmailForm()

    context = {'title':'Email', 'form':form}
    return render(request, 'email_form.html', context) 
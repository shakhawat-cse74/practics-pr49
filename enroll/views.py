from django.shortcuts import render
from .forms import StudentRegistration,TeacherRegistration
# Create your views here.
#For Student Registration

def studentdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    return render(request,'enroll/studentregistration.html', {'form':fm})



#For Teacher Registration

def teacherdata(request):
    if request.method == 'POST':
        fmt = TeacherRegistration(request.POST)
        if fmt.is_valid():
            fmt.save()
            fmt = TeacherRegistration()
    else:
        fmt = TeacherRegistration()
    return render (request, 'enroll/teacherregistration.html', {'form':fmt})
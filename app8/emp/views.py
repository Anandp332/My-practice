from django.shortcuts import render
from emp.forms import EmpSignUpForm
def homev(request):
    emp1 = EmpSignUpForm()
    return render(request,'Signup.html',{'empform':emp1})


# Create your views here.

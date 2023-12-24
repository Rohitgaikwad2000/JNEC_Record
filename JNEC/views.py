from django.shortcuts import render, HttpResponse, redirect
from .models import Placed_Student
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/user/login')
def Add_Record(request):
    if request.method == "GET":
        return render(request, "create.html")
    elif request.method == "POST":
        data = request.POST
        Placed_Student.objects.create(First_Name = data.get("first_name").title(), Last_Name = data.get("last_name").title(),
                                      Department = data.get("department").title(), Company_Name = data.get("company_name").title(),
                                      Salary = data.get("salary"))  
    return HttpResponse("Added Succesfully....!")


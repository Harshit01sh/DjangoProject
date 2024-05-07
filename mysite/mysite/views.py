from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    # data = {
    #     'title':'Home Page',
    #     'clist':['Php','Java','Django'],
    #     'numbers':[10,20,30,40,50],
    #     'student_details':[
    #         {'name':'Harshit', 'phone':7877895355},
    #         {'name':'Sharma', 'phone':6367720679}
    #      ]
    # }
    return render(request,"index.html")

def aboutus(request):
    return HttpResponse("Welcome to mysite")

def course(request):
    return HttpResponse("Welcome to mysite courses")

def courseDetails(request,courseid):
    return HttpResponse(courseid)
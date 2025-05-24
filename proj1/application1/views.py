from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def testCase1(request):
    return HttpResponse("<h1>My Django Project</h1>")
def testCase2(request):
    return HttpResponse("This is Django")
def testCase3(request):
    return HttpResponse("This is testcase 3")

class Test_Case1(View):
    def get(self,request):
        return HttpResponse("<h1>Welcome to class based views</h1>")

class Test_Case2(View):
    def get(self, request):
        return HttpResponse("This is testcase 2")
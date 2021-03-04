from django.shortcuts import render

# Create your views here.
def createaccount(request):
    return render(request,'interpretor/account-create.html')
def dashboard(request):
    return render(request,'interpretor/dashboard.html')
def login(request):
    return render(request,'interpretor/login.html')
def eventCreate(request):
    return render(request,'interpretor/event-create.html')
def eventModify(request):
    return render(request,'interpretor/event-modify.html')
def logout(request):
    return render(request,'interpretor/logout.html')
def submitPython(request):
    return render(request,'interpretor/submit-python.html')
def submitToken(request):
    return render(request,'interpretor/submit-token.html')
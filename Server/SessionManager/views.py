from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "login.html")

def sessionmanagement(request):
    return render(request, "sessionmanagement.html")

def restrictedaccounts(request):
    return render(request, "restrictedaccounts.html")

def lockedsystems(request):
    return render(request, "lockedsystems.html")

def multi_sessioncards(request):
    return render(request, "multisessioncards.html")

def breakoverride(request):
    return render(request, "breakoverride.html")

def reports(request):
    return render(request, "reports.html")

def sendmessage(request):
    return render(request, "sendmessage.html")

def printqueue(request):
    return render(request, "printqueue.html")

def adjustfunds(request):
    return render(request, "adjustfunds.html")

def expresssession(request):
    return render(request, "expresssession.html")

def settigns(request):
    return render(request, "settings.html")

def reportlogs(request):
    return render(request, "reportlogs.html")
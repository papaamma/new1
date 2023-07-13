from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        usn = request.POST['username']
        fr = request.POST['first_name']
        la = request.POST['last_name']
        ma = request.POST['mail']
        pa = request.POST['password']
        pa1 = request.POST['password1']
        if pa == pa1:
            if User.objects.filter(username=usn).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            elif User.objects.filter(email=ma).exists():
                messages.info(request, "Email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=usn, first_name=fr, last_name=la, email=ma, password=pa)
                user.save()
                print("User created")
                return redirect('login')
        else:
            print("Passwords do not match")
            return redirect('register')
    return render(request, 'register.html')
def login(request):
    if request.method=='POST':
        usern= request.POST['username']
        passw=request.POST['password']
        user=auth.authenticate(username=usern ,password= passw)
        if  user is not None :
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid entry')
            return redirect('login')
    return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
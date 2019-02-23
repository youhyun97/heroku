from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            auth.login(request, user) # 회원가입 후 자동 로그인 되도록...
            return redirect('home')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            # authenticate함수는 회원이 맞는지 확인해줌. DB의 내용과 일치하는지!  
            user = auth.authenticate(request, username=username, password=password)
            # 회원이 존재한다면...
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            # 회원이 아니라면...
            else:
                return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')
from django.shortcuts import render,redirect,HttpResponse,redirect, get_object_or_404
from .forms import UserExtraForm,Userwp,UserForm,User
from .models import UserExtra
from django.contrib.auth import authenticate,login,logout
def signin(request):
    if request.method == 'GET':
        return render(request,'account/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.user_type == 'admin':
                return redirect('ltd')
            elif user.user_type =='staff':
                return HttpResponse("staff Index page")
            else:
                return redirect('user_index')
        else:
            return HttpResponse("Invalid Username/password")
def register(request):
    if request.method == 'GET':
        context = {
            'form1': UserForm(),
            'form2': UserExtraForm()
        }
        return render(request, 'account/register.html',context)
    elif request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = UserExtraForm(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            obj1 = form1.save(commit=False)
            obj2 = form2.save(commit=False)
            obj1.set_password(form1.cleaned_data['password'])
            obj1.User_type ='user'
            obj1.save()
            obj2.user =obj1
            obj2.save()
            return redirect('account_signin')
        else:
            context = {
                'form1': form1,
                'form2': form2
            }
            return render(request,'account/edit.html',context)
def update(request, id):
    # Retrieve the user object with the given id
    user = get_object_or_404(UserExtra, id=id)

    if request.method == 'POST':
        # Create form instances with the new POST data and the existing user object
        form1 = Userwp(request.POST, instance=user.user)
        form2 = UserExtraForm(request.POST, request.FILES, instance=user)

        # Check if the form data is valid
        if form1.is_valid() and form2.is_valid():
            obj1 = form1.save(commit=False)
            obj2 = form2.save(commit=False)
            obj1.User_type ='user'
            obj1.save()
            obj2.user =obj1
            obj2.save()
            return redirect('user_index')
    else:
        # Create form instances with the existing user object
        form1 = Userwp(instance=user.user)
        form2 = UserExtraForm(instance=user)

    context = {
        'form1': form1,
        'form2': form2,
    }

    return render(request, 'account/edit.html', context)

def logout_action(request):
    logout(request)
    return redirect('home') 
           
def delete(request, id):
    user_extra = get_object_or_404(UserExtra, id=id)
    user = user_extra.user
    if request.method == 'GET':
        user.delete()
        user_extra.delete()
        return redirect('user_index')
    else:
        return HttpResponse("Invalid request method")
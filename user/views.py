from django.shortcuts import render, redirect
from .forms import ReportForm,LtdAdmin
from django.http import HttpResponse
from django.contrib import messages
from account.models import UserExtra
from .models import Report,Vote,SolvedImage
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated:
        user_extra = UserExtra.objects.filter(user=request.user).first()
        context = {
            'issues': Report.objects.filter(issue_status='0').order_by('-id'),
            'profile': user_extra.issuer_image if user_extra else None
        }
    else:
        context={
            'issues': Report.objects.filter(issue_status='0').order_by('-id')
        }
    return render(request, 'user/index.html',context)


def home(request):
    return render(request,'user/home.html')

@login_required
def report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = UserExtra.objects.get(user=request.user)
            obj.save()
            return redirect('user_report')
    else:
        form = ReportForm()
    return render(request,'user/report.html',{'form':form})
def profile(request):
    user_extra = UserExtra.objects.get(user=request.user)
    context = {'data': user_extra}
    print(context)
    return render(request, 'user/profile.html',context)
def history(request):
    user = UserExtra.objects.get(user=request.user)
    if request.method == 'GET':
        context = {
            'reports': Report.objects.filter(user=user)
        }
        return render(request, 'user/history.html',context)    
def edit(request,id):
    report = Report.objects.get(pk=id)
    if request.method == 'POST':
        form = ReportForm(data=request.POST,files=request.FILES,instance=report)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = UserExtra.objects.get(user=request.user)
            obj.save()
            return redirect('user_history')
    else:
        form = ReportForm(instance=report)
    return render(request,'user/edit.html',{'form': form})        
def delete(request,id):
    Report.objects.get(pk=id).delete()
    return redirect('history')    
@login_required
def upvote(request, id):
    report = Report.objects.get(pk=id)
    issue_title = report.issue_title
    user = UserExtra.objects.get(user=request.user) 
    if Vote.objects.filter(user=user, report=report).exists():
        return HttpResponse("Already Voted")
    else:
        vote = Vote(user=user, report=report)
        vote.save()
        report.vote_count += 1
        report.save()
        return HttpResponse("success")
        #return redirect('index.html')    
def ltd(request):
    ltds = Report.objects.filter(issue_status='0') | Report.objects.filter(issue_status='1')
    context = {'ltds': ltds}
    return render(request, 'ltd.html', context)
    
def upload_solved_image(request, report_id):
    report = Report.objects.get(pk=report_id)
    if request.method == 'POST':
        form = LtdAdmin(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.report = report
            obj.save()
            report.issue_status = '1'
            report.save()
            return redirect('ltd')
        else:
            messages.error(request, 'Error occurred while uploading solved image.')
    else:
        form = LtdAdmin()
    return render(request, 'user/ltd.html', {'form': form, 'report': report})
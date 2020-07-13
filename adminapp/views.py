from django.shortcuts import render,redirect
from django.contrib import messages
from adminapp.forms import AdminForms
from adminapp.models import AdminnModel
from django.http import HttpResponse
# Create your views here.
def adminloginpage(request):
    return render(request,"adminloginpage.html")
def adminvalidation(request):
    adminname=request.POST.get("a1")
    adminpassword=request.POST.get("a2")
    if adminname=="sowmya" and adminpassword=="sree":
        return render(request,"adminpage.html",{"data":adminname})
    else:
        messages.error(request,"Invalid Admin")
        return redirect('adminloginpage')
def schedule_new_class(request):
    af = AdminForms()
    return render(request,"schedule_new_class.html",{'form':af})
def View_all_Scheduled_classes(request):
    am=AdminnModel.objects.all()
    return render(request,"View_all_Scheduled_classes.html",{"data":am})
def admin_cousre_reg(request):
    af=AdminForms(request.POST)
    if af.is_valid():
        af.save()
        messages.success(request, "registration is succesfull")
        return redirect('/adminn/schedule_new_class/')
    else:
        messages.error(request,"registration is failed")
        return redirect('schedule_new_class')
def update_viewall_admin(request):
    cn=request.GET.get("coursename")
    res = AdminnModel.objects.get(Coursename=cn)
    af=AdminForms(request.POST)
    return render(request,"update_viewall_admin.html",{'data':res})
def delete_viewall_admin(request):
    cn = request.GET.get("coursename")
    AdminnModel.objects.filter(Coursename=cn).delete()
    messages.success(request,"sucessfully deleted")
    return redirect('View_all_Scheduled_classes')
def updated_schedule(request):
    cn=request.POST.get("coursename")
    f=request.POST.get("faculty")
    date=request.POST.get("date")
    time=request.POST.get("time")
    fee=request.POST.get("fee")
    duration=request.POST.get("duration")
    AdminnModel.objects.filter(Coursename=cn).update(Faculty=f,Date=date,Time=time,Fee=fee,Duration=duration)
    messages.success(request,"sucessfully updated")
    return redirect("View_all_Scheduled_classes")
def admin_logout(request):
    return redirect('adminloginpage')
from django.shortcuts import render,redirect
from student.forms import StudentForms
from student.models import StudentModel,EnroleListModel
from adminapp.models import AdminnModel
from django.contrib import messages
from adminapp.forms import AdminForms
from django.db.models import Q

# Create your views here.
def studenthome(request):
    return render(request,"studenthomepage.html")
def student_reg(request):
    sf=StudentForms()
    return render(request,"student_reg.html",{"form":sf})
def student_login(request):
    return render(request, "student_login.html")
def student_search(request):
    return render(request, "student_search.html")
def student_contactus(request):
    return render(request, "student_contactus.html")
def student_registred_process(request):
    sf=StudentForms(request.POST)
    if sf.is_valid():
        sf.save()
        messages.success(request, "registration is succesfull")
        return redirect('home')
    else:
        messages.error(request,"registration is failed")
        return redirect('home')
def student_page(request):
    name=request.POST.get("s1")
    password=request.POST.get("s2")
    cor=AdminnModel.objects.all()
    try:
        result=StudentModel.objects.get(Q(Name=name,Password=password))
        request.session['contact']=result.Contactno
        return render(request,'student_page.html',{'data':result,"courses":cor})
    except StudentModel.DoesNotExist:
        messages.error(request,"Invalid User Details")
        return redirect('student_login')
    # if StudentModel.objects.filter(Name=name,Password=password):
    #     res=StudentModel.objects.filter(Name=name)
    #     return render(request,"student_page.html",{"data":res,"name":name})
    # else:
    #     messages.error(request,"Invalid User")
    #     return redirect('student_login')

def enrol_course(request):
    af=AdminnModel.objects.all()
    return render(request, "enrol_course.html", {"data": af})
def enrolling_process(request):
    forms=AdminForms
    cno=request.POST.get("cno")
    contact=request.POST.get("contact")
    try:
        EnroleListModel.objects.get(Contactno_id=contact,idno_id=cno)
        messages.error(request,"Already enrolled")
        return redirect('enrol_course')
    except EnroleListModel.DoesNotExist:
        EnroleListModel.objects.create(Contactno_id=contact,idno_id=cno)
        messages.success(request,"Enrolled Sucessfully")
        return redirect('enrol_course')
    # # response=redirect('enrol_course')
    # # response.set_cookie(sco,cid)
    # # return response
    # # # data={"cid":cid,"sco":sco}
    # # # EnroleListModel(studentcontctno=sco,courseid=cid).save()
    # # # return render(request.COOKIES,"enrol_course.html")
    # EnroleListModel(studentcontctno=sco,courseid=cid).save()
    # return render(request,'enrol_course.html',{"sco":sco})
def Viewall_the_enrolled_courses(request):
    contact=request.GET.get('contact')
    res=EnroleListModel.objects.filter(Contactno_id=contact)
    data=[AdminnModel.objects.get(idno=x.idno_id)for x in res]
    return render(request,"Viewall_the_enrolled_courses.html",{"data":data})
def cancel_enrolled_courses(request):
    contact = request.GET.get('contact')
    res = EnroleListModel.objects.filter(Contactno_id=contact)
    data = [AdminnModel.objects.get(idno=x.idno_id) for x in res]
    return render(request, "cancel_enrolled_courses.html", {"data": data})
def student_logout(request):
    del request.session['contact']
    return redirect('student_login')
def cancelling_enrolled_course(request):
    cno=request.POST.get('cno')
    contact=request.POST.get('contact')
    EnroleListModel.objects.get(Contactno_id=contact,idno_id=cno).delete()
    res = EnroleListModel.objects.filter(Contactno_id=contact)
    data = [AdminnModel.objects.get(idno=x.idno_id) for x in res]
    return render(request, "cancel_enrolled_courses.html", {"data": data})
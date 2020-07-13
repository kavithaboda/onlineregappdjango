from django.shortcuts import render,redirect
from student.forms import StudentForms
from student.models import StudentModel
from adminapp.models import AdminnModel
from django.contrib import messages
from adminapp.forms import AdminForms
from student.models import EnroleListModel

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
    if StudentModel.objects.filter(Name=name,Password=password):
        res=StudentModel.objects.filter(Name=name)
        return render(request,"student_page.html",{"data":res,"name":name})
    else:
        messages.error(request,"Invalid User")
        return redirect('student_login')
def enrol_course(request):
    af=AdminnModel.objects.all()
    sco=request.GET.get("sco")
    sid=request.GET.get("sid")
    response = render(request,'enrol_course.html',{"dataa":af})
    response.set_cookie(sco,sid)
    return response

    # res={"data": af, "sco": sco}
    # return render(request,"enrol_course.html",{"data":af,"sco":sco})
def enrolling_process(request):
    # # forms=AdminForms
    cid=request.GET.get("cid")
    sco=request.GET.get("sco")
    data={"cid":cid,"sco":sco}
    EnroleListModel(studentcontctno=sco,courseid=cid).save()
    return redirect('enrol_course',{"data":request.COOKIES})
def Viewall_the_enrolled_courses(request):
    af = AdminnModel.objects.all()
    sco=request.GET.get("sid")
    res=EnroleListModel.objects.all()

    # l1=[]
    # for x in res:
    #     print(x.courseid)
    #     l1.append(x.courseid)
    # print(l1)
    # student_data=[AdminnModel.objects.get(Coursename=x.courseid)for x in res["courseid"]]
    # print(student_data)
    return render(request,"Viewall_the_enrolled_courses.html",{"data":res})


def cancel_enrolled_courses(request):
    return render(request,"cancel_enrolled_courses.html")


def student_logout(request):
    return redirect('student_login')
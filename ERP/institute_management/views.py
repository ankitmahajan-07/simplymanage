from django.shortcuts import render,redirect
from requests import request
from .models import *
from datetime import datetime
from django.core.files.storage import FileSystemStorage

# Create your views here.
user_details = ""

def log_in(request):
    get_inst_name = request.POST.get('inst_name')
    get_own_name = request.POST.get('own_name')
    get_city = request.POST.get('city')
    get_mobile = request.POST.get('mobile')
    get_email = request.POST.get('email')
    get_username = request.POST.get('username')
    get_pwd = request.POST.get('pwd')
    get_state = request.POST.get('state')

    fetch_user = SignUp.objects.filter(Username=get_username)
    fetch_email = SignUp.objects.filter(Email=get_email)
    fetch_mobile = SignUp.objects.filter(Mobile=get_mobile)
    if fetch_user.exists():
        print("Username already exits")
        return render(request, "Home.html")
    else:
        if fetch_email.exists():
            print("Email already exits")
            return render(request, "Home.html")
        else:
            if fetch_mobile.exists():
                print("Mobile Name already exits")
                return render(request, "Home.html")
            else:
                my_new_sign_up = SignUp(Institute_Name=get_inst_name,
                                        Owner_Name=get_own_name,
                                        State=get_state,
                                        City=get_city,
                                        Mobile=get_mobile,
                                        Email=get_email,
                                        Username=get_username,
                                        Password=get_pwd)
                my_new_sign_up.save()
                print("Datails saved to database")
                return render(request, "Home.html")

def dashboard(request):
    global user_details
    if request.method =="POST" and 'log_in' in request.POST:
        get_username = request.POST.get('uname')
        get_pwd = request.POST.get('pword')
        remember = request.POST.get('remember')

        fetch_user = SignUp.objects.filter(Username=get_username, Password=get_pwd)
        if fetch_user.exists():
            user_details = SignUp.objects.get(Username=get_username)
            if remember == "on":
                admission = Admission.objects.filter(Institute_Id=user_details).values_list('Date')
                jan = feb = mar = apr = may = june = july = aug = sept = october = nov = dec = 0
                date = month = year = 0
                now = datetime.now()
                get_date = now.strftime('%d')
                print(get_date)
                get_month = now.strftime('%m')
                print(get_month)
                get_year = now.strftime('%Y')
                print(get_year)
                for i in admission:
                    sp = str(i)
                    sp1 = sp.split("'")
                    var = sp1[1].split('/')
                    if var[0] == get_date:
                        date += 1
                    if var[1] == get_month:
                        month += 1
                    if var[2] == get_year:
                        year += 1
                    if var[1] == '01' or var[1] == '1':
                        jan += 1
                    elif var[1] == '02' or var[1] == '2':
                        feb += 1
                    elif var[1] == '03' or var[1] == '3':
                        mar += 1
                    elif var[1] == '04' or var[1] == '4':
                        apr += 1
                    elif var[1] == '05' or var[1] == '5':
                        may += 1
                    elif var[1] == '06' or var[1] == '6':
                        june += 1
                    elif var[1] == '07' or var[1] == '7':
                        july += 1
                    elif var[1] == '08' or var[1] == '8':
                        aug += 1
                    elif var[1] == '09' or var[1] == '9':
                        sept += 1
                    elif var[1] == '10':
                        october += 1
                    elif var[1] == '11':
                        nov += 1
                    else:
                        dec += 1

                admission = [jan, feb, mar, apr, may, june, july, aug, sept, october, nov, dec, date, month, year]
                receipt = Receipt.objects.filter(Institute_Id=user_details).values_list('Date', 'Amount')
                jan = feb = mar = apr = may = june = july = aug = sept = october = nov = dec = 0
                date = month = year = 0
                for i in receipt:
                    sp = str(i)
                    sp1 = sp.split("'")
                    var = sp1[1].split('/')
                    if var[0] == get_date:
                        date += int(i[1])
                    if var[1] == get_month:
                        month += int(i[1])
                    if var[2] == get_year:
                        year += int(i[1])
                    if var[1] == '01' or var[1] == '1':
                        jan += int(i[1])
                    elif var[1] == '02' or var[1] == '2':
                        feb += int(i[1])
                    elif var[1] == '03' or var[1] == '3':
                        mar += int(i[1])
                    elif var[1] == '04' or var[1] == '4':
                        apr += int(i[1])
                    elif var[1] == '05' or var[1] == '5':
                        may += int(i[1])
                    elif var[1] == '06' or var[1] == '6':
                        june += int(i[1])
                    elif var[1] == '07' or var[1] == '7':
                        july += int(i[1])
                    elif var[1] == '08' or var[1] == '8':
                        aug += int(i[1])
                    elif var[1] == '09' or var[1] == '9':
                        sept += int(i[1])
                    elif var[1] == '10':
                        october += int(i[1])
                    elif var[1] == '11':
                        nov += int(i[1])
                    elif var[1] == '12':
                        dec += int(i[1])
                receipt = [jan, feb, mar, apr, may, june, july, aug, sept, october, nov, dec, date, month, year]
                enquiry = Enquiry.objects.filter(Institute_Id=user_details).values_list('Date')
                jan = feb = mar = apr = may = june = july = aug = sept = october = nov = dec = 0
                date = month = year = 0
                for i in enquiry:
                    sp = str(i)
                    sp1 = sp.split("'")
                    var = sp1[1].split('/')
                    if var[0] == get_date:
                        date += 1
                    if var[1] == get_month:
                        month += 1
                    if var[2] == get_year:
                        year += 1
                    if var[1] == '01' or var[1] == '1':
                        jan += 1
                    elif var[1] == '02' or var[1] == '2':
                        feb += 1
                    elif var[1] == '03' or var[1] == '3':
                        mar += 1
                    elif var[1] == '04' or var[1] == '4':
                        apr += 1
                    elif var[1] == '05' or var[1] == '5':
                        may += 1
                    elif var[1] == '06' or var[1] == '6':
                        june += 1
                    elif var[1] == '07' or var[1] == '7':
                        july += 1
                    elif var[1] == '08' or var[1] == '8':
                        aug += 1
                    elif var[1] == '09' or var[1] == '9':
                        sept += 1
                    elif var[1] == '10':
                        october += 1
                    elif var[1] == '11':
                        nov += 1
                    else:
                        dec += 1

                enquiry = [jan, feb, mar, apr, may, june, july, aug, sept, october, nov, dec, date, month, year]
                params = {'user_details': user_details, 'admission': admission, 'receipt': receipt, 'enquiry': enquiry}
                response = render(request, "dashbrd.html", {'params':params})
                response.set_cookie('remember', get_username)
                return response
            else:
                admission = Admission.objects.filter(Institute_Id=user_details).values_list('Date')
                jan = feb = mar = apr = may = june = july = aug = sept = october = nov = dec = 0
                date = month = year = 0
                now = datetime.now()
                get_date = now.strftime('%d')
                get_month = now.strftime('%m')
                get_year = now.strftime('%Y')
                for i in admission:
                    sp = str(i)
                    sp1 = sp.split("'")
                    var = sp1[1].split('/')
                    if var[0] == get_date:
                        date += 1
                    if var[1] == get_month:
                        month += 1
                    if var[2] == get_year:
                        year += 1
                    if var[1] == '01' or var[1] == '1':
                        jan += 1
                    elif var[1] == '02' or var[1] == '2':
                        feb += 1
                    elif var[1] == '03' or var[1] == '3':
                        mar += 1
                    elif var[1] == '04' or var[1] == '4':
                        apr += 1
                    elif var[1] == '05' or var[1] == '5':
                        may += 1
                    elif var[1] == '06' or var[1] == '6':
                        june += 1
                    elif var[1] == '07' or var[1] == '7':
                        july += 1
                    elif var[1] == '08' or var[1] == '8':
                        aug += 1
                    elif var[1] == '09' or var[1] == '9':
                        sept += 1
                    elif var[1] == '10':
                        october += 1
                    elif var[1] == '11':
                        nov += 1
                    else:
                        dec += 1

                admission = [jan, feb, mar, apr, may, june, july, aug, sept, october, nov, dec, date, month, year]
                receipt = Receipt.objects.filter(Institute_Id=user_details).values_list('Date', 'Amount')
                jan = feb = mar = apr = may = june = july = aug = sept = october = nov = dec = 0
                date = month = year = 0
                for i in receipt:
                    sp = str(i)
                    sp1 = sp.split("'")
                    var = sp1[1].split('/')
                    if var[0] == get_date:
                        date += int(i[1])
                    if var[1] == get_month:
                        month += int(i[1])
                    if var[2] == get_year:
                        year += int(i[1])
                    if var[1] == '01' or var[1] == '1':
                        jan += int(i[1])
                    elif var[1] == '02' or var[1] == '2':
                        feb += int(i[1])
                    elif var[1] == '03' or var[1] == '3':
                        mar += int(i[1])
                    elif var[1] == '04' or var[1] == '4':
                        apr += int(i[1])
                    elif var[1] == '05' or var[1] == '5':
                        may += int(i[1])
                    elif var[1] == '06' or var[1] == '6':
                        june += int(i[1])
                    elif var[1] == '07' or var[1] == '7':
                        july += int(i[1])
                    elif var[1] == '08' or var[1] == '8':
                        aug += int(i[1])
                    elif var[1] == '09' or var[1] == '9':
                        sept += int(i[1])
                    elif var[1] == '10':
                        october += int(i[1])
                    elif var[1] == '11':
                        nov += int(i[1])
                    elif var[1] == '12':
                        dec += int(i[1])
                receipt = [jan, feb, mar, apr, may, june, july, aug, sept, october, nov, dec, date, month, year]
                enquiry = Enquiry.objects.filter(Institute_Id=user_details).values_list('Date')
                jan = feb = mar = apr = may = june = july = aug = sept = october = nov = dec = 0
                date = month = year = 0
                for i in enquiry:
                    sp = str(i)
                    sp1 = sp.split("'")
                    var = sp1[1].split('/')
                    if var[0] == get_date:
                        date += 1
                    if var[1] == get_month:
                        month += 1
                    if var[2] == get_year:
                        year += 1
                    if var[1] == '01' or var[1] == '1':
                        jan += 1
                    elif var[1] == '02' or var[1] == '2':
                        feb += 1
                    elif var[1] == '03' or var[1] == '3':
                        mar += 1
                    elif var[1] == '04' or var[1] == '4':
                        apr += 1
                    elif var[1] == '05' or var[1] == '5':
                        may += 1
                    elif var[1] == '06' or var[1] == '6':
                        june += 1
                    elif var[1] == '07' or var[1] == '7':
                        july += 1
                    elif var[1] == '08' or var[1] == '8':
                        aug += 1
                    elif var[1] == '09' or var[1] == '9':
                        sept += 1
                    elif var[1] == '10':
                        october += 1
                    elif var[1] == '11':
                        nov += 1
                    else:
                        dec += 1

                enquiry = [jan, feb, mar, apr, may, june, july, aug, sept, october, nov, dec, date, month, year]
                params = {'user_details': user_details, 'admission': admission, 'receipt': receipt, 'enquiry': enquiry}
                return render(request, "dashbrd.html", {'params': params})
        else:
            error='Wrong username or password'
            params={'error':error}
            return render(request, "Home.html", {'params':params})
    else:
        if request.COOKIES.get('remember'):
            user_details = SignUp.objects.get(Username=request.COOKIES.get('remember'))
            admission = Admission.objects.filter(Institute_Id=user_details).values_list('Date')
            jan=feb=mar=apr=may=june=july=aug=sept=october=nov=dec= 0
            date = month = year = 0
            now = datetime.now()
            get_date = now.strftime('%d')
            get_month = now.strftime('%m')
            get_year = now.strftime('%Y')
            for i in admission:
                print(i)
                sp = str(i)
                sp1 = sp.split("'")
                var = sp1[1].split('/')
                if var[0] == get_date:
                    date += 1
                if var[1] == get_month:
                    month += 1
                if var[2] == get_year:
                    year += 1
                if var[1] == '01' or var[1] == '1':
                    jan += 1
                elif var[1] == '02' or var[1] == '2':
                    feb += 1
                elif var[1] == '03' or var[1] == '3':
                    mar += 1
                elif var[1] == '04' or var[1] == '4':
                    apr += 1
                elif var[1] == '05' or var[1] == '5':
                    may += 1
                elif var[1] == '06' or var[1] == '6':
                    june += 1
                elif var[1] == '07' or var[1] == '7':
                    july += 1
                elif var[1] == '08' or var[1] == '8':
                    aug += 1
                elif var[1] == '09' or var[1] == '9':
                    sept += 1
                elif var[1] == '10':
                    october += 1
                elif var[1] == '11':
                    nov += 1
                else:
                    dec += 1

            admission=[jan,feb,mar,apr,may,june,july,aug,sept,october,nov,dec,date,month,year]
            receipt = Receipt.objects.filter(Institute_Id=user_details).values_list('Date', 'Amount')
            jan = feb = mar = apr = may = june = july = aug = sept = october = nov = dec = 0
            date = month = year = 0
            for i in receipt:
                sp = str(i)
                sp1 = sp.split("'")
                var = sp1[1].split('/')
                if var[0] == get_date:
                    date += int(i[1])
                if var[1] == get_month:
                    month += int(i[1])
                if var[2] == get_year:
                    year += int(i[1])
                if var[1] == '01' or var[1] == '1':
                    jan += int(i[1])
                elif var[1] == '02' or var[1] == '2':
                    feb += int(i[1])
                elif var[1] == '03' or var[1] == '3':
                    mar += int(i[1])
                elif var[1] == '04' or var[1] == '4':
                    apr += int(i[1])
                elif var[1] == '05' or var[1] == '5':
                    may += int(i[1])
                elif var[1] == '06' or var[1] == '6':
                    june += int(i[1])
                elif var[1] == '07' or var[1] == '7':
                    july += int(i[1])
                elif var[1] == '08' or var[1] == '8':
                    aug += int(i[1])
                elif var[1] == '09' or var[1] == '9':
                    sept += int(i[1])
                elif var[1] == '10':
                    october += int(i[1])
                elif var[1] == '11':
                    nov += int(i[1])
                elif var[1] == '12':
                    dec += int(i[1])
            receipt = [jan, feb, mar, apr, may, june, july, aug, sept, october, nov, dec,date,month,year]
            enquiry = Enquiry.objects.filter(Institute_Id=user_details).values_list('Date')
            jan = feb = mar = apr = may = june = july = aug = sept = october = nov = dec = 0
            date = month = year = 0
            for i in enquiry:
                sp = str(i)
                sp1 = sp.split("'")
                print(sp1[1])
                var = sp1[1].split('/')
                if var[0] == get_date:
                    date += 1
                if var[1] == get_month:
                    month += 1
                if var[2] == get_year:
                    year += 1
                if var[1] == '01' or var[1] == '1':
                    jan += 1
                elif var[1] == '02' or var[1] == '2':
                    feb += 1
                elif var[1] == '03' or var[1] == '3':
                    mar += 1
                elif var[1] == '04' or var[1] == '4':
                    apr += 1
                elif var[1] == '05' or var[1] == '5':
                    may += 1
                elif var[1] == '06' or var[1] == '6':
                    june += 1
                elif var[1] == '07' or var[1] == '7':
                    july += 1
                elif var[1] == '08' or var[1] == '8':
                    aug += 1
                elif var[1] == '09' or var[1] == '9':
                    sept += 1
                elif var[1] == '10':
                    october += 1
                elif var[1] == '11':
                    nov += 1
                else:
                    dec += 1

            enquiry = [jan, feb, mar, apr, may, june, july, aug, sept, october, nov, dec,date,month,year]
            params = {'user_details': user_details, 'admission':admission,'receipt':receipt, 'enquiry':enquiry}
            return render(request, "dashbrd.html", {'params':params})
        elif not request.COOKIES.get('remember'):
            return render(request, "Home.html")

def forgot(request):
    return render(request, "forgot.html")

def courses(request):
    global user_details
    if request.method == "POST" and 'add' in request.POST:
        course_name = request.POST.get('course_name')
        course_name = course_name.upper()
        duration = request.POST.get('duration')
        fee = request.POST.get('fee')
        reg_amt = request.POST.get('reg_amt')
        user_details = SignUp.objects.get(Username=request.COOKIES.get('remember'))
        fetch_courses = Courses.objects.filter(Course_Name=course_name, Institute_Id=user_details)
        if fetch_courses.exists():
            print('Course name already registered ')
            params = {'user_details': user_details}
            return render(request, "courses.html", {'params': params})
        else:
            add_course = Courses(Course_Name=course_name,
                                 Duration=duration,
                                 Fee=fee,
                                 Reg_amt=reg_amt,
                                 Institute_Id=user_details
                                 )
            add_course.save()
            print("Details saved to database")
            user_details = SignUp.objects.get(Username=request.COOKIES.get('remember'))
            table = Courses.objects.filter(Institute_Id=user_details)
            params = {'user_details': user_details,'table': table}
            return render(request, "courses.html",{'params':params})

    elif request.method == "POST" and 'change' in request.POST:
        c_id = request.POST.get('course_id')
        course_name = request.POST.get('course_name')
        course_name = course_name.upper()
        duration = request.POST.get('duration')
        fee = request.POST.get('fee')
        reg_amt = request.POST.get('reg_amt')
        user_details = SignUp.objects.get(Username=request.COOKIES.get('remember'))
        fetch_courses = Courses.objects.get(id=c_id, Institute_Id=user_details)
        fetch_courses.Course_Name=course_name
        fetch_courses.Duration=duration
        fetch_courses.Fee=fee
        fetch_courses.Reg_amt=reg_amt
        fetch_courses.save()
        print("Details updated to database")
        table = Courses.objects.filter(Institute_Id=user_details.id)
        params = {'user_details': user_details, 'table':table}
        return render(request, "courses.html", {'params': params})

    elif request.method == "POST" and 'btn-search' in request.POST:
        get_search = request.POST.get('search')
        table = Courses.objects.filter(Institute_Id=user_details.id, Course_Name=get_search)
        params = {'user_details': user_details, 'table': table}
        return render(request, "courses.html", {'params': params})

    elif request.method == "POST" and 'popup' in request.POST:
        delete = request.POST.get('optradio')
        course_id = request.POST.get('course_id')
        if delete == 'YES':
            del_course = Courses.objects.get(id=course_id)
            del_course.delete()
            print('Deleted Successfully')
            table = Courses.objects.filter(Institute_Id=user_details.id)
            params = {'user_details': user_details, 'table': table}
            return render(request, "courses.html", {'params': params})
        else:
            table = Courses.objects.filter(Institute_Id=user_details.id)
            params = {'user_details': user_details, 'table': table}
            return render(request, "courses.html", {'params': params})

    else:
        table = Courses.objects.filter(Institute_Id=user_details.id)
        params = {'user_details':user_details,'table': table}
        return render(request, "courses.html", {'params':params})

def enquiry(request):
    if request.method == 'POST':
        global user_details
        get_date = request.POST.get('date')
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        reference = request.POST.get('reference')
        enquired_for = request.POST.get('enquired_for')
        user_details = SignUp.objects.get(Username=request.COOKIES.get('remember'))
        save_enq = Enquiry(Date=get_date,
                           Name=name,
                           Address=address,
                           Phone=phone,
                           Reference=reference,
                           Enquired_For=enquired_for,
                           Institute_Id=user_details
                          )
        save_enq.save()
        print('Saved Successfully')
        now = datetime.now()
        date = now.strftime('%d/%m/%Y')
        params = {'user_details': user_details, 'date': date}
        return render(request, "enquiry.html", {'params': params})
    else:
        now = datetime.now()
        date = now.strftime('%d/%m/%Y')
        params = {'user_details': user_details, 'date': date}
        return render(request, "enquiry.html", {'params':params})

def admission(request):
    global user_details
    if request.method == 'POST':
        get_date = request.POST.get('date')
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        f_name = request.POST.get('f_name')
        qual = request.POST.get('qual')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        c_name = request.POST.get('c_name')
        fee = request.POST.get('fee')
        duration = request.POST.get('duration')
        photo = request.FILES['photo']
        identity = request.FILES['identity']
        user_details = SignUp.objects.get(Username=request.COOKIES.get('remember'))
        admit = Admission(Date=get_date,
                           Name=name,
                           F_Name=f_name,
                           Address=address,
                           Phone=phone,
                           Qualification=qual,
                           Gender=gender,
                           DOB=dob,
                           Course_Name=c_name,
                           Fee=fee,
                           Duration=duration,
                           photo=photo,
                           Identity=identity,
                           Institute_Id=user_details
                           )
        admit.save()
        save_photo = FileSystemStorage()
        save_photo.save(name=name, content=photo)

        save_identity = FileSystemStorage()
        save_identity.save(name=identity.name, content=identity)

        params = {'user_details': user_details}
        return render(request, "students.html", {'params': params})
    else:
        now = datetime.now()
        date = now.strftime('%d/%m/%Y')
        params = {'user_details': user_details, 'date': date}
        return render(request, "admission.html", {'params': params})

def students(request):
    global user_details
    if request.method == 'POST' and 'btn-search' in request.POST:
        get_search = request.POST.get('get_search')
        get_search = get_search.upper()
        admission = Admission.objects.filter(Institute_Id=user_details.id, Course_Name=get_search)
        print(len(admission))
        if len(admission) == 0:
            admission = Admission.objects.filter(Institute_Id=user_details.id, Name=get_search)
            print(len(admission))
            if len(admission) == 0:
                admission = Admission.objects.filter(Institute_Id=user_details.id, Date=get_search)
                print(len(admission))
        params = {'user_details': user_details, 'admission': admission}
        return render(request, "students.html", {'params': params})

    else:
        admission = Admission.objects.filter(Institute_Id=user_details)
        receipt = Receipt.objects.filter(Institute_Id=user_details)
        params = {'user_details':user_details, 'admission':admission, 'receipt':receipt}
        return render(request, "students.html", {'params':params})

def forms(request):
    return render(request, "forms.html", {'user_details':user_details})

def receipt(request):
    global user_details
    if request.method == 'POST':
        get_date = request.POST.get('date')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        amount = request.POST.get('amount')
        course = request.POST.get('course')
        user_details = SignUp.objects.get(Username=request.COOKIES.get('remember'))
        fetch_details = Admission.objects.filter(Name=name, Phone=mobile, Institute_Id=user_details)
        if fetch_details.exists():
            save_receipt = Receipt(Date=get_date,
                                   Name=name,
                                   Mobile=mobile,
                                   Amount=amount,
                                   Course=course,
                                   Institute_Id=user_details
                                   )
            save_receipt.save()
            now = datetime.now()
            date = now.strftime('%d/%m/%Y')
            params = {'user_details': user_details, 'date': date}
            return render(request, "receipt.html", {'params': params})
        else:
            print('Wrong details entered')
            now = datetime.now()
            date = now.strftime('%d/%m/%Y')
            params = {'user_details': user_details, 'date': date}
            return render(request, "receipt.html", {'params': params})
    else:
        now = datetime.now()
        date = now.strftime('%d/%m/%Y')
        params = {'user_details': user_details, 'date': date}
        return render(request, "receipt.html", {'params': params})

def Dashboard(request):
    admission = Admission.objects.filter(Institute_Id=user_details).values_list('Date')
    jan = feb = mar = apr = may = june = july = aug = sept = october = nov = dec = 0
    date = month = year = 0
    now = datetime.now()
    get_date = now.strftime('%d')
    get_month = now.strftime('%m')
    get_year = now.strftime('%Y')
    for i in admission:
        sp = str(i)
        sp1 = sp.split("'")
        var = sp1[1].split('/')
        if var[0] == get_date:
            date += 1
        if var[1] == get_month:
            month += 1
        if var[2] == get_year:
            year += 1
        if var[1] == '01' or var[1] == '1':
            jan += 1
        elif var[1] == '02' or var[1] == '2':
            feb += 1
        elif var[1] == '03' or var[1] == '3':
            mar += 1
        elif var[1] == '04' or var[1] == '4':
            apr += 1
        elif var[1] == '05' or var[1] == '5':
            may += 1
        elif var[1] == '06' or var[1] == '6':
            june += 1
        elif var[1] == '07' or var[1] == '7':
            july += 1
        elif var[1] == '08' or var[1] == '8':
            aug += 1
        elif var[1] == '09' or var[1] == '9':
            sept += 1
        elif var[1] == '10':
            october += 1
        elif var[1] == '11':
            nov += 1
        else:
            dec += 1

    admission = [jan, feb, mar, apr, may, june, july, aug, sept, october, nov, dec, date, month, year]
    receipt = Receipt.objects.filter(Institute_Id=user_details).values_list('Date', 'Amount')
    jan = feb = mar = apr = may = june = july = aug = sept = october = nov = dec = 0
    date = month = year = 0
    for i in receipt:
        sp = str(i)
        sp1 = sp.split("'")
        var = sp1[1].split('/')
        if var[0] == get_date:
            date += int(i[1])
        if var[1] == get_month:
            month += int(i[1])
        if var[2] == get_year:
            year += int(i[1])
        if var[1] == '01' or var[1] == '1':
            jan += int(i[1])
        elif var[1] == '02' or var[1] == '2':
            feb += int(i[1])
        elif var[1] == '03' or var[1] == '3':
            mar += int(i[1])
        elif var[1] == '04' or var[1] == '4':
            apr += int(i[1])
        elif var[1] == '05' or var[1] == '5':
            may += int(i[1])
        elif var[1] == '06' or var[1] == '6':
            june += int(i[1])
        elif var[1] == '07' or var[1] == '7':
            july += int(i[1])
        elif var[1] == '08' or var[1] == '8':
            aug += int(i[1])
        elif var[1] == '09' or var[1] == '9':
            sept += int(i[1])
        elif var[1] == '10':
            october += int(i[1])
        elif var[1] == '11':
            nov += int(i[1])
        elif var[1] == '12':
            dec += int(i[1])
    receipt = [jan, feb, mar, apr, may, june, july, aug, sept, october, nov, dec, date, month, year]
    enquiry = Enquiry.objects.filter(Institute_Id=user_details).values_list('Date')
    jan = feb = mar = apr = may = june = july = aug = sept = october = nov = dec = 0
    date = month = year = 0
    for i in enquiry:
        sp = str(i)
        sp1 = sp.split("'")
        print(sp1[1])
        var = sp1[1].split('/')
        if var[0] == get_date:
            date += 1
        if var[1] == get_month:
            month += 1
        if var[2] == get_year:
            year += 1
        if var[1] == '01' or var[1] == '1':
            jan += 1
        elif var[1] == '02' or var[1] == '2':
            feb += 1
        elif var[1] == '03' or var[1] == '3':
            mar += 1
        elif var[1] == '04' or var[1] == '4':
            apr += 1
        elif var[1] == '05' or var[1] == '5':
            may += 1
        elif var[1] == '06' or var[1] == '6':
            june += 1
        elif var[1] == '07' or var[1] == '7':
            july += 1
        elif var[1] == '08' or var[1] == '8':
            aug += 1
        elif var[1] == '09' or var[1] == '9':
            sept += 1
        elif var[1] == '10':
            october += 1
        elif var[1] == '11':
            nov += 1
        else:
            dec += 1

    enquiry = [jan, feb, mar, apr, may, june, july, aug, sept, october, nov, dec, date, month, year]
    params = {'user_details': user_details, 'admission': admission, 'receipt': receipt, 'enquiry': enquiry}
    return render(request, "dashbrd.html", {'params': params})

def rec_book(request):
    global user_details
    if request.method == 'POST':
        get_search = request.POST.get('get_search')
        receipt = Receipt.objects.filter(Institute_Id=user_details, Course=get_search)
        print(len(receipt))
        if len(receipt) == 0:
            receipt = Receipt.objects.filter(Institute_Id=user_details, Name=get_search)
            print(len(receipt))
            if len(receipt) == 0:
                receipt = Receipt.objects.filter(Institute_Id=user_details, Date=get_search)
                print(len(receipt))
        params = {'user_details': user_details, 'receipt': receipt}
        return render(request, "rec_book.html", {'params': params})
    else:
        receipt = Receipt.objects.filter(Institute_Id=user_details)
        params= {'user_details': user_details, 'receipt': receipt}
        return render(request, "rec_book.html", {'params': params})

def enq_book(request):
    if request.method == 'POST':
        get_search = request.POST.get('get_search')
        enquiry = Enquiry.objects.filter(Institute_Id=user_details, Enquired_For=get_search)
        print(len(enquiry))
        if len(enquiry) == 0:
            enquiry = Enquiry.objects.filter(Institute_Id=user_details, Name=get_search)
            print(len(enquiry))
            if len(enquiry) == 0:
                enquiry = Enquiry.objects.filter(Institute_Id=user_details, Date=get_search)
                print(len(enquiry))
        params = {'user_details': user_details, 'enquiry': enquiry}
        return render(request, "enq_book.html", {'params': params})
    else:
        enquiry = Enquiry.objects.filter(Institute_Id=user_details)
        params = {'user_details': user_details, 'enquiry': enquiry}
        return render(request, "enq_book.html", {'params': params})


def logout(request):
    if request.COOKIES.get('remember'):
        response = render(request, "Home.html")
        response.delete_cookie("remember")
    else:
        response = render(request, "Home.html")
    return response


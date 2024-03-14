from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .forms import mail_form
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404


from django.shortcuts import render, redirect
from requests import get
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout


def index(request):
    login_name = get_login_name(request)
    print(login_name)
    bnc_regier_check = check_registration(request)
    context = {"login_name":login_name,"bnc_regier_check":bnc_regier_check}
    return render(request,"index.html",context)

def logout_view(request):
    logout(request)
    return redirect('home')
def service_page(request):
    login_name = get_login_name(request)
    bnc_regier_check = check_registration(request)


    service_data = UserProfile.objects.values('service_name', 'brand_name','register_id',)
    context = {"service_data":service_data,"login_name":login_name,"bnc_regier_check":bnc_regier_check}
    return render(request,"service_page.html",context)
def sign_up_page(request):
    return render(request,"sign_up.html")
def sign_in_page(request):
    return render(request,"sign_in.html")
def meet_our_team(request):
    login_name = get_login_name(request)
    bnc_regier_check = check_registration(request)

    team_members = superior_team.objects.all()
    founder_details = founder.objects.all()
    president_details = president.objects.all()
    vice_details = vice_president.objects.all()
    secretary_details = secretary.objects.all()
    coordinate_team_members = coordinate_team.objects.all()
    renders = {"team_members":team_members,"bnc_regier_check":bnc_regier_check,"founder_detail":founder_details,"president_detail":president_details,"vice_detail":vice_details,"secretary_detail":secretary_details,'coordinate_team':coordinate_team_members,"login_name":login_name}
    return render(request,"meet_our_team.html",renders)
def nav_page(request):

    return render(request,"nav_bar.html")

@login_required
def join_our_team(request):
    login_name = get_login_name(request)
    bnc_regier_check = check_registration(request)


    categories_object = open_cat.objects.all()
    return render(request,"openings.html",{"categories": categories_object,"bnc_regier_check":bnc_regier_check,"login_name":login_name})

@login_required
def send_mail(request):
  
    if request.method == 'POST':
        form = mail_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message_content = form.cleaned_data['message']
            email_address = 'chandrusri247@gmail.com'
            
            mail_process(email_address,name,email,message_content,1)

            mail_process(email_address,name,email,message_content,0)

            
            return render(request,"index.html")

@login_required
def mail_process(email_address,name,email,message_content,check):
    password = 'pxgx utab kfdx pndb'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    message = MIMEMultipart()
   
    if check == 1:
        to_address = 'jenctechnologies@gmail.com'
        message['From'] = email_address   
        message['To'] = 'jenctechnologies@gmail.com'
        message['Subject'] = 'Enquire request'
        message.attach(MIMEText(f"Name : {name}\nEmail : {email}\nMessage : {message_content}", 'plain'))
    else:
        to_address = email
        message['From'] = email_address   
        message['To'] = email
        message['Subject'] = 'BNC'
        message.attach(MIMEText(f"Hi {name}\n\n Our Team Will Be Contact You Soon \n\n Thanks for Visiting",'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_address, password)
    server.sendmail(email_address, to_address, message.as_string())
    server.quit()

def meetings(request):
    login_name = get_login_name(request)
    bnc_regier_check = check_registration(request)

    meeting_data = meeting_assign.objects.all()
    founder_data = founder.objects.all()
    context = {"bnc_regier_check":bnc_regier_check,"meeting_data":meeting_data,'founder_data':founder_data,'login_name':login_name}



    return render(request,"meetings.html",context)
def meeting_details(request):
    
    return render(request, 'meeting-details.html')

def events(request):
    login_name = get_login_name(request)
    bnc_regier_check = check_registration(request)

    event_data = Event.objects.all()
    for i in event_data:
        print(i.event_name)
    context = {"event_details":event_data,"login_name":login_name,"bnc_regier_check":bnc_regier_check}
    return render(request, 'event.html',context)
# def event_gallery(request):
#     return render(request, 'event_gallery.html')
def save_bnc_registration(request):
    login_name = get_login_name(request)
    bnc_regier_check = check_registration(request)

    if request.method == 'POST':
        form = BncRegisterForm(request.POST)
        if form.is_valid():
            print("run")
            form.save()
    else:
        form = BncRegisterForm()

    context = {'form': form,"login_name":login_name,"bnc_regier_check":bnc_regier_check}
    return render(request, 'bnc_register_mem_form.html', context)

def get_next_register_id(request):
    
    print("run")
    # Logic to generate the next available register_id based on existing entries
    base_register_id = "BNC"
    latest_register = UserProfile.objects.filter(register_id__startswith=base_register_id).order_by('-register_id').first()

    if latest_register:
        latest_number = int(latest_register.register_id[len(base_register_id):])
        new_number = latest_number + 1
        next_register_id = f"{base_register_id}{new_number:03d}"
    else:
        next_register_id = f"{base_register_id}001"

    return JsonResponse({'next_register_id': next_register_id})

def upload_index(request):
    text_data = request.GET.get('title')
    images = Image.objects.filter(title=text_data)
    for i in images:
        print(i.pic)
    context = {'images': images}
    return render(request, "event_gallery.html", context)
def fileupload(request):
    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            images = request.FILES.getlist('pic')
            for image in images:
                image_ins = Image(title=title, pic=image)
                image_ins.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = ImagesForm()
    context = {'form': form}
    return render(request, "image_list.html", context)

def service_details(request):
    login_name = get_login_name(request)
    bnc_regier_check = check_registration(request)

    print("run")
    register_id_to_filter = request.GET.get('id_')
    user_profiles = UserProfile.objects.filter(register_id=register_id_to_filter)
    context={"user_profile":user_profiles,"login_name":login_name,"bnc_regier_check":bnc_regier_check}
    return render(request,"service_details.html",context)


@login_required
def user_profile(request):
    login_name = get_login_name(request)
    bnc_regier_check = check_registration(request)

    login_mail = request.user.email
    print(login_mail)
    user_details = UserProfile.objects.filter(email_address=login_mail)
    user_profile = get_object_or_404(UserProfile, email_address=login_mail)
    if request.method == 'POST':
        form = UsereditForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail', user_id=user_profile.id)
        else:
            print(form.errors)

    else:
        form = UsereditForm(instance=user_profile)

    return render(request, 'user_profile.html', {'form': form, "bnc_regier_check":bnc_regier_check,'user_profile': user_profile,"user_details":user_details,"login_name":login_name})

@login_required
def user_form(request):
    login_name = get_login_name(request)
    bnc_regier_check = check_registration(request)
    login_mail = request.user.email
    register_object = bnc_register_mem.objects.values()
    gmail_list = list(register_object.values_list('gmail', flat=True))
    if login_mail in gmail_list:
        pass
    else:
        return  redirect("home")
    user_data = UserProfile.objects.filter(email_address=login_mail)
    if len(user_data) != 0:
        return  redirect("home")
    user_name = login_mail.split("@")[0]
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('home')  # Replace 'success_page' with the URL name for your success page
        else:
            print(form.errors)
    else:
        form = UserProfileForm(initial={"bnc_regier_check":bnc_regier_check,'email_address': login_mail,"username":user_name,"login_name":login_name})
    context = {"form":form}
    return render(request,"user_form.html",context)


def meeting_assignment(request):
    login_name = get_login_name(request)
    bnc_regier_check = check_registration(request)

    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meet')  # Redirect to a page displaying the list of meetings
    else:
        form = MeetingForm()

    return render(request, 'meeting_assign.html', {"bnc_regier_check":bnc_regier_check,'form': form,"login_name":login_name})


def event_assignment(request):
    login_name = get_login_name(request)
    bnc_regier_check = check_registration(request)

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bnc/event')  # Redirect to a page displaying the list of events
    else:
        form = EventForm()

    return render(request, 'meeting_assign.html', {"bnc_regier_check":bnc_regier_check,'form': form,"login_name":login_name})

def get_login_name(request):
    login_name = request.user.username
    if login_name:
        return login_name
    else:
        return None
@login_required
def check_registration(request):
    login_mail = request.user.email
    register_object = bnc_register_mem.objects.values()
    gmail_list = list(register_object.values_list('gmail', flat=True))
    if login_mail in gmail_list:
        return True
    else:
        return False

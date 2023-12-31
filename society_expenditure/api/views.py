from django.contrib.auth import get_user_model,logout
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .models import Exp , Content
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
from django.db import connection

def homepage(request):
    if request.user.is_authenticated:
        try:
            user_profile = Exp.objects.get(username=request.user)
            return render(request,'homepage.html',{'user_profile':user_profile})
        except Exp.DoesNotExist:
            pass
    else:
        return render(request, 'homepage.html')
    
def welcome_page(request):
    return render(request, 'welcome.html')

def login_views(request):
    if request.method == 'POST':
        username = request.POST.get('login-username')
        password = request.POST.get('login-password')
        print(username)
        print(password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(homepage)
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect(login_views)
    return render(request, 'login.html')

def signup_views(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email_id = request.POST.get('email')
        user_name = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm-password')
        security_question = request.POST.get('security_question')
        security_answer = request.POST.get('answer')

        if password1 != password2:
            error_message = "Passwords do not match. Please try again."
            return render(request, 'signup.html', {'error_message': error_message})
        if Exp.objects.filter(username=user_name).exists():
            messages.info(request, 'Username is already taken')
        elif Exp.objects.filter(email=email_id).exists():
            messages.info(request, 'Email is already taken')
            return redirect(signup_views)
        else:
            new_user = Exp.objects.create(
                username = user_name,
                email = email_id,
                password = password1,
                user_name = name,
                securityquestion = security_question,
                securityanswer = security_answer,
            )
            new_user.set_password(new_user.password)
            new_user.save()
            print(new_user.securityquestion)
            print(new_user.securityanswer)
            return redirect(login_views)
    
    return render(request,'signup.html')

# def getpassword(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         security_question = request.POST.get('security_question')
#         security_answer = request.POST.get('security_answer')
#         print(security_question)
#         print(security_answer)
#         user = auth.authenticate(user_name = username, securityquestion = security_question , securityanswer = security_answer)
#         if user is not None:
#             original_password = user.password
#             print(original_password)
#             return render(request, 'getpassword.html', {'password': original_password})
#         else:
#             messages.error(request, 'Invalid Security question or answer')
#             return redirect(getpassword)
    
#     return render(request, 'getpassword.html')

def fats(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        event = request.POST.get('event')
        date = request.POST.get('date')
        total_amount = float(request.POST.get('totalAmount'))
        total_spent = float(request.POST.get('totalSpent'))
        current_balance = total_amount-total_spent
        print(name)
        print(event)
        print(date)
        print(total_amount)
        try:
            user_profile = Exp.objects.get(username=request.user)
            Content.objects.create(user=user_profile,name=name,event=event, Date=date, Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)

        except Exp.DoesNotExist:
            exp_instance = Exp.objects.create(user_name=name)
            Content.objects.create(user=exp_instance,name=name, event=event, Date=date,Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)
        return redirect(homepage)

    return render(request, 'fats.html')

def fatdetail(request):
   

    post = Content.objects.raw("SELECT * FROM api_content WHERE name='option1'")
    #post = Content.objects.filter(name = 'FATS')
    # context = {
    #     # 'all_exp_instances' : all_exp_instances,
    #     # 'all_content_instances' : all_content_instances,
    #     # 'show_data_condition': show_data_condition,
    #     'results':post
    # }
    print(post)
    


    return render(request, 'fat_detail.html', {'data': post})

def cult(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        event = request.POST.get('event')
        date = request.POST.get('date')
        total_amount = float(request.POST.get('totalAmount'))
        total_spent = float(request.POST.get('totalSpent'))
        current_balance = total_amount-total_spent
        print(name)
        try:
            user_profile = Exp.objects.get(username=request.user)
            Content.objects.create(user=user_profile,name=name,event=event, Date=date, Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)

        except Exp.DoesNotExist:
            exp_instance = Exp.objects.create(user_name=name)
            Content.objects.create(user=exp_instance,name=name, event=event, Date=date,Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)
        return redirect(homepage)

    return render(request, 'cult.html')

def cultdetail(request):
   
    # if show_data_condition:
    #     query = """
    #             SELECT * FROM api_content WHERE name='FATS';
    #         """
    #     with connection.cursor() as cursor:
    #         cursor.execute(query)
    #         results = cursor.fetchall()
    # else:
    #     results = []

    post = Content.objects.raw("SELECT * FROM api_content WHERE name='option2'")
    #post = Content.objects.filter(name='option2').first()
    # context = {
    #     # 'all_exp_instances' : all_exp_instances,
    #     # 'all_content_instances' : all_content_instances,
    #     # 'show_data_condition': show_data_condition,
    #     'results':post
    # }

    


    return render(request, 'cult_detail.html', {'data': post})


def paracosm(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        event = request.POST.get('event')
        date = request.POST.get('date')
        total_amount = float(request.POST.get('totalAmount'))
        total_spent = float(request.POST.get('totalSpent'))
        current_balance = total_amount-total_spent
        try:
            user_profile = Exp.objects.get(username=request.user)
            Content.objects.create(user=user_profile,name=name, event=event, Date=date, Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)

        except Exp.DoesNotExist:
            exp_instance = Exp.objects.create(user_name=name)
            Content.objects.create(user=exp_instance,name=name, event=event, Date=date,Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)
        return redirect(homepage)

    return render(request, 'paracosm.html')

def paracosmdetail(request):
   
    # if show_data_condition:
    #     query = """
    #             SELECT * FROM api_content WHERE name='FATS';
    #         """
    #     with connection.cursor() as cursor:
    #         cursor.execute(query)
    #         results = cursor.fetchall()
    # else:
    #     results = []

    post1 = Content.objects.raw("SELECT * FROM api_content WHERE name='option3'")
    # context = {
    #     # 'all_exp_instances' : all_exp_instances,
    #     # 'all_content_instances' : all_content_instances,
    #     # 'show_data_condition': show_data_condition,
    #     'results':post
    # }

    


    return render(request, 'paracosm_detail.html', {'data1': post1})


def photogeeks(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        event = request.POST.get('event')
        date = request.POST.get('date')
        total_amount = float(request.POST.get('totalAmount'))
        total_spent = float(request.POST.get('totalSpent'))
        current_balance = total_amount-total_spent
        try:
            user_profile = Exp.objects.get(username=request.user)
            Content.objects.create(user=user_profile,name=name, event=event, Date=date, Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)

        except Exp.DoesNotExist:
            exp_instance = Exp.objects.create(user_name=name)
            Content.objects.create(user=exp_instance,name=name, event=event, Date=date,Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)
        return redirect(homepage)

    return render(request, 'photogeeks.html')

def photogeeksdetail(request):
   
        # Handle the case where no Exp instance with user_name="FATS" is found
    # if show_data_condition:
    #     query = """
    #             SELECT * FROM api_content WHERE name='FATS';
    #         """
    #     with connection.cursor() as cursor:
    #         cursor.execute(query)
    #         results = cursor.fetchall()
    # else:
    #     results = []

    post = Content.objects.raw("SELECT * FROM api_content WHERE name='option4'")
    # context = {
    #     # 'all_exp_instances' : all_exp_instances,
    #     # 'all_content_instances' : all_content_instances,
    #     # 'show_data_condition': show_data_condition,
    #     'results':post
    # }

    


    return render(request, 'photogeeks_detail.html', {'data': post})

def tech(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        event = request.POST.get('event')
        date = request.POST.get('date')
        total_amount = float(request.POST.get('totalAmount'))
        total_spent = float(request.POST.get('totalSpent'))
        current_balance = total_amount-total_spent
        print(name)
        try:
            user_profile = Exp.objects.get(username=request.user)
            Content.objects.create(user=user_profile,name = name,event=event, Date=date, Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)

        except Exp.DoesNotExist:
            exp_instance = Exp.objects.create(user_name=name)
            Content.objects.create(user=exp_instance,name = name, event=event, Date=date,Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)
        return redirect(homepage)

    return render(request, 'tech.html')

def techdetail(request):
   
    # if show_data_condition:
    #     query = """
    #             SELECT * FROM api_content WHERE name='FATS';
    #         """
    #     with connection.cursor() as cursor:
    #         cursor.execute(query)
    #         results = cursor.fetchall()
    # else:
    #     results = []

    post = Content.objects.raw("SELECT * FROM api_content WHERE name='option5'")
    # context = {
    #     # 'all_exp_instances' : all_exp_instances,
    #     # 'all_content_instances' : all_content_instances,
    #     # 'show_data_condition': show_data_condition,
    #     'results':post
    # }

    


    return render(request, 'tech_detail.html', {'data': post})


def vedant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        event = request.POST.get('event')
        date = request.POST.get('date')
        total_amount = float(request.POST.get('totalAmount'))
        total_spent = float(request.POST.get('totalSpent'))
        current_balance = total_amount-total_spent
        try:
            user_profile = Exp.objects.get(username=request.user)
            Content.objects.create(user=user_profile,name=name, event=event, Date=date, Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)

        except Exp.DoesNotExist:
            exp_instance = Exp.objects.create(user_name=name)
            Content.objects.create(user=exp_instance,name=name, event=event, Date=date,Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)
        return redirect(homepage)

    return render(request, 'vedant.html')

def vedantdetail(request):
   
    # if show_data_condition:
    #     query = """
    #             SELECT * FROM api_content WHERE name='FATS';
    #         """
    #     with connection.cursor() as cursor:
    #         cursor.execute(query)
    #         results = cursor.fetchall()
    # else:
    #     results = []

    post = Content.objects.raw("SELECT * FROM api_content WHERE name='option6'")
    # context = {
    #     # 'all_exp_instances' : all_exp_instances,
    #     # 'all_content_instances' : all_content_instances,
    #     # 'show_data_condition': show_data_condition,
    #     'results':post
    # }

    


    return render(request, 'vedant_detail.html', {'data': post})


def megaheartz(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        event = request.POST.get('event')
        date = request.POST.get('date')
        total_amount = float(request.POST.get('totalAmount'))
        total_spent = float(request.POST.get('totalSpent'))
        current_balance = total_amount-total_spent
        try:
            user_profile = Exp.objects.get(username=request.user)
            Content.objects.create(user=user_profile,name=name, event=event, Date=date, Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)

        except Exp.DoesNotExist:
            exp_instance = Exp.objects.create(user_name=name)
            Content.objects.create(user=exp_instance,name=name, event=event, Date=date,Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)
        return redirect(homepage)

    return render(request, 'megaheartz.html')

def megaheartzdetail(request):

    # if show_data_condition:
    #     query = """
    #             SELECT * FROM api_content WHERE name='FATS';
    #         """
    #     with connection.cursor() as cursor:
    #         cursor.execute(query)
    #         results = cursor.fetchall()
    # else:
    #     results = []

    post = Content.objects.raw("SELECT * FROM api_content WHERE name='option7'")
    # context = {
    #     # 'all_exp_instances' : all_exp_instances,
    #     # 'all_content_instances' : all_content_instances,
    #     # 'show_data_condition': show_data_condition,
    #     'results':post
    # }

    


    return render(request, 'megaheartz_detail.html', {'data': post})


def tars(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        event = request.POST.get('event')
        date = request.POST.get('date')
        total_amount = float(request.POST.get('totalAmount'))
        total_spent = float(request.POST.get('totalSpent'))
        current_balance = total_amount-total_spent
        try:
            user_profile = Exp.objects.get(username=request.user)
            Content.objects.create(user=user_profile,name=name, event=event, Date=date, Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)

        except Exp.DoesNotExist:
            exp_instance = Exp.objects.create(user_name=name)
            Content.objects.create(user=exp_instance,name=name, event=event, Date=date,Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)
        return redirect(homepage)

    return render(request, 'tars.html')

def tarsdetail(request):
   
    # if show_data_condition:
    #     query = """
    #             SELECT * FROM api_content WHERE name='FATS';
    #         """
    #     with connection.cursor() as cursor:
    #         cursor.execute(query)
    #         results = cursor.fetchall()
    # else:
    #     results = []

    post = Content.objects.raw("SELECT * FROM api_content WHERE name='option8'")
    # context = {
    #     # 'all_exp_instances' : all_exp_instances,
    #     # 'all_content_instances' : all_content_instances,
    #     # 'show_data_condition': show_data_condition,
    #     'results':post
    # }

    


    return render(request, 'tars_detail.html', {'data': post})


def ecell(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        event = request.POST.get('event')
        date = request.POST.get('date')
        total_amount = float(request.POST.get('totalAmount'))
        total_spent = float(request.POST.get('totalSpent'))
        current_balance = total_amount-total_spent
        try:
            user_profile = Exp.objects.get(username=request.user)
            Content.objects.create(user=user_profile,name=name, event=event, Date=date, Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)

        except Exp.DoesNotExist:
            exp_instance = Exp.objects.create(user_name=name)
            Content.objects.create(user=exp_instance,name=name, event=event, Date=date,Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)
        return redirect(homepage)

    return render(request, 'ecell.html')

def ecelldetail(request):
   
    # if show_data_condition:
    #     query = """
    #             SELECT * FROM api_content WHERE name='FATS';
    #         """
    #     with connection.cursor() as cursor:
    #         cursor.execute(query)
    #         results = cursor.fetchall()
    # else:
    #     results = []

    post = Content.objects.raw("SELECT * FROM api_content WHERE name='option9'")
    # context = {
    #     # 'all_exp_instances' : all_exp_instances,
    #     # 'all_content_instances' : all_content_instances,
    #     # 'show_data_condition': show_data_condition,
    #     'results':post
    # }

    


    return render(request, 'ecell_detail.html', {'data': post})


def sports(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        event = request.POST.get('event')
        date = request.POST.get('date')
        total_amount = float(request.POST.get('totalAmount'))
        total_spent = float(request.POST.get('totalSpent'))
        current_balance = total_amount-total_spent
        try:
            user_profile = Exp.objects.get(username=request.user)
            Content.objects.create(user=user_profile,name=name, event=event, Date=date, Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)

        except Exp.DoesNotExist:
            exp_instance = Exp.objects.create(user_name=name)
            Content.objects.create(user=exp_instance,name=name, event=event, Date=date,Total_Amount=total_amount, Total_Spent=total_spent, Current_Balance = current_balance)
        return redirect(homepage)

    return render(request, 'sports.html')

def sportsdetail(request):

    # if show_data_condition:
    #     query = """
    #             SELECT * FROM api_content WHERE name='FATS';
    #         """
    #     with connection.cursor() as cursor:
    #         cursor.execute(query)
    #         results = cursor.fetchall()
    # else:
    #     results = []

    post = Content.objects.raw("SELECT * FROM api_content WHERE name='option10'")
    # context = {
    #     # 'all_exp_instances' : all_exp_instances,
    #     # 'all_content_instances' : all_content_instances,
    #     # 'show_data_condition': show_data_condition,
    #     'results':post
    # }

    


    return render(request, 'sports_detail.html', {'data': post})

def logout_view(request):
    if request.method == 'POST':
            logout(request)
            return redirect('welcome_page')



from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
from .models import Donation



# Create your views here.

def indexView (request):
	return render(request,'index.html')



def homeView (request):

	return render(request,'home.html')



def loginView (request):

    
#def login(request):
    if request.method == 'POST':
        lg_username = request.POST['lg_username']
        lg_password = request.POST['lg_password']

        user = auth.authenticate(username=lg_username, password=lg_password)
        
        if user is not None:
            auth.login(request, user)
            return redirect("base.html")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login.html')
    else:
        return render(request, 'login.html')

	


def contactView (request):
   
    if request.method == "POST":
        name = request.POST['name']
        email_address = request.POST['email_address']
        phone_number = request.POST['phone_number']
        messages = request.POST['message']

        #send an email
        #send_email(
        #   name,
        #   message, 
        #    email,    
        #    ['farzana.toma@northsouth.edu'],
        #    phone_number,
        #    )

        return render(request, 'contact.html', {'name': name})

    else:
        return render(request, 'contact.html', {})
	



def aboutView (request):
	return render(request,'about.html')


def specialservicesView (request):
 
	return render(request,'specialservices.html')


def PaymentGatewayView (request):
	if request.method=='POST':
		name=request.POST.get('name')
		email=request.POST.get('email')
		amount=request.POST.get('amount')
		Payment=PaymentGateway(name=name,email=email,amount=amount)
		Payment.save()
	return render(request,'PaymentGateway.html')


def DonorDetailsView (request):
  
	return render(request,'DonorDetails.html')



def DonorRegistrationView (request):
    if request.method == 'POST':
        dreg_first_name = request.POST['dreg_first_name']
        dreg_last_name  = request.POST['dreg_last_name']
        dreg_email = request.POST['dreg_email']
        dreg_password = request.POST['dreg_password']
        dreg_password = request.POST['dreg_password']
        dreg_date_of_birth = request.POST['dreg_date_of_birth']
        dreg_phone_number  = request.POST['dreg_phone_number ']
        

        if dreg_password==dreg_password:
            if User.objects.filter(email=dreg_email).exists():
                messages.info(request, 'Email Taken')
                return redirect('base.html')
            elif User.objects.filter(first_name=dreg_first_name).exists():
                messages.info(request, 'Fist Name Taken')
                return redirect('base.html')
            else:
                user = User.objects.create_user( email=dreg_email, first_name=dreg_first_name, password=dreg_password)
                user.save()
                print('user created')
    
        else:
            messages.info(request, 'Password not matching')
            return redirect('DonorRegistration.html')
        #return redirect('base.html')

    else:
        return render(request, 'DonorRegistration.html')





def search_result(request):

    user_list = Donation.objects.all().order_by('-age')
    context = {'users': user_list}

    if request.method == 'GET':
        keyword = request.GET.get('bloodgroup')
        search_filter = Donation.objects.filter(bloodgroup=keyword)
        context['results'] = search_filter
        context['keyword'] = keyword

    return render(request, 'search_result.html', context)





def registerView(request):

    if request.method == 'POST':
        reg_first_name = request.POST['reg_first_name']
        reg_last_name = request.POST['reg_last_name']
        reg_email = request.POST['reg_email']
        reg_password = request.POST['reg_password']
        reg_confirm_pass = request.POST['reg_confirm_pass']
        

        if reg_password==reg_confirm_pass:
            if User.objects.filter(email=reg_email).exists():
                messages.info(request, 'Email Taken')
                return redirect('base.html')
            elif User.objects.filter(first_name=reg_first_name).exists():
                messages.info(request, 'Fist Name Taken')
                return redirect('base.html')
            else:
                user = User.objects.create_user( email=reg_email, first_name=reg_first_name, password=reg_confirm_pass)
                user.save()
                print('user created')
    
        else:
            messages.info(request, 'Password not matching')
            return redirect('register.html')
        #return redirect('base.html')

    else:
        return render(request, 'register.html')

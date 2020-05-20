from django.shortcuts import render,redirect
# from django.contrib.auth import login, authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Account
from amacademy.settings import EMAIL_HOST_USER
from django.http import HttpResponse,FileResponse,Http404,HttpResponseRedirect
import random
import string
from django.core.mail import send_mail

# Create your views here.

def register(request):
	if request.method == 'POST':
		name = request.POST['name'] 
		email = request.POST['email'] 
		phno = request.POST['phno'] 
		password = request.POST['pass'] 
		re_pass = request.POST['re_pass'] 
		country = request.POST['country'] 
		city = request.POST['city']
		if password == re_pass:
			if Account.objects.filter(email=email).exists():
				print(Account.objects.filter(username=email).exists())
				messages.info(request,'Email Already Registered')
				return redirect('register.html')
			else:
				user = Account.objects.create_user(email = email,username= name ,phno = phno,country=country,city=city ,password=password)
				# extenduser(country=country,city=city,phno=phno,user=user)
				user.save()
				print('user created')
				return redirect('/')
		else:
			messages.info(request,'Passwords do not Match')
			return redirect('register.html',)

	else:
		return render(request,'register.html') 


def login(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['pass']
		user = auth.authenticate(email=email,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		
		else:
			messages.info(request,'Invalid Password')
			return redirect('login.html')

	else:
		return render(request,'login.html')

def forgetpass(request):
	try:
		if not 'otp_verify_dict' in globals():
			global otp_verify_dict
			otp_verify_dict={}
		if request.method=='POST':
			email=request.POST['email']
			if Account.objects.filter(email=email).exists:
				otp=random.randint(1000,9999)
				subject="Trouble Signing In to your AmAcademy Account?"
				msg="Hi "+email+",\nYou indicated that you are having a trouble signing in to your AmAcademy Account.\nYour OTP for Password Change is '"+str(otp)+"'.\nIn case you have not changed report it to our Team."
				print(msg)
				recepient=email
				send_mail(subject,msg,EMAIL_HOST_USER,[recepient],fail_silently=False)
				otp_verify_dict[recepient]=otp
				messages.info(request,"Email has been sent")
				return render(request,"OTPverification.html",{'recepient':recepient,'otp':otp})
			else:
				messages.info(request,"Email Does Not Exists!")
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		else:
			return render(request,'forgetpass.html')
	except:
		messages.info(request,"Problem in sending Email ! Please Try again Later.")
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def otpverify(request):
	try:
		if request.method=='POST':
			userotp=request.POST['otp']
			recepient=request.POST.get('recepient')
			# print("userotp=",userotp)
			if len(userotp)>=4:
				# print("recepient=",recepient)
				# print("otp",otp)
				if int(userotp)==otp:
					paswd_character=string.ascii_letters+string.digits+string.punctuation
					generated_pass=''.join(random.choice(paswd_character) for i in range(8))
					print(generated_pass)
					subject="Trouble Signing In to your AmAcademy Account?"
					message="Hi "+recepient+",\nYou indicated that you are having a trouble signing in to your AmAcademy Account.\nYour Password Has been reset to '"+generated_pass+"'\nPlease try Signing in using this credentials."
					recepient=recepient
					# print(recepient)
					send_mail(subject,message,EMAIL_HOST_USER,[recepient],fail_silently=False)
					del otp_verify_dict[recepient]
					messages.info(request,"Email has been Sent !")
					u=Account.objects.get(email=recepient)
					u.set_password(generated_pass)
					u.save()
					return render(request,'login.html')
			else:
				messages.info(request,"Invalid OTP")
				return redirect('/')
	except:
		messages.info(request,"Error in Sending Email.\nPlease try again Later.")
		return redirect('/')
		
	
def registeradmin(request):
	if request.method == 'POST':
		name = request.POST['name'] 
		email = request.POST['admin_email'] 
		phno = request.POST['admin_phno'] 
		password = request.POST['admin_pass'] 
		re_pass = request.POST['admin_re_pass'] 
		country = request.POST['admin_country'] 
		city = request.POST['admin_city']
		if password == re_pass:
			if Account.objects.filter(email=email).exists():
				messages.info(request,'Email Already Registered')
				return redirect('registeradmin.html')
			else:
				user = Account.objects.create_superuser(email = email,username= name ,phno = phno,country=country,city=city ,password=password)
				user.save()
				print('user created')
				return redirect('/')
		else:
			messages.info(request,'Passwords do not Match')
			return redirect('accounts/registeradmin.html')

	else:
		return render(request,'registeradmin.html') 
	# return render(request,'registeradmin.html')

def adminlogin(request):
	return render(request,'AdminLogin.html')

def changepass(request):
	try:
		if request.method=='POST':
			if request.user.is_authenticated:
				session=request.user.email
				pass1=request.POST['pass1']
				pass2=request.POST['pass2']
				if pass1==pass2:
					u=Account.objects.get(email=session)
					u.set_password(pass1)
					u.save()
					auth.login(request,auth.authenticate(email=session,password=pass1))
					messages.info(request,"Successfully Changed Your Password")
				else:
					messages.info(request,"Passwords Do not Match!!!")
				return redirect('/')
				# return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		else:
			return render(request,'ChangePassword.html')

	except:
		messages.info(request,"Exception Occured")

# def forgotadminpass(request):
#     return render(request,'ForgotAdminPass.html')

def logout(request):
	auth.logout(request)
	return redirect('/')


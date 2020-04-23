from django.shortcuts import render,redirect
from django.http import HttpResponse,FileResponse,Http404,HttpResponseRedirect
from .models import book,contactus
import os
from django.contrib import messages
# from django.contrib.auth.models import User
from django.conf import settings

# Create your views here.

def index(request):
	return render(request,'index.html')
	# return HttpResponse("index.html")

# def login(request):
#     return render(request,'login.html')

def contact(request):
	if request.method=='POST':
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']
		doubt = contactus(name=name,email=email,doubt=message)
		doubt.save()
		return redirect('contact.html')
	else:
		return render(request,'contact.html')

def about(request):
	return render(request,'about.html')

# def adminlogin(request):
#     return render(request,'AdminLogin.html')

def doubts(request):
	if request.method=='POST':
		doubt=contactus.objects.all()
		# return redirect('doubts.html')
		return render(request,'doubts.html',{'doubts': doubt})
	else:
		return render(request,'doubts.html')

# def changepass(request):
#     return render(request,'ChangePassword.html')

# def forgetpass(request):
#     return render(request,'forgetpass.html')

# def register(request):
#     return render(request,'register.html')

# def registeradmin(request):
#     return render(request,'registeradmin.html')

# def forgotadminpass(request):
#     return render(request,'ForgotAdminPass.html')

def specificfile(request,course_name):
	if request.method == 'POST' and len(request.FILES)!=0:
		fileupload = request.FILES['fileUpload']
		fileupload.name= fileupload.name.replace(" ","_")
		path=os.path.join(settings.MEDIA_ROOT,"uploads",fileupload.name)
		# print(path)
		if book.objects.filter(filename=fileupload.name) or os.path.exists(path):
			messages.info(request,"Filename Already Exist")
			return redirect('/specificfile.html/{}'.format(course_name))
		else:
			# path=os.path.join(settings.MEDIA_ROOT,"uploads",fileupload.name)
			# fileupload.name= fileupload.name.replace(" ","_")
			uploadbook=book(filename=fileupload.name,course=course_name,uploadpath=fileupload,filesize=fileupload.size)
			uploadbook.save()
			messages.info(request,"File Uploaded Successfully")
			return redirect('/specificfile.html/{}'.format(course_name))
	else:
		if course_name=='all':
			search=request.GET['search']
			files=book.objects.filter(filename__icontains=search)
			# print(files)
		else:
			files=book.objects.filter(course=course_name)
		return render(request,'specificfile.html',{'course_name':course_name,'files':files})
# @login_required
def pdf_view(request,filename):
	try:
		if request.user.is_authenticated:
			# print(filename)
			search=book.objects.filter(filename=filename)
			# print("search=",search)
			path=os.path.join(settings.MEDIA_ROOT,search.values('uploadpath')[0]['uploadpath'])
			# print("path="+path)
			# response=open(path,'rb').read()
			# response= FileResponse(open(path,'rb'),content_type='application/pdf')
			# response= HttpResponse(open(path,'rb').read(),mimetype='application/pdf')
			# response["Content-Disposition"] = 'filename='+filename
			# response.closed
			# print(response)
			# return response
			return FileResponse(open(path,'rb'),content_type='application/pdf')
		else:
			return render(request,'login.html')
	except:
		messages.info(request,"File Not Found")
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		# raise Http404()
	
def download(request,filename):
	print(filename)
	try:
		search=book.objects.filter(filename=filename)
		path=os.path.join(settings.MEDIA_ROOT,search.values('uploadpath')[0]['uploadpath'])
		
		# response= FileResponse(open(path,'rb'),content_type='application/force-download')
		# response=HttpResponse(mimetype='application/force-download')
		# response['Content-Disposition']='attachment; filename=%s' %filename
		# response['X-Sendfile']=smart__str(path)
		# return HttpResponse(response,"application/force-download")
		if os.path.exists(path):
			return FileResponse(open(path,'rb'),content_type='application/force-download')
		else:
			messages.info(request,"File Does Not Exists")
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
			# return HttpResponse("<alert>File Does Not Exist</alert>")
	except:
		messages.info(request,"File Not Found")
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		# raise Http404()

def delete(request,filename):
	try:
		if request.user.is_authenticated and request.user.is_admin:
			
			search=book.objects.filter(filename=filename)
			uploadpath=search.values('uploadpath')[0]['uploadpath']
			print(search.values('uploadpath'))
			path=os.path.join(settings.MEDIA_ROOT,uploadpath)
			print(uploadpath)
			if os.path.exists(path):
				books=book.objects.get(filename=filename,uploadpath=uploadpath)
				# print(books)
				os.remove(path)
				books.delete()
				# print("admin")
				messages.info(request,"File deleted")
				# return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
			else:
				messages.info(request,"File Not Found")
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		else:
			return render(request,'login.html')
	except:
		messages.info(request,"File Not Found exception")
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



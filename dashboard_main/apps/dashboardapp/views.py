from django.shortcuts import render, HttpResponse, redirect
from .models import Users, UserManager, Messages, Comments
from django.core.urlresolvers import reverse

def index(request):
	return render(request,'dashboardapp/index.html')
def signin(request):
	return render(request, 'dashboardapp/signin.html')
def login(request):
	email = request.POST['email']
	password = request.POST['password']
	errors = Users.userManager.loginValidation(email, password)
	if len(errors) == 0:
		user = Users.objects.get(email=email)
		request.session['id'] = user.id
		return redirect(reverse('dashboard_dashboard'))
	else:
		context={
			"errors": errors
		}
		return render(request, 'dashboardapp/signin.html', context)
def register(request):
	return render(request, 'dashboardapp/register.html')
def create(request):
	first_name=request.POST['first_name']
	last_name=request.POST['last_name']
	email=request.POST['email']
	password=request.POST['password']
	confirm_password=request.POST['confirm_password']
	errors = Users.userManager.getErrors(first_name, last_name, email, password, confirm_password)
	if len(errors) == 0:
		encryptedPassword = Users.userManager.encrypt(password)
		if len(Users.objects.all()) == 0:
			Users.objects.create(first_name=first_name, last_name=last_name, email=email, password=encryptedPassword, user_level=9)
		else:
			Users.objects.create(first_name=first_name, last_name=last_name, email=email, password=encryptedPassword, user_level=1)
		errors.append("Succesfully Registered!")
		context = {
			'errors': errors,
			'users': Users.objects.all()
		}
		return render(request, request.POST['redirect_success'], context)
	else:
		context = {
			'errors': errors
		}
		return render(request, request.POST['redirect_fail'], context)
def dashboard(request):
	user = Users.objects.get(id=request.session['id'])
	context = {
		"users": Users.objects.all()
	}
	if user.user_level == 9:
		return render(request, 'dashboardapp/dashboard_admin.html', context)
	else:
		return render(request, 'dashboardapp/dashboard.html', context)
def new(request):
	return render(request, 'dashboardapp/addnew.html')
def edit(request, id):
	user = Users.objects.get(id=id)
	context = {
		"user": user
	}
	return render(request, 'dashboardapp/edit.html', context)
def destroy(request, id):
	user = Users.objects.get(id=id)
	user.delete()
	return redirect(reverse('dashboard_dashboard'))
def update(request, id):
	user = Users.objects.get(id=id)
	content = request.POST['content']
	if content == "password":
		password = request.POST['password']
		encryptedPassword = Users.userManager.encrypt(password)
		user.password = encryptedPassword
	elif content == "userinfo":
		user.email = request.POST['email']
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		if request.POST['editor'] == "admin":
			user.user_level = request.POST['user_level']
	else:
		user.description = request.POST['description']
	user.save()
	return redirect(reverse('dashboard_dashboard'))
def show(request, id):
	user = Users.objects.get(id=id)
	context = {
		"user": user,
		"messages": Messages.objects.all(),
		"comments": Comments.objects.all()
	}
	return render(request, 'dashboardapp/show.html', context)
def post(request, id):
	content = request.POST['message']
	user = Users.objects.get(id=request.session['id'])
	author = user.first_name + " " + user.last_name
	user = Users.objects.get(id=id)
	Messages.objects.create(content=content, author=author, user=user)
	context = {
		"user": user,
		"messages": Messages.objects.all(),
		"comments": Comments.objects.all()
	}
	return render(request, 'dashboardapp/show.html', context)
def reply(request, id):
	content = request.POST['comment']
	user = Users.objects.get(id=request.session['id'])
	author = user.first_name + " " + user.last_name
	messageid = request.POST['messageid']
	message = Messages.objects.get(id=messageid)
	Comments.objects.create(content=content, author=author, message=message)
	user = Users.objects.get(id=id)
	context = {
		"user": user,
		"messages": Messages.objects.all(),
		"comments": Comments.objects.all()
	}
	return render(request, 'dashboardapp/show.html', context)
def profile(request):
	context = {
		"user": Users.objects.get(id=request.session['id'])
	}
	return render(request, 'dashboardapp/profile.html', context)
def logoff(request):
	request.session.pop('id')
	return redirect(reverse('dashboard_signin'))

















from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
	def loginValidation(self, email, password):
		errors = []
		if len(Users.objects.filter(email=email)) == 0:
			errors.append("Email does not exist in database")
		else:
			user = Users.objects.get(email=email)
			hashed = user.password
			password = password.encode('utf-8')
			hashed = hashed.encode('utf-8')
			if not bcrypt.hashpw(password, hashed) == hashed:
				errors.append("Invalid Password")
		return errors


		return len(Users.objects.filter(email=email)) > 0
	def getErrors(self, first_name, last_name, email, password, confirm_password):
		errors = []
		if len(first_name) < 2 or len(last_name) < 2 or not first_name.isalpha() or not last_name.isalpha():
			errors.append("Name is not valid (needs to be more than 2 characters and only alpha characters)")
		if not EMAIL_REGEX.match(email):
			errors.append("Email is not a valid email")
		if len(password) < 8:
			errors.append("Password is too short")
		if not password == confirm_password:
			errors.append("Passwords must match")
		if len(Users.objects.filter(email=email)) > 0:
			errors.append("Email already exists in our database")
		return errors
	def encrypt(self, password):
		password = password.encode('utf-8')
		return bcrypt.hashpw(password, bcrypt.gensalt()) 
	def validPassword(self, password, hashed):
		password = password.encode('utf-8')
		hashed = hashed.encode('utf-8')
		if bcrypt.hashpw(password, hashed) == hashed:
			return True
		else:
			return False

class Users(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	user_level = models.IntegerField()
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	userManager = UserManager()
	objects = models.Manager()

class Messages(models.Model):
	content = models.TextField()
	author = models.CharField(max_length=255)
	user = models.ForeignKey(Users)
	created_at = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
	content = models.TextField()
	author = models.CharField(max_length=255)
	message = models.ForeignKey(Messages)
	created_at = models.DateTimeField(auto_now_add=True)


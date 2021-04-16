from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.dispatch import receiver


# Create your models here.
class manageAkunAdmin(BaseUserManager):
	def create_user(self, username, password):
		if not username:
			raise ValueError("Users must have an Username")

		user = self.model(username=username)

		user.set_password(password)
		user.is_admin 		= True
		user.save(using=self._db)
		return user

	def create_superuser(self, username, password):
		user = self.create_user(username=username, password=password)
		user.is_admin 		= True
		user.is_staff 		= True
		user.is_superuser	= True
		user.save(using=self._db)
		return user

class Account(AbstractBaseUser):
	username		= models.CharField(max_length=30, unique=True)
	last_login		= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin		= models.BooleanField(default=True)
	is_active		= models.BooleanField(default=True)
	is_staff		= models.BooleanField(default=False)
	is_superuser	= models.BooleanField(default=False)

	USERNAME_FIELD	= 'username'
	REQUIRED_FIELD	= ['username']

	objects			= manageAkunAdmin()

	def __str__(self):
		return self.username

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True

# from django.contrib.auth.base_user import BaseUserManager


# class UserManager(BaseUserManager):
# 	use_in_migration = True



# 	def create_user(self, email, username, password=None, **extra_fields):

# 		if not email:
# 			raise ValueError("Email is require")

# 		email = self.normalize_email(email)
		

# 		user = self.model(email=email, username=username, **extra_fields)
# 		user.set_password(password)

# 		user.save(using=self.db)
# 		return user


# 	def create_superuser(self , email, username, password, **extra_fields):
# 		extra_fields.setdefault('is_staff', True)
# 		extra_fields.setdefault('is_superuser', True)
# 		extra_fields.setdefault('is_active', True)


# 		if extra_fields.get('is_staff') is not True:
# 			raise ValueError(('Super user must have is_staff true'))

# 		return self.create_user(email, username, password, **extra_fields)
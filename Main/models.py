from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

# Create your models here.


class AccountManager(BaseUserManager):
    def create_user(self, email , name, password= None):
        if not email:
            raise ValueError("Users must have email address")
        if not name:
            raise ValueError("Users must have a name")
        user = self.model(
            email = self.normalize_email(email),
            name = name,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email,name,password):
        user = self.create_user(
            email = self.normalize_email(email),
            name = name,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using = self._db)
        return user



def get_profile_image_filepath(self):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return "default_profile.png"

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name= "email" , max_length=100, unique= True)
    name  = models.CharField(max_length=50)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add = True)
    last_login  = models.DateTimeField(verbose_name='last login', auto_now = True)
    profile_image = models.ImageField(max_length=255, upload_to= get_profile_image_filepath, null=True, blank=True, default = get_default_profile_image)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default= False)
    is_superuser = models.BooleanField(default= False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = AccountManager()

    def __str__(self):
        return self.name

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

    def has_perm(self , perm , obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True




    
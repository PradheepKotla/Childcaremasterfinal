from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy  as _
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from accounts.managers import CustomUserManager
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.
from django.contrib.auth.models import User

AUTH_PROVIDERS = {'google': 'google', 'email': 'email'}

# register the user
AUTH_PROVIDERS = {'email': 'email'}
class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone_no = models.CharField(unique=True,  null=True,max_length=10)
   
    teacher = models.BooleanField(default=False)
    parent = models.BooleanField(default=False)
    name = models.CharField(max_length=100,null=True)
    auth_provider = models.CharField(max_length=255, blank=False, null=False, default=AUTH_PROVIDERS.get('email'))
    USERNAME_FIELD = 'email'
    objects = CustomUserManager() 
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
  
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _
from defaultPickers.models import State,District,City

from .managers import CustomUserManager
from bazaar.models import Bazaar

AGENT_PROFILE_TYPE=(
    ('individual','individual'),
    ('agency','agency'),
    ('salesman','salesman'),
)

USER_TYPE=(
    ('admin','admin'),
    ('agent','agent'),
    ('customer','customer')
)

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    mobile = models.IntegerField(unique=True)
    state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)
    district = models.ForeignKey(District, null=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=400, null=True)
    kyc_approved = models.BooleanField(default=False)

    userType = models.CharField(choices=USER_TYPE, max_length=30)

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name or "not first name"

    

class AgentProfile(models.Model):
    user = models.ForeignKey(User, related_name='agentProfile', on_delete=models.CASCADE)
    bazaars = models.ManyToManyField(Bazaar, blank=True)
    allocatedStates = models.ManyToManyField(State, blank=True, related_name='allocatedStates')
    allocatedDistricts = models.ManyToManyField(District, blank=True, related_name='allocatedDistricts')
    allocatedCities = models.ManyToManyField(City, blank=True, related_name='allocatedCities')
    agentType = models.CharField(max_length=30,choices=AGENT_PROFILE_TYPE,default='individual')

class CustomerType(models.Model):
    name = models.CharField(max_length=50)

class CustomerProfile(models.Model):
    user = models.ForeignKey(User, related_name='customerProfile', on_delete=models.CASCADE)
    bazaars = models.ManyToManyField(Bazaar, blank=True)
    customer_type=models.ForeignKey(CustomerType, on_delete=models.CASCADE)
from contextlib import nullcontext
from email.policy import default
from unittest.util import _MAX_LENGTH
from bazaar.models import Bazaar
from defaultPickers.models import State, District, City
from django.db import models


class PlanFeature(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


PLAN_TYPE = (
    (0,"Free"),
    (1,"Paid")
)

class Plan(models.Model):
    plan_name = models.CharField(max_length=150)
    amount = models.IntegerField(null=True)
    branches = models.IntegerField(null=True)
    user_per_branch = models.IntegerField(null=True)
    plan_type = models.IntegerField(choices=PLAN_TYPE)
    start_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_date = models.DateField(null=True)
    end_time = models.TimeField(null=True)
    bazaars = models.ManyToManyField(Bazaar, blank=True)
    states = models.ManyToManyField(State, blank=True)
    districts = models.ManyToManyField(District, blank=True)
    cities = models.ManyToManyField(City, blank=True)
    features = models.ManyToManyField(PlanFeature)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self) -> str:
        return self.name

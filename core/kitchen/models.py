# Create your models here.
import re
from django.db import models
from users.models import CustomUser
from base.models import Section
# Create your models here.


class Meal(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=255)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Chef(models.Model):
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.person.first_name + ' ' + self.person.last_name


class Distributor(models.Model):
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.person.first_name + ' ' + self.person.last_name


class Report(models.Model):
    personnel_mistake_report = models.TextField(null=True, blank=True)
    daily_report = models.TextField(null=True, blank=True)
    # extra_foods = models.IntegerField(default=0)
    step = models.IntegerField(default=0)
    report_date = models.DateField(unique=True, null=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (
            ("to_step_1", "To step 1"),
            ("to_step_2", "To step 2"),
            # ("to_step_3", "To step 3"),
        )
    # def __str__(self):
    #     return self.id


class Cook(models.Model):
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, related_name='food')
    preparation_chef = models.ForeignKey(
        Chef, on_delete=models.CASCADE, related_name='preparation_chef')
    cook_chef = models.ForeignKey(
        Chef, on_delete=models.CASCADE, related_name='cook_chef')
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    number_of_foods = models.IntegerField(default=0)
    number_of_extra_foods = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.food


class Distribution(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    distributor1 = models.ForeignKey(
        Distributor, on_delete=models.CASCADE, related_name='distributor1')
    distributor2 = models.ForeignKey(
        Distributor, on_delete=models.CASCADE, related_name='distributor2')
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.section

from django.db import models
from django_options import *

class Country(models.Model):
    name = models.CharField(max_length = 48, choices = COUNTRY_NAME_CHOICES)
    class Meta:
        app_label = 'test'

class Sector(models.Model):
    name = models.CharField(max_length = 48)
    class Meta:
        app_label = 'test'

class Subsector(models.Model):
    name = models.CharField(max_length = 48)
    sector = models.OneToOneField(Sector)
    class Meta:
        app_label = 'test'

class Keyword(models.Model):
    name = models.CharField(max_length = 48)
    class Meta:
        app_label = 'test'

class Volunteer(models.Model):
    first_name = models.CharField(max_length = 48)
    last_name = models.CharField(max_length = 48)
    home_state = models.CharField(max_length = 2, choices = "STATES")
    country = models.OneToOneField(Country, verbose_name = "country of service")
    sector = models.OneToOneField(Subsector, verbose_name = "sector of service")
    start_date = models.DateField(verbose_name = "start date of service")
    end_date = models.DateField(verbose_name = "end date of service")
    email = models.CharField(max_length = 48, verbose_name = "email address")
    language = models.CharField(max_length = 48, verbose_name = "primary language of communication in the field")
    keywords = models.ForeignKey(Keyword, verbose_name = "list of keywords")
    class Meta:
        app_label = 'test'

class Grade(models.Model):
    grade = models.IntegerField()
    class Meta:
        app_label = 'test'

class School(models.Model):
    name = models.CharField(max_length = 80)
    addr1 = models.CharField(max_length = 80, verbose_name = "address line 1")
    addr2 = models.CharField(max_length = 80, verbose_name = "address line 2")
    city = models.CharField(max_length = 80)
    state = models.CharField(max_length = 2, verbose_name = "state abbreviation", choices = "STATES")
    zip = models.IntegerField()
    class Meta:
        app_label = 'test'

class Teacher(models.Model):
    first_name = models.CharField(max_length = 48)
    last_name = models.CharField(max_length = 48)
    school = models.ForeignKey(School, "school")
    phone = models.CharField(max_length=15, verbose_name="work phone")
    email = models.CharField(max_length = 48, verbose_name = "email address")
    grade = models.CharField(max_length = 2, verbose_name = "grade of students", choices=GRADES)
    num_students = models.IntegerField(verbose_name = "number of students")
    keywords = models.ForeignKey(Keyword, verbose_name = "list of keywords")
    class Meta:
        app_label = 'test'

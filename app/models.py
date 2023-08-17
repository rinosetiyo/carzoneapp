from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
    
class Car(models.Model):
    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AR', 'Arkansas'),
    )
    features_choice = (
        ('AC', 'Air Conditioner'),
        ('PW', 'Power Window'),
        ('SR', 'Sunroof'),
    )
    doors_choice = (
        ('2', '2'),
        ('4', '4'),
        ('6', '6'),
    )
    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r,r))

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    state = MultiSelectField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=255)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choice, max_length=100)
    body_style = models.CharField(max_length=255)
    engine = models.CharField(max_length=255)
    transmission = models.CharField(max_length=255)
    interior = models.CharField(max_length=255)
    doors = MultiSelectField(choices=doors_choice, max_length=100)
    passengers = models.IntegerField()
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=255)
    no_of_owner = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(Car, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    email = models.EmailField(max_length=200)
    customer_need = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    car_title = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import os
from datetime import datetime


class open_cat(models.Model):
    style = [
        ('style1', 'style1'),
        ('style2', 'style2'),
        ('style3', 'style3'),
        ('style4', 'style4'),
        ('style5', 'style5'),
        ('style6', 'style6'),

    ]
    categorie_image = models.ImageField(upload_to="open_categories/")
    open_categories = models.CharField(max_length=255, blank=True, null=True)
    style = models.CharField(max_length=10, choices=style)
    slogans = models.CharField(max_length=500 ,blank = True,null=True)

    def __str__(self):
        return self.open_categories
    class Meta:
        verbose_name_plural = "open_cat" 

@receiver(pre_delete, sender=open_cat)
def open_cat_delete(sender, instance, **kwargs):
    # Delete the associated image file when the record is deleted
    if instance.categorie_image:
        storage, path = instance.categorie_image.storage, instance.categorie_image.path
        storage.delete(path)

class founder(models.Model):
    founder_name = models.CharField(max_length=255)
    founder_image = models.ImageField(upload_to='founder/')
    founder_business_type = models.CharField(max_length=255)
    instagram_link = models.URLField(max_length=255)  # For Instagram link
    whatsapp_number = models.CharField(max_length=20)  # For WhatsApp number

    def __str__(self):
        return f"{self.founder_name}"
    
@receiver(pre_delete, sender=founder)
def founder_delete(sender, instance, **kwargs):
    # Delete the associated image file when the record is deleted
    if instance.founder_image:
        storage, path = instance.founder_image.storage, instance.founder_image.path
        storage.delete(path)


class president(models.Model):
    president_name = models.CharField(max_length=255)
    president_image = models.ImageField(upload_to='president/')
    president_business_type = models.CharField(max_length=255)
    instagram_link = models.URLField(max_length=255)  # For Instagram link
    whatsapp_number = models.CharField(max_length=20)  # For WhatsApp number

    def __str__(self):
        return f"{self.president_name}"
    
@receiver(pre_delete, sender=president)
def president_delete(sender, instance, **kwargs):
    # Delete the associated image file when the record is deleted
    if instance.president_image:
        storage, path = instance.president_image.storage, instance.president_image.path
        storage.delete(path)



class vice_president(models.Model):
    vice_president_name = models.CharField(max_length=255)
    vice_president_image = models.ImageField(upload_to='vice_president/')
    vice_president_business_type = models.CharField(max_length=255)
    instagram_link = models.URLField(max_length=255)  # For Instagram link
    whatsapp_number = models.CharField(max_length=20)  # For WhatsApp number
    def __str__(self):
        return f"{self.vice_president_name}"
    
@receiver(pre_delete, sender=vice_president)
def vice_delete(sender, instance, **kwargs):
    # Delete the associated image file when the record is deleted
    if instance.vice_president_image:
        storage, path = instance.vice_president_image.storage, instance.vice_president_image.path
        storage.delete(path)

class secretary(models.Model):
    secretary_name = models.CharField(max_length=255)
    secretary_image = models.ImageField(upload_to='secretary/')
    secretary_business = models.CharField(max_length=255)
    instagram_link = models.URLField(max_length=255)  # For Instagram link
    whatsapp_number = models.CharField(max_length=20)  # For WhatsApp number

    def __str__(self):
        return f"{self.secretary_name}" 

@receiver(pre_delete, sender=secretary)
def secretary_delete(sender, instance, **kwargs):
    # Delete the associated image file when the record is deleted
    if instance.secretary_image:
        storage, path = instance.secretary_image.storage, instance.secretary_image.path
        storage.delete(path)
  

class superior_team(models.Model):
    id = models.AutoField(primary_key=True)
    members_image = models.ImageField(upload_to='superiour_image/')  # For image upload
    name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=255)  # For the type of business
    instagram_link = models.URLField(max_length=255)  # For Instagram link
    whatsapp_number = models.CharField(max_length=20)  # For WhatsApp number
    position = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}" 
@receiver(pre_delete, sender=superior_team)
def superior_delete(sender, instance, **kwargs):
    # Delete the associated image file when the record is deleted
    if instance.members_image:
        storage, path = instance.members_image.storage, instance.members_image.path
        storage.delete(path)

class coordinate_team(models.Model):
    id = models.AutoField(primary_key=True)
    members_image = models.ImageField(upload_to='coordinate_images/')  # For image upload
    name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=255)  # For the type of business
    instagram_link = models.URLField(max_length=255)  # For Instagram link
    whatsapp_number = models.CharField(max_length=20)  # For WhatsApp number
    position = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.members_image} - {self.business_type}"
@receiver(pre_delete, sender=coordinate_team)
def coordinate_delete(sender, instance, **kwargs):
    # Delete the associated image file when the record is deleted
    if instance.members_image:
        storage, path = instance.members_image.storage, instance.members_image.path
        storage.delete(path)
    
class bnc_register_mem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    gmail = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
def generate_upload_path(instance, filename):
    formatted_date = instance.title
    print(formatted_date)
    return f'event_images/{formatted_date}/{filename}'

class Image(models.Model):
    title = models.CharField(max_length=255)  # Assuming you have 
    pic = models.FileField(upload_to=generate_upload_path,blank=True)
@receiver(pre_delete, sender=Image)
def coordinate_delete(sender, instance, **kwargs):
    # Delete the associated image file when the record is deleted
    if instance.pic:
        storage, path = instance.pic.storage, instance.pic.path
        storage.delete(path)

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email_address = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50,blank=True, null=True)
    last_name = models.CharField(max_length=50,blank=True, null=True)
    # date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    pincode = models.TextField(blank=True, null=True)
    # instagram_link = models.URLField(blank=True, null=True)
    instagram_link = models.CharField(max_length=100, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    brand_name = models.CharField(max_length=1000,blank=True, null=True)
    service_name = models.CharField(max_length=50,blank=True, null=True)
    company_address = models.TextField(blank=True, null=True)
    register_id = models.CharField(max_length=10,unique=True)
    user_image = models.ImageField(upload_to='user_images/',blank=True,null=True)
    position = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username
    
class meeting_assign(models.Model):
    Id = models.AutoField(primary_key=True)
    meet_date = models.DateField()
    meet_time = models.TimeField()
    meeting_title = models.CharField(max_length=255)
    meeting_content = models.TextField()
    meeting_location = models.TextField()

    def __str__(self) -> str:
        return self.meeting_title
    
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    event_details = models.TextField()
    event_date = models.DateField()
    event_time = models.TimeField()

    def __str__(self):
        return f"Event(id={self.id}, event_name={self.event_name}, event_details={self.event_details}, " \
               f"event_date={self.event_date}, event_time={self.event_time})"

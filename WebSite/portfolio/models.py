from distutils.command.upload import upload
from enum import auto
from django.db import models

class Home(models.Model):
    name=models.CharField(max_length=25)
    text1=models.CharField(max_length=5)
    text2=models.CharField(max_length=5)
    #picture=models.ImageField(upload_to='media_root/image/')
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class About(models.Model):
    headline=models.CharField(max_length=40)
    profession_title=models.CharField(max_length=20)
    description=models.TextField(blank=True)
    #profile_img=models.ImageField(upload_to='media_root/profile/')
    updated=models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.profession_title

class profile(models.Model):
    about=models.ForeignKey(About,on_delete=models.CASCADE)
    social_name=models.CharField(max_length=12)
    link=models.URLField(max_length=200)

class Category(models.Model):
    name=models.CharField(max_length=20)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Skill'
        verbose_name_plural='Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    skill_name=models.CharField(max_length=20)

class Portfolio(models.Model):
    image=models.ImageField(upload_to='Portfolio/')
    link=models.URLField(max_length=200)
 
    def __str__(self):
        return f'Portfolio {self.id}'
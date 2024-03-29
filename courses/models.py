from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.text import slugify


# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Course(models.Model):
    owner = models.ForeignKey(User, related_name='courses_created', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title    


class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class ItemBase(models.Model):
    owner = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title    

class Text(ItemBase):
    module = models.ForeignKey(Module, related_name='text', on_delete=models.CASCADE)
    content = models.TextField()

class File(ItemBase):
    module = models.ForeignKey(Module, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='files')

class Image(ItemBase):
    module = models.ForeignKey(Module, related_name='images', on_delete=models.CASCADE)
    file = models.FileField(upload_to='images')

class Video(ItemBase):
    module = models.ForeignKey(Module, related_name='videos', on_delete=models.CASCADE)
    url = models.URLField()    
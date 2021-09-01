from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='doc/')
    description = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class Sermon(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    scripture = models.CharField(max_length=500)
    image = models.FileField(upload_to='doc/')
    audios = models.FileField(upload_to='doc/')
    date_made = models.DateField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class subscribe(models.Model):
    email = models.CharField(max_length=500)
    created_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.email

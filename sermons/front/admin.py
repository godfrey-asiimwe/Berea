from django.contrib import admin

# Register your models here.
from django.db import models
from django.forms import Textarea

from .models import Sermon, Author, Category


@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'id': 'project_update_textarea'})}
    }


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

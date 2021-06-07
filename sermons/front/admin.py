from django.contrib import admin

# Register your models here.
from .models import Sermon


@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    pass

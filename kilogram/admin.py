from django.contrib import admin
from .models import Photo

# Register your models here.
# models.py에서 내가 만든 Photo를 admin에 등록하기

admin.site.register(Photo)

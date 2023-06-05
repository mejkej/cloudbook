from django.contrib import admin
from .models import Note
# Note model accessible for admin panel.
admin.site.register(Note)


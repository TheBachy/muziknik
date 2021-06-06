from django.contrib import admin

from .models import *

admin.site.register(Genre)
admin.site.register(Song)
admin.site.register(Attachment)
admin.site.register(Album)
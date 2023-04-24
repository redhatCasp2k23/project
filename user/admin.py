from django.contrib import admin

# Register your models here.
from .models import Report,Vote,SolvedImage
admin.site.register(Report)
admin.site.register(Vote)
admin.site.register(SolvedImage)
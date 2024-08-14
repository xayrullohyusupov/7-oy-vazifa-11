from django.contrib import admin
from . import models

admin.site.register(models.Contact)
admin.site.register(models.ChooseItem)
admin.site.register(models.TeamMember)
admin.site.register(models.Partner)
admin.site.register(models.RoadmapItem)
admin.site.register(models.ContactMessage)
from django.contrib import admin
from .models import Member, News, Project, Event, YEvent, Number, Collaborator

admin.site.register(Member)
admin.site.register(News)
admin.site.register(Project)
admin.site.register(Event)
admin.site.register(Number)
admin.site.register(YEvent)
admin.site.register(Collaborator)
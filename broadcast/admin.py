from django.contrib import admin

from broadcast.models import Message, Client, Mailing

admin.site.register(Mailing)
admin.site.register(Client)
admin.site.register(Message)

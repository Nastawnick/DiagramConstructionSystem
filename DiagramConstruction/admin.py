from django.contrib import admin
from .models import User, Session, UserMessage, UserMistake, ServerMessage, Mistake, Theme 
# Register your models here.

admin.site.register(User)
admin.site.register(Session)
admin.site.register(UserMessage)
admin.site.register(UserMistake)
admin.site.register(ServerMessage)
admin.site.register(Mistake)
admin.site.register(Theme)
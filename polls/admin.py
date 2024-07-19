from django.contrib import admin
import polls.models as polls 

@admin.register(polls.Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ("poll_name", "poll_number")
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Main.models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email','name','date_joined','last_login','is_admin','is_staff')
    search_fields = ('email',)
    readonly_fields = ('id','date_joined', 'last_login')
    ordering = ('email',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
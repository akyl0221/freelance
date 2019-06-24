from django.contrib import admin

from .models import CustomUser, Transaction


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'role', 'balance')


class UserChangeBalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'reason', 'amount', 'datetime',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Transaction, UserChangeBalanceAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import User




class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("phone_number", "is_staff", "is_active",)
    list_filter = ("phone_number", "is_staff", "is_active",)
    fieldsets = (
        (None, {
            "fields": ("phone_number", "password"   
            ),
        }),
        ('Permission', {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes":("wide",),
            "fields":(
                "phone_number", "password", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )
        }),
    )
    search_fileds = ("phone_number",)
    ordering = ("phone_number",)

admin.site.register(User, UserAdmin)


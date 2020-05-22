from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# big s/o to this so question: https://stackoverflow.com/questions/54341927/addig-form-fields-to-a-custom-user-model-in-django-admin-panel
# and this article I had opened the entire time but didn't read until the above question sent me to it:
# https://testdriven.io/blog/django-custom-user-model/#admin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = MyUser
    list_display = ('username', 'is_staff', 'is_active',)
    list_filter = ('username', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'display_name', 'homepage', 'age')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('display_name', 'homepage', 'age',
            'password1', 'password2', 'is_staff', 'is_active')
        }),
    )

admin.site.register(MyUser, CustomUserAdmin)
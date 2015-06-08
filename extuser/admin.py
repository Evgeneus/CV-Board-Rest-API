from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from extuser.forms import UserChangeForm, UserCreationForm
from extuser.models import ExtUser


@admin.register(ExtUser)
class ExtUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('first_name', 'last_name', 'email',
                    'date_of_birth', 'age', 'location',
                    'desired_salary', 'register_date',
                    'last_change', 'role', 'is_active', 'other')

    list_filter = ('role',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',
                                      'date_of_birth', 'age', 'location',)}),
        ('Permissions', {'fields': ('role',)}),
        ('Salary', {'fields': ('desired_salary',)}),
        ('Additional infornations', {'fields': ('is_active', 'other')})
    )

    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('email', ('date_of_birth',), 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name',
                                      'age', 'location',)}),
        ('Permissions', {'fields': ('role',)}),
        ('Salary', {'fields': ('desired_salary',)}),
        ('Additional infornations', {'fields': ('other',)}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

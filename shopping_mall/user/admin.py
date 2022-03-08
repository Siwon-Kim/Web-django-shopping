from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', )

    def changelist_view(self, request, extra_context=None):
        extra_context = { 'title': 'User List' }
        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        user = User.objects.get(pk=object_id)
        extra_context = {'title': f'Change {user.email}'}
        return super().changeform_view(request, object_id, form_url, extra_context)


admin.site.register(User, UserAdmin)
from django.contrib import admin
from models import Clasa, Student, Profesor


class StudentAdmin(admin.ModelAdmin):
    def queryset(self, request):
        qs = super(StudentAdmin, self).queryset(request)

        if request.user.is_superuser:
            return qs

        user = request.user
        if user.has_perm('cms.edit') and user.has_perm('cms.view'):
            return qs
        else:
            raise PermissionDenied


class ProfesorAdmin(admin.ModelAdmin):
    def queryset(self, request):
        qs = super(ProfesorAdmin, self).queryset(request)

        if request.user.is_superuser:
            return qs

        user = request.user
        if user.has_perm('cms.edit') and user.has_perm('cms.view') and\
            user.has_perm('cms.add') and user.has_perm('cms.assign'):
            return qs
        else:
            raise PermissionDenied


admin.site.register(Clasa)
admin.site.register(Student, StudentAdmin)
admin.site.register(Profesor, ProfesorAdmin)


from django.contrib import admin

from .models import Room, Reservation, EmployeeRoom, Employee

class RoomInline(admin.TabularInline):
    model = Room.employees.through
    extra = 1
class ReservationAdmin(admin.ModelAdmin):
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(ReservationAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user and (obj.employee.type == 'm' or obj.employee.type == 'r'):
            return True
        return False


class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomInline]
    exclude = ('employees',)
    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and obj.employees.type == 'h':
            return True
        return False

admin.site.register(Room,RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(EmployeeRoom)
admin.site.register(Employee)
# Register your models here.

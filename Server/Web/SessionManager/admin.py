from django.contrib import admin
from .models import active_sessions, users_on_timeout, restricted_sessions, express_sessions, multi_session, computer_zone, computer, locked_computer

# Register your models here.
@admin.register(active_sessions)
class ActiveSessionsAdmin(admin.ModelAdmin):
    pass

@admin.register(users_on_timeout)
class UsersOnTimeoutAdmin(admin.ModelAdmin):
    pass

@admin.register(restricted_sessions)
class RestrictedSessionsAdmin(admin.ModelAdmin):
    pass

@admin.register(express_sessions)
class ExpressSessionsAdmin(admin.ModelAdmin):
    pass

@admin.register(multi_session)
class MultiSessionAdmin(admin.ModelAdmin):
    pass

@admin.register(computer_zone)
class ComputerZoneAdmin(admin.ModelAdmin):
    pass

@admin.register(computer)
class ComputerAdmin(admin.ModelAdmin):
    pass

@admin.register(locked_computer)
class LockedComputerAdmin(admin.ModelAdmin):
    pass

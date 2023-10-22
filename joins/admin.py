from django.contrib import admin

from .models import *


# Register your models here.


class JoinModelAdmin(admin.ModelAdmin):
    list_display = ["email", "ref_id", "timestamp"]

    class Meta:
        model = Join


admin.site.register(Join, JoinModelAdmin)


class EmailModelAdmin(admin.ModelAdmin):
    list_display = ["email", "timestamp"]

    class Meta:
        model = Email


admin.site.register(Email, EmailModelAdmin)


class AcctModelAdmin(admin.ModelAdmin):
    list_display = ["id", "fname", "lname", "timestamp"]

    class Meta:
        model = t_acct


admin.site.register(t_acct, AcctModelAdmin)


class AttriModelAdmin(admin.ModelAdmin):
    list_display = ["id", "department", "level", "status", "timestamp"]

    class Meta:
        model = t_user_attribute


admin.site.register(t_user_attribute, AttriModelAdmin)


class ChildrenAdmin(admin.ModelAdmin):
    list_display = [
        "rootid",
        "relationship",
    ]

    class Meta:
        model = t_children


admin.site.register(t_children, ChildrenAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = ["id", "rootid", "name", "category"]

    class Meta:
        model = t_group


admin.site.register(t_group, GroupAdmin)


class UserPicAdmin(admin.ModelAdmin):
    list_display = [
        "id",
    ]

    class Meta:
        model = UserProfile


admin.site.register(UserProfile, UserPicAdmin)

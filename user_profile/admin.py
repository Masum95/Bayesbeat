from django.contrib import admin
from user_profile import models

admin.site.register(models.MyFile)
admin.site.register(models.UserHealthProfile)


class WatchDistributionModelAdmin(admin.ModelAdmin):
    readonly_fields=('registration_id',)

admin.site.register(models.WatchDistributionModel, WatchDistributionModelAdmin)


#
# @admin.register(models.SupplyOrder)
# class FeedbackAdmin(admin.ModelAdmin):
#     list_filter = ('author', )
#
# @admin.register(models.FeedbackReact)
# class FeedbackAdmin(admin.ModelAdmin):
#     list_filter = ('post', )
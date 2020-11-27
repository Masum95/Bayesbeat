from django.contrib import admin
from user_profile import models

admin.site.register(models.MyFile)

#
# @admin.register(models.SupplyOrder)
# class FeedbackAdmin(admin.ModelAdmin):
#     list_filter = ('author', )
#
# @admin.register(models.FeedbackReact)
# class FeedbackAdmin(admin.ModelAdmin):
#     list_filter = ('post', )
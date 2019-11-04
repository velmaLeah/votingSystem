from django.contrib import admin
from .models import President, Choice, Position

admin.site.site_header = "SU-Voting System"
admin.site.site_title = "SU-Voting System: Admin Area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class PositionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['position_name']}), ]
    inlines = [ChoiceInline]


admin.site.register(Position, PositionAdmin)

admin.site.register(President)


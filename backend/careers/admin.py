from django.contrib import admin
from .models import Career
@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ("title", "sector", "source_verified", "updated_at")
    list_filter = ("sector", "source_verified")
    search_fields = ("title", "description")

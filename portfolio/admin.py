from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "owner",
        "featured",
        "is_active",
        "created_at",
    )

    list_filter = (
        "category",
        "featured",
        "is_active",
    )

    search_fields = (
        "title",
        "description",
        "technologies",
        "owner__username",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )
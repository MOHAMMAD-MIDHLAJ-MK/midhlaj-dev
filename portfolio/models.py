from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Project(models.Model):

    # =====================================================
    # CATEGORY
    # =====================================================

    CATEGORY_CHOICES = [
        ("django", "Django"),
        ("full stack", "Full Stack"),
        ("frontend", "Frontend"),
        ("backend", "Backend"),
        ("web application", "Web Application"),
        ("other", "Other"),
    ]

    # =====================================================
    # BASIC INFORMATION
    # =====================================================

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default="other"
    )

    description = models.TextField(
        blank=True
    )

    # =====================================================
    # COVER IMAGE
    # =====================================================

    cover_image = models.ImageField(
        upload_to="projects/covers/",
        blank=True,
        null=True
    )

    cover_paragraph = models.TextField(
        blank=True,
        null=True
    )

    # =====================================================
    # PROJECT IMAGES
    # =====================================================

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    image_paragraph = models.TextField(
        blank=True,
        null=True
    )

    image_2 = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    image_2_paragraph = models.TextField(
        blank=True,
        null=True
    )

    image_3 = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    image_3_paragraph = models.TextField(
        blank=True,
        null=True
    )

    # =====================================================
    # VIDEO
    # =====================================================

    video = models.FileField(
        upload_to="project_videos/",
        blank=True,
        null=True
    )

    video_paragraph = models.TextField(
        blank=True,
        null=True
    )

    # =====================================================
    # TECHNOLOGIES
    # =====================================================

    technologies = models.CharField(
        max_length=500,
        blank=True
    )

    # =====================================================
    # PROJECT LINKS
    # =====================================================

    github_url = models.URLField(
        blank=True,
        null=True
    )

    live_url = models.URLField(
        blank=True,
        null=True
    )

    # =====================================================
    # PROJECT STATUS
    # =====================================================

    featured = models.BooleanField(
        default=False,
        verbose_name="Featured Project"
    )

    recent = models.BooleanField(
        default=False,
        verbose_name="Recent Project"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Project Active"
    )

    # =====================================================
    # OWNER
    # =====================================================

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="projects",
        blank=True,
        null=True
    )

    # =====================================================
    # DATES
    # =====================================================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    # =====================================================
    # SAVE
    # =====================================================

    def save(self, *args, **kwargs):

        if not self.slug:

            base_slug = slugify(self.title)

            new_slug = base_slug
            counter = 1

            while Project.objects.filter(
                slug=new_slug
            ).exclude(
                pk=self.pk
            ).exists():

                new_slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = new_slug

        super().save(*args, **kwargs)

    # =====================================================
    # TECHNOLOGY LIST
    # =====================================================

    @property
    def technology_list(self):

        if not self.technologies:
            return []

        return [
            tech.strip()
            for tech in self.technologies.split(",")
            if tech.strip()
        ]

    # =====================================================
    # STRING
    # =====================================================

    def __str__(self):
        return self.title

    # =====================================================
    # META
    # =====================================================

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"


# =========================================================
# PROJECT CONTENT
# =========================================================

class ProjectContent(models.Model):

    CONTENT_TYPE_CHOICES = [
        ("image", "Image"),
        ("video", "Video"),
    ]

    # =====================================================
    # PROJECT
    # =====================================================

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="contents"
    )

    # =====================================================
    # CONTENT TYPE
    # =====================================================

    content_type = models.CharField(
        max_length=10,
        choices=CONTENT_TYPE_CHOICES,
        default="image"
    )

    # =====================================================
    # IMAGE
    # =====================================================

    image = models.ImageField(
        upload_to="projects/content/images/",
        blank=True,
        null=True
    )

    # =====================================================
    # VIDEO
    # =====================================================

    video = models.FileField(
        upload_to="projects/content/videos/",
        blank=True,
        null=True
    )

    # =====================================================
    # TITLE
    # =====================================================

    title = models.CharField(
        max_length=200,
        blank=True
    )

    # =====================================================
    # DESCRIPTION
    # =====================================================

    paragraph = models.TextField(
        blank=True
    )

    # =====================================================
    # ORDER
    # =====================================================

    order = models.PositiveIntegerField(
        default=0
    )

    # =====================================================
    # ACTIVE
    # =====================================================

    is_active = models.BooleanField(
        default=True
    )

    # =====================================================
    # DATES
    # =====================================================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    # =====================================================
    # META
    # =====================================================

    class Meta:
        ordering = [
            "order",
            "created_at"
        ]

    # =====================================================
    # STRING
    # =====================================================

    def __str__(self):

        return (
            f"{self.project.title} - "
            f"{self.content_type} - "
            f"{self.order}"
        )
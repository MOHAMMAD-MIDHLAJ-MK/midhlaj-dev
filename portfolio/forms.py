from django import forms

from .models import Project, ProjectContent


# =========================================================
# PROJECT FORM
# =========================================================

class ProjectForm(forms.ModelForm):

    # =====================================================
    # TECHNOLOGY OPTIONS
    # =====================================================

    TECHNOLOGY_CHOICES = [
        ("Python", "Python"),
        ("Django", "Django"),
        ("HTML", "HTML"),
        ("CSS", "CSS"),
        ("JavaScript", "JavaScript"),
        ("Bootstrap", "Bootstrap"),
        ("Tailwind CSS", "Tailwind CSS"),
        ("React", "React"),
        ("jQuery", "jQuery"),
        ("REST API", "REST API"),
        ("MySQL", "MySQL"),
        ("SQLite", "SQLite"),
        ("PostgreSQL", "PostgreSQL"),
        ("MongoDB", "MongoDB"),
        ("Git", "Git"),
        ("GitHub", "GitHub"),
        ("Figma", "Figma"),
        ("AJAX", "AJAX"),
        ("JSON", "JSON"),
        ("API", "API"),
    ]

    technologies = forms.MultipleChoiceField(
        choices=TECHNOLOGY_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "technology-checkboxes",
            }
        ),
        label="Technologies Used",
    )

    # =====================================================
    # META
    # =====================================================

    class Meta:

        model = Project

        fields = [

            # =============================================
            # BASIC INFORMATION
            # =============================================

            "title",
            "category",
            "description",

            # =============================================
            # COVER IMAGE
            # =============================================

            "cover_image",
            "cover_paragraph",

            # =============================================
            # IMAGE 01
            # =============================================

            "image",
            "image_paragraph",

            # =============================================
            # IMAGE 02
            # =============================================

            "image_2",
            "image_2_paragraph",

            # =============================================
            # IMAGE 03
            # =============================================

            "image_3",
            "image_3_paragraph",

            # =============================================
            # VIDEO
            # =============================================

            "video",
            "video_paragraph",

            # =============================================
            # TECHNOLOGIES
            # =============================================

            "technologies",

            # =============================================
            # LINKS
            # =============================================

            "github_url",
            "live_url",

            # =============================================
            # STATUS
            # =============================================

            "featured",
            "is_active",
        ]

        widgets = {

            # =============================================
            # TITLE
            # =============================================

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter project title",
                    "autocomplete": "off",
                }
            ),

            # =============================================
            # CATEGORY
            # =============================================

            "category": forms.Select(
                attrs={
                    "class": "form-control category-select",
                }
            ),

            # =============================================
            # DESCRIPTION
            # =============================================

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": (
                        "Describe your project, "
                        "features and functionality..."
                    ),
                    "rows": 6,
                }
            ),

            # =============================================
            # COVER IMAGE
            # =============================================

            "cover_image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),

            "cover_paragraph": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": (
                        "Write a short description "
                        "for the cover image..."
                    ),
                    "rows": 4,
                }
            ),

            # =============================================
            # IMAGE 01
            # =============================================

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),

            "image_paragraph": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": (
                        "Write a description for Image 01..."
                    ),
                    "rows": 4,
                }
            ),

            # =============================================
            # IMAGE 02
            # =============================================

            "image_2": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),

            "image_2_paragraph": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": (
                        "Write a description for Image 02..."
                    ),
                    "rows": 4,
                }
            ),

            # =============================================
            # IMAGE 03
            # =============================================

            "image_3": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),

            "image_3_paragraph": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": (
                        "Write a description for Image 03..."
                    ),
                    "rows": 4,
                }
            ),

            # =============================================
            # VIDEO
            # =============================================

            "video": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "video/*",
                }
            ),

            "video_paragraph": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": (
                        "Describe what is demonstrated "
                        "in the project video..."
                    ),
                    "rows": 4,
                }
            ),

            # =============================================
            # GITHUB
            # =============================================

            "github_url": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": (
                        "https://github.com/username/project"
                    ),
                    "autocomplete": "off",
                }
            ),

            # =============================================
            # LIVE DEMO
            # =============================================

            "live_url": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": (
                        "https://your-project.com"
                    ),
                    "autocomplete": "off",
                }
            ),

            # =============================================
            # FEATURED
            # =============================================

            "featured": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),

            # =============================================
            # ACTIVE
            # =============================================

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

        labels = {

            "title": "Project Title",
            "category": "Project Category",
            "description": "Project Description",

            "cover_image": "Project Cover Image",
            "cover_paragraph": "Cover Image Description",

            "image": "Project Image 01",
            "image_paragraph": "Image 01 Description",

            "image_2": "Project Image 02",
            "image_2_paragraph": "Image 02 Description",

            "image_3": "Project Image 03",
            "image_3_paragraph": "Image 03 Description",

            "video": "Project Demo Video",
            "video_paragraph": "Video Description",

            "technologies": "Technologies Used",

            "github_url": "GitHub Repository",
            "live_url": "Live Demo",

            "featured": "Featured Project",
            "is_active": "Project Active",
        }

        help_texts = {

            "cover_image": (
                "Upload the main cover image."
            ),

            "cover_paragraph": (
                "Explain what the cover image represents."
            ),

            "image": (
                "Upload the first project screenshot."
            ),

            "image_paragraph": (
                "Explain what Image 01 shows."
            ),

            "image_2": (
                "Upload the second project screenshot."
            ),

            "image_2_paragraph": (
                "Explain what Image 02 shows."
            ),

            "image_3": (
                "Upload the third project screenshot."
            ),

            "image_3_paragraph": (
                "Explain what Image 03 shows."
            ),

            "video": (
                "Upload your project demonstration video."
            ),

            "video_paragraph": (
                "Explain what users can see in the video."
            ),

            "technologies": (
                "Select all technologies used in this project."
            ),

            "github_url": (
                "Optional GitHub repository."
            ),

            "live_url": (
                "Optional live project URL."
            ),

            "featured": (
                "Show this project on the homepage."
            ),

            "is_active": (
                "Inactive projects are hidden from the project list."
            ),
        }

    # =====================================================
    # INITIALIZE
    # =====================================================

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # Existing technologies:
        #
        # "Python, Django, HTML"
        #
        # becomes:
        #
        # ["Python", "Django", "HTML"]

        if self.instance and self.instance.pk:

            if self.instance.technologies:

                self.initial["technologies"] = [
                    tech.strip()
                    for tech in self.instance.technologies.split(",")
                    if tech.strip()
                ]

    # =====================================================
    # SAVE
    # =====================================================

    def save(self, commit=True):

        project = super().save(commit=False)

        technologies = self.cleaned_data.get(
            "technologies",
            []
        )

        project.technologies = ", ".join(
            technologies
        )

        if commit:
            project.save()

        return project


# =========================================================
# PROJECT CONTENT FORM
# =========================================================

class ProjectContentForm(forms.ModelForm):

    class Meta:

        model = ProjectContent

        fields = [
            "content_type",
            "image",
            "video",
            "title",
            "paragraph",
            "order",
            "is_active",
        ]

        widgets = {

            # =============================================
            # CONTENT TYPE
            # =============================================

            "content_type": forms.Select(
                attrs={
                    "class": "form-control content-type-input",
                }
            ),

            # =============================================
            # IMAGE
            # =============================================

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control content-image-input",
                    "accept": "image/*",
                }
            ),

            # =============================================
            # VIDEO
            # =============================================

            "video": forms.ClearableFileInput(
                attrs={
                    "class": "form-control content-video-input",
                    "accept": "video/*",
                }
            ),

            # =============================================
            # TITLE
            # =============================================

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Content title...",
                    "autocomplete": "off",
                }
            ),

            # =============================================
            # PARAGRAPH
            # =============================================

            "paragraph": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": (
                        "Write a description for "
                        "this image or video..."
                    ),
                    "rows": 5,
                }
            ),

            # =============================================
            # ORDER
            # =============================================

            "order": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                    "placeholder": "Display order",
                }
            ),

            # =============================================
            # ACTIVE
            # =============================================

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

        labels = {

            "content_type": "Content Type",
            "image": "Project Image",
            "video": "Project Video",
            "title": "Content Title",
            "paragraph": "Content Description",
            "order": "Display Order",
            "is_active": "Active",
        }

    # =====================================================
    # CLEAN
    # =====================================================

    def clean(self):

        cleaned_data = super().clean()

        content_type = cleaned_data.get(
            "content_type"
        )

        image = cleaned_data.get(
            "image"
        )

        video = cleaned_data.get(
            "video"
        )

        # =================================================
        # IMAGE
        # =================================================

        if content_type == "image":

            if not image:

                if (
                    not self.instance.pk
                    or not self.instance.image
                ):

                    raise forms.ValidationError(
                        "Please upload an image."
                    )

            cleaned_data["video"] = None

        # =================================================
        # VIDEO
        # =================================================

        elif content_type == "video":

            if not video:

                if (
                    not self.instance.pk
                    or not self.instance.video
                ):

                    raise forms.ValidationError(
                        "Please upload a video."
                    )

            cleaned_data["image"] = None

        # =================================================
        # INVALID
        # =================================================

        else:

            raise forms.ValidationError(
                "Please select Image or Video."
            )

        return cleaned_data
from django import forms
from django.forms import inlineformset_factory

from .models import Project, ProjectContent


class ProjectContentForm(forms.ModelForm):

    class Meta:
        model = ProjectContent

        fields = [
            "content_type",
            "image",
            "video",
            "title",
            "paragraph",
            "order",
            "is_active",
        ]

        widgets = {
            "content_type": forms.Select(
                attrs={
                    "class": "content-type-input",
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "content-image-input",
                    "accept": "image/png,image/jpeg,image/jpg,image/webp,image/gif",
                }
            ),

            "video": forms.ClearableFileInput(
                attrs={
                    "class": "content-video-input",
                    "accept": "video/mp4,video/webm,video/ogg",
                }
            ),

            "title": forms.TextInput(
                attrs={
                    "class": "content-title-input",
                    "placeholder": "Content title...",
                    "autocomplete": "off",
                }
            ),

            "paragraph": forms.Textarea(
                attrs={
                    "class": "content-paragraph-input",
                    "placeholder": "Write a description for this image or video...",
                    "rows": 4,
                }
            ),

            "order": forms.NumberInput(
                attrs={
                    "class": "content-order-input",
                    "min": 1,
                }
            ),

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "content-active-input",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        content_type = cleaned_data.get("content_type")
        image = cleaned_data.get("image")
        video = cleaned_data.get("video")

        if content_type == "image":
            if not image:
                if not self.instance.pk or not self.instance.image:
                    raise forms.ValidationError(
                        "Please upload an image."
                    )

            cleaned_data["video"] = None

        elif content_type == "video":
            if not video:
                if not self.instance.pk or not self.instance.video:
                    raise forms.ValidationError(
                        "Please upload a video."
                    )

            cleaned_data["image"] = None

        return cleaned_data


ProjectContentFormSet = inlineformset_factory(
    Project,
    ProjectContent,
    form=ProjectContentForm,
    extra=0,
    can_delete=True,
)    
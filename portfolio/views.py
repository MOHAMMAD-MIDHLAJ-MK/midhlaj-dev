from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Project
from .forms import ProjectForm, ProjectContentFormSet


# =========================================================
# HOME
# =========================================================

def home(request):

    featured_projects = (
        Project.objects
        .filter(
            featured=True,
            is_active=True
        )
        .order_by("-created_at")[:3]
    )

    return render(
        request,
        "portfolio/home.html",
        {
            "featured_projects": featured_projects,
        }
    )


# =========================================================
# ABOUT
# =========================================================

def about(request):

    return render(
        request,
        "portfolio/about.html"
    )


# =========================================================
# SKILLS
# =========================================================

def skills(request):

    return render(
        request,
        "portfolio/skills.html"
    )


# =========================================================
# PROJECT LIST
# =========================================================

def projects(request):

    project_list = (
        Project.objects
        .filter(
            is_active=True
        )
        .order_by("-created_at")
    )

    return render(
        request,
        "portfolio/projects.html",
        {
            "projects": project_list,
        }
    )


# =========================================================
# PROJECT DETAIL
# =========================================================

def project_detail(request, slug):

    project = get_object_or_404(
        Project,
        slug=slug,
        is_active=True
    )

    contents = (
        project.contents
        .filter(is_active=True)
        .order_by(
            "order",
            "created_at"
        )
    )

    technologies = []

    if project.technologies:

        technologies = [
            tech.strip()
            for tech in project.technologies.split(",")
            if tech.strip()
        ]

    return render(
        request,
        "portfolio/project_detail.html",
        {
            "project": project,
            "contents": contents,
            "technologies": technologies,
        }
    )


# =========================================================
# ADD PROJECT
# =========================================================

@login_required
def add_project(request):

    if request.method == "POST":

        project_form = ProjectForm(
            request.POST,
            request.FILES
        )

        content_formset = ProjectContentFormSet(
            request.POST,
            request.FILES,
            prefix="contents"
        )

        if (
            project_form.is_valid()
            and content_formset.is_valid()
        ):

            project = project_form.save(
                commit=False
            )

            project.owner = request.user

            project.save()

            content_formset.instance = project

            content_formset.save()

            messages.success(
                request,
                "Project added successfully!"
            )

            return redirect(
                "project_detail",
                slug=project.slug
            )

    else:

        project_form = ProjectForm()

        content_formset = ProjectContentFormSet(
            prefix="contents"
        )

    return render(
        request,
        "portfolio/add_project.html",
        {
            "project_form": project_form,
            "content_formset": content_formset,
        }
    )


# =========================================================
# EDIT PROJECT
# =========================================================

@login_required
def edit_project(request, slug):

    project = get_object_or_404(
        Project,
        slug=slug
    )

    # -----------------------------------------
    # OWNER CHECK
    # -----------------------------------------

    if (
        project.owner
        and project.owner != request.user
    ):
        messages.error(
            request,
            "You are not allowed to edit this project."
        )

        return redirect(
            "project_detail",
            slug=project.slug
        )

    # -----------------------------------------
    # POST
    # -----------------------------------------

    if request.method == "POST":

        form = ProjectForm(
            request.POST,
            request.FILES,
            instance=project
        )

        if form.is_valid():

            project = form.save(
                commit=False
            )

            if not project.owner:
                project.owner = request.user

            project.save()

            messages.success(
                request,
                "Project updated successfully!"
            )

            return redirect(
                "project_detail",
                slug=project.slug
            )

    # -----------------------------------------
    # GET
    # -----------------------------------------

    else:

        form = ProjectForm(
            instance=project
        )

    return render(
        request,
        "portfolio/edit_project.html",
        {
            "form": form,
            "project": project,
        }
    )


# =========================================================
# DELETE PROJECT
# =========================================================

@login_required
def delete_project(request, slug):

    project = get_object_or_404(
        Project,
        slug=slug
    )

    # -----------------------------------------
    # OWNER CHECK
    # -----------------------------------------

    if (
        project.owner
        and project.owner != request.user
    ):
        messages.error(
            request,
            "You are not allowed to delete this project."
        )

        return redirect(
            "project_detail",
            slug=project.slug
        )

    # -----------------------------------------
    # DELETE
    # -----------------------------------------

    if request.method == "POST":

        project.delete()

        messages.success(
            request,
            "Project deleted successfully!"
        )

        return redirect(
            "projects"
        )

    return render(
        request,
        "portfolio/delete_project.html",
        {
            "project": project,
        }
    )


# =========================================================
# CONTACT
# =========================================================

def contact(request):

    if request.method == "POST":

        name = request.POST.get(
            "name",
            ""
        ).strip()

        email = request.POST.get(
            "email",
            ""
        ).strip()

        subject = request.POST.get(
            "subject",
            ""
        ).strip()

        message = request.POST.get(
            "message",
            ""
        ).strip()

        if (
            not name
            or not email
            or not message
        ):

            messages.error(
                request,
                "Please fill in all required fields."
            )

            return redirect(
                "contact"
            )

        messages.success(
            request,
            "Your message has been sent successfully!"
        )

        return redirect(
            "contact"
        )

    return render(
        request,
        "portfolio/contact.html"
    )


# =========================================================
# RESUME
# =========================================================

def resume(request):

    return render(
        request,
        "portfolio/resume.html"
    )
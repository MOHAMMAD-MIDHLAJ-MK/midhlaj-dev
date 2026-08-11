from django.urls import path

from . import views

urlpatterns = [

    # =====================================================
    # HOME
    # =====================================================

    path(
        "",
        views.home,
        name="home"
    ),

    # =====================================================
    # ABOUT
    # =====================================================

    path(
        "about/",
        views.about,
        name="about"
    ),

    # =====================================================
    # SKILLS
    # =====================================================

    path(
        "skills/",
        views.skills,
        name="skills"
    ),

    # =====================================================
    # PROJECTS
    # =====================================================

    path(
        "projects/",
        views.projects,
        name="projects"
    ),

    # =====================================================
    # ADD PROJECT
    # =====================================================

    path(
        "projects/add/",
        views.add_project,
        name="add_project"
    ),

    # =====================================================
    # EDIT PROJECT
    # =====================================================

    path(
        "projects/<slug:slug>/edit/",
        views.edit_project,
        name="edit_project"
    ),

    # =====================================================
    # DELETE PROJECT
    # =====================================================

    path(
        "projects/<slug:slug>/delete/",
        views.delete_project,
        name="delete_project"
    ),

    # =====================================================
    # PROJECT DETAIL
    # =====================================================

    path(
        "projects/<slug:slug>/",
        views.project_detail,
        name="project_detail"
    ),

    # =====================================================
    # CONTACT
    # =====================================================

    path(
        "contact/",
        views.contact,
        name="contact"
    ),

    # =====================================================
    # RESUME
    # =====================================================

    path(
        "resume/",
        views.resume,
        name="resume"
    ),
    path(
    "projects/<slug:slug>/edit/",
    views.edit_project,
    name="edit_project"
    ),
    # ACCOUNT
]
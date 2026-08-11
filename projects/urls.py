from django.urls import path
from . import views


urlpatterns = [

    path(
        "ecommerce/",
        views.ecommerce,
        name="ecommerce"
    ),

    path(
        "hospital/",
        views.hospital,
        name="hospital"
    ),

    path(
        "hotel/",
        views.hotel,
        name="hotel"
    ),

    path(
        "portfolio/",
        views.portfolio_project,
        name="portfolio_project"
    ),

    path(
        "chat/",
        views.chat,
        name="chat"
    ),

]
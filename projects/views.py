from django.shortcuts import render


def ecommerce(request):
    return render(request, "projects/ecommerce.html")


def hospital(request):
    return render(request, "projects/hospital.html")


def hotel(request):
    return render(request, "projects/hotel.html")


def portfolio_project(request):
    return render(request, "projects/portfolio.html")


def chat(request):
    return render(request, "projects/chat.html")
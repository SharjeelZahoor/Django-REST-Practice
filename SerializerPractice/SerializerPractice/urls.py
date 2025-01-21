
from django.contrib import admin
from django.urls import path
from SerialPrac import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("std_info/", views.student_details),
    path("std_info/<int:pk>", views.student_detailone),
]

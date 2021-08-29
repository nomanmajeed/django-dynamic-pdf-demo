from django.urls import path, include
from .views import (
    home,
    post_student,
    update_student_put,
    update_student_patch,
    delete_student,
    get_book,
    StudentAPI,
    RegisterAPI,
    GeneratePDF,
)

urlpatterns = [
    path("", home, name="home"),
    path("post_student", post_student, name="post_student"),
    path("update_student_put/<int:id>", update_student_put, name="update_student_put"),
    path(
        "update_student_patch/<int:id>",
        update_student_patch,
        name="update_student_patch",
    ),
    path(
        "delete_student/<int:id>",
        delete_student,
        name="delete_student",
    ),
    path(
        "get_book",
        get_book,
        name="get_book",
    ),
    path("student", StudentAPI.as_view(), name="student_api"),
    path("register", RegisterAPI.as_view(), name="register_api"),
    path("pdf", GeneratePDF.as_view(), name="pdf_api"),
]

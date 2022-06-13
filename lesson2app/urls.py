from django.urls import path

from lesson2app import views
from lesson2app.apps import Lesson2AppConfig

app_name = Lesson2AppConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main_page"),
    path("news/", views.NewsPageView.as_view(), name="news"),
    path("courses/", views.CoursesPageView.as_view(), name="courses"),
    path("contacts/", views.ContactsPageView.as_view(), name="contacts"),
    path("doc_site/", views.DocSitePageView.as_view(), name="doc_site"),
    path("login/", views.LoginPageView.as_view(), name="login"),
]


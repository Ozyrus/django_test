from django.conf.urls import url

from . import views
app_name='courses'

urlpatterns = [
    url(r"^$", views.all_courses, name="courselist"),
    url(r"(?P<course_pk>\d+)/(?P<step_pk>\d+)/$", views.step_detail, name="steps"),
    url(r"(?P<pk>\d+)/$", views.course_detail, name="detail"),
]
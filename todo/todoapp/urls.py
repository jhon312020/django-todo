from django.conf.urls import url
from todoapp import views


app_name = 'todoapp'

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^$', views.CoachesPageView.as_view()),
    url(r'^login', views.login),
]

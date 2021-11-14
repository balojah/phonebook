from django.urls import path, re_path
from .views import home_page, edit


urlpatterns = [
    path('', home_page, name='contact_view'),
    re_path(r'^edit/(?P<pk>[0-9]+)/$', edit, name='edit')
]

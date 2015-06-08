from django.conf.urls import url, include
from rest_framework import routers
import views

from views.loginsys import UserRegister
router = routers.DefaultRouter()
router.register(r'users', views.UserViewset)
router.register(r'groups', views.GroupViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/login', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^auth/refresh', 'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^auth/register', UserRegister.as_view()),
]

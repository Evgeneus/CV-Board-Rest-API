from django.conf.urls import url, include
from rest_framework import routers
import views

from views.loginsys import UserRegister
from views.skill import SetSkillView
from views.user_group import UserView, GetUsersView
from views.skill_rate_log import SkillRateLogView
from views.company_manag import CreateCompanyView, ManageCompanyView
from views.job import CreateJobView
router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/login', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^auth/refresh', 'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^auth/register', UserRegister.as_view()),
    url(r'^user/skill/rate', SkillRateLogView.as_view()),
    url(r'^user/skill', SetSkillView.as_view()),
    url(r'^get/users', GetUsersView.as_view()),
    url(r'^user', UserView.as_view()),
    url(r'^company/(?P<company_id>\d+)', ManageCompanyView.as_view()),
    url(r'^company', CreateCompanyView.as_view()),
    url(r'^job', CreateJobView.as_view()),
]

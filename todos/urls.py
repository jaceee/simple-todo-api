from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from todos_api import views


router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet, 'todo')

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^auth/login/', obtain_jwt_token),
    url(r'^auth/refresh/', refresh_jwt_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

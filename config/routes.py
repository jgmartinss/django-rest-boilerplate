from rest_framework import routers

from v1.apps.accounts import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

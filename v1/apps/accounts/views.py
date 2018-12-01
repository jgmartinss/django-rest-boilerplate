from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from . import serializer
from . import models


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.UserSerializer
    queryset = models.User.objects.all().order_by('-date_joined')

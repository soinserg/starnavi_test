from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from .models import User
from .serializers import UserSerializer


class UserList(ListCreateAPIView):
    queryset = User.objects.visitors()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.visitors()
    serializer_class = UserSerializer

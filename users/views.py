from rest_framework import viewsets

from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly
from .models import User


# Create your views here.


class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = UserSerializer
    class Meta:
        model = User

    


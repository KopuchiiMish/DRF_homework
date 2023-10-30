from rest_framework.generics import RetrieveAPIView

# Create your views here.
from users.models import User
from users.serializers import UserDetailSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()

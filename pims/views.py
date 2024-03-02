from rest_framework.viewsets import ModelViewSet

from .models import Catagory, ProjectInfo
from .permissions import IsAdminOrReadOnly
from .serializers import CatagorySerializer, ProjectInfoSerializer

# Create your views here.


class CatagoryViewSet(ModelViewSet):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer
    permission_classes = [IsAdminOrReadOnly]


class ProjectInfoViewSet(ModelViewSet):
    queryset = ProjectInfo.objects.all()
    serializer_class = ProjectInfoSerializer
    permission_classes = [IsAdminOrReadOnly]

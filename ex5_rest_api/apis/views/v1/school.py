from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from ...models import School
from ...serializers import SchoolSerializer
from ...filters import SchoolFilter


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SchoolFilter
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.method == 'GET':
            pass
        
        return queryset
        
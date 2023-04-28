from django.shortcuts import render

from rest_framework import generics, viewsets

from apps.team.models import (
    Team, 
    Gallary
)
from apps.team.serializers import (
    TeamSerializer, 
    GallarySerializer
)


class TeamListView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamCreateView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer 


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer  


class GalleryViewSet(viewsets.ModelViewSet):
    serializer_class = GallarySerializer
    queryset = Gallary.objects.all()
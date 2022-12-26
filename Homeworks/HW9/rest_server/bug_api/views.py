from django.shortcuts import render

# Create your views here.

from .models import Bug, Comment
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BugsSerializer, CommentsSerializer


class BugsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Bug.objects.all().order_by('id')
    serializer_class = BugsSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticated]

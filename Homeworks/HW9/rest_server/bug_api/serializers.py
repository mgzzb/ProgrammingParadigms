from .models import Bug, Comment
from rest_framework import serializers


class BugsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bug
        fields = ['id', 'package', 'status', 'version', 'summary']


class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'bug', 'user', 'content']

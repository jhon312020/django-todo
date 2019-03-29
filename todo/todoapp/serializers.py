from rest_framework import serializers
from todoapp.models import Todolist


class TodolistSerializer(serializers.ModelSerializer):

    id = serializers.CharField(source="title.id", read_only=True)
    taskname = serializers.CharField(source='title.taskname', read_only=True)
    status = serializers.CharField(source="title.status", read_only=True)

    class Meta:
        model = Todolist
        fields = ('id', 'taskname', 'status',)



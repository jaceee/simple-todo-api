from rest_framework import serializers

from todos_api.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('url', 'title', 'description', 'done',)

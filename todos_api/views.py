from rest_framework import viewsets

from todos_api.models import Todo
from todos_api.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows To Do's to be viewed or edited.
    """
    serializer_class = TodoSerializer

    def get_queryset(self):
        """
        This view should return a list of all the To Do's
        for the currently authenticated user.
        """
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        This view should add the currently authenticated
        user to the created To Do's.
        """
        serializer.save(user=self.request.user)

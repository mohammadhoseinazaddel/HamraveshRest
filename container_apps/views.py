from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from container_apps.models import ContainerApps, Author
from container_apps.serializers import ContainerAppsSerializer, AuthorSerializer, UserSerializer


class ContainerAppsViewSet(viewsets.ModelViewSet):
    queryset = ContainerApps.objects.all()
    serializer_class = ContainerAppsSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'creat']
    permission_classes = (permissions.IsAuthenticated,)

class AppRunner(viewsets.ModelViewSet):
    queryset = ContainerApps.objects.all()
    serializer_class = ContainerAppsSerializer
    http_method_names = ['post']
    permission_classes = (permissions.IsAuthenticated,)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'creat']

    # overwriting creat permission for Author
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'list']:
            self.permission_classes = [permissions.IsAuthenticated, ]
        elif self.action in ['create']:
            self.permission_classes = [permissions.IsAdminUser, ]
        else:
            self.permission_classes = [permissions.AllowAny, ]
        return super(self.__class__, self).get_permissions()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # overwriting creat permission for usercreation
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'list']:
            self.permission_classes = [permissions.IsAuthenticated, ]
        elif self.action in ['create']:
            self.permission_classes = [permissions.IsAdminUser, ]
        else:
            self.permission_classes = [permissions.AllowAny, ]
        return super(self.__class__, self).get_permissions()

from django.contrib.auth.models import User
from commander import command_utils
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from container_apps.models import ContainerApps, Author
from container_apps.serializers import ContainerAppsSerializer, AuthorSerializer, UserSerializer
import logging

logger = logging.getLogger('hamdocker-view.error_classes')

class ContainerAppsViewSet(viewsets.ModelViewSet):
    queryset = ContainerApps.objects.all()
    serializer_class = ContainerAppsSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = (permissions.IsAuthenticated,)

    @action(detail=False)
    def recent_apps(self, request):
        recent_apps = ContainerApps.objects.all().filter(name=request.data['name'])

        # page = self.paginate_queryset(recent_users)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_apps, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def create_app(self, request):
        app = self.get_object()
        serializer = ContainerAppsSerializer(data=request.data)
        if serializer.is_valid():
            app_name = serializer.validated_data['name']
            environments = serializer.validated_data['name']
            # port = serializer.validated_data['port']
            app.set_vasrs(serializer.validated_data)
            app.save()
            return Response({'status': 'app created use runner to run it'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['patch'])
    def patche():
        pass


    # @list_route()
    # def new_arrivals(self, request):
        # books = self.get_queryset()
        # books = books.filter(when_added__gte=d 
        # serializer = self.get_serializer(books, many=True)
        # return Response(serializer.data)

class AppRunner(viewsets.ModelViewSet):
    queryset = ContainerApps.objects.filter()
    serializer_class = ContainerAppsSerializer
    http_method_names = ['post']
    permission_classes = (permissions.IsAuthenticated,)
    try:
        command_output=command_utils.call_stub("ps -a",by_shell=True, timeout=280)
        logger.info("creating your app finished with ","output%s"%command_output.cout)
    except Exception as e:
        logger.error(msg = e)

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

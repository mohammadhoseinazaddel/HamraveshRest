from container_apps import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#functional 
router.register('runapp_functional', views.docker_apps_runner) # to run docker build command and get status of docker
router.register('apps_functional', views.apps_functions)
#generics #TODO not completed
router.register('apps', views.ContainerAppsViewSet)
router.register('runapps', views.AppRunner)
router.register('author', views.AuthorViewSet)
router.register('user_creation', views.UserViewSet)

urlpatterns = [

]

urlpatterns += router.urls

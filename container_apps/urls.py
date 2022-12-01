from container_apps import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('apps', views.ContainerAppsViewSet)
router.register('runapps', views.AppRunner)
router.register('author', views.AuthorViewSet)
router.register('user_creation', views.UserViewSet)

urlpatterns = [

]

urlpatterns += router.urls

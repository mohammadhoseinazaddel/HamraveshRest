from book import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books', views.BookViewSet)
router.register('author', views.AuthorViewSet)
router.register('user_creation', views.UserViewSet)

urlpatterns = [

]

urlpatterns += router.urls

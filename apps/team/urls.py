from rest_framework.routers import DefaultRouter
from apps.team.views import GalleryViewSet

router = DefaultRouter()
router.register(r'users/', GalleryViewSet, basename='gallery')
urlpatterns = router.urls
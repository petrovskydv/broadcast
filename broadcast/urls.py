from rest_framework.routers import DefaultRouter

from broadcast.views import ClientViewSet, MailingViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'mailings', MailingViewSet)
urlpatterns = router.urls

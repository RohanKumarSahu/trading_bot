from rest_framework import routers
from webhook.viewsets import DataViewSet

router = routers.DefaultRouter()
router.register('data', DataViewSet)
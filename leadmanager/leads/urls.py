from rest_framework import routers
from .api import LeadViewset

router = routers.DefaultRouter()
router.register('api/leads', LeadViewset)

urlpatterns = router.urls

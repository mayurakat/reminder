from rest_framework import routers
from .views import RemindMeLaterViewset


router = routers.DefaultRouter(trailing_slash=False)
router.register('remind-me-later', RemindMeLaterViewset, basename='remindlater')
urlpatterns=router.urls
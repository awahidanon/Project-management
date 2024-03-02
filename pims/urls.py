from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register("catagory", views.CatagoryViewSet, basename="catagory")
router.register("projectinfo", views.ProjectInfoViewSet, basename="project")

urlpatterns = router.urls

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'meal', views.mealViewSet)
router.register(r'food', views.foodViewSet)
router.register(r'chef', views.chefViewSet)
router.register(r'distributor', views.distributorViewSet)
router.register(r'cook', views.cookViewSet)
router.register(r'distribution', views.distributionViewSet)
router.register(r'report', views.reportViewSet)
# router.register(r'test', views.foodTestViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('cook-report/', views.cookReport)
]

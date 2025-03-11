from django.urls import include
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [ include(router.urls)

]
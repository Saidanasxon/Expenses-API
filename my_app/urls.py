from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'my_app'

router = routers.DefaultRouter()
router.register('expenses', views.ExpenseViewSet, basename='expenses')


urlpatterns = [
    path('my_app/', include(router.urls)),
]
from django.urls import path,include
from habit_app.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api',views.HabitApi,basename='api')

urlpatterns = [
    path('',include(router.urls))
]
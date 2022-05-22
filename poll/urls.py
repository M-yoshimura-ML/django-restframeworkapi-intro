from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


router = routers.DefaultRouter()
router.register('poll', views.PollViewSet)

poll_list_view = views.PollViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

urlpatterns = [
    path('', include(router.urls)),
    path('generic/poll/', poll_list_view),
    path('generic/poll/<int:id>', views.PollListView.as_view()),
]


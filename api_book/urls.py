from django.urls import path, include
from . import views
from .views import BulkCreateBookView
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


router = routers.DefaultRouter()
router.register('book', views.BookViewSet)

book_list_view = views.BookViewSet.as_view({
    "get": "list",
    "post": "create",
})

urlpatterns = [
    path('', include(router.urls)),
    # path('book/bulk', BulkCreateBookView.as_view(), name='books'),

    # path('book/', views.book), # function based
    # path('book/', views.BookAPIView.as_view()), # class based

    # path('book/<int:id>', views.book_detail), # function based
    # path('book/<int:id>', views.BookDetailView.as_view()), # class based

    # path('generic/book/', views.BookListView.as_view()),
    path('generic/book/', book_list_view),
    path('generic/book/<int:id>', views.BookListView.as_view()),
]


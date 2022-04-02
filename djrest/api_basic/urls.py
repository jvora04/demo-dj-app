from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('', views.BookModelViewSet, basename = 'book')
# router.register('book/<int:pk>', views.BookViewSet, basename = 'book')
urlpatterns = [
    
    # path('', views.book_list),
    # path('book/<int:pk>/', views.book_detail),
    
    # path('', views.book_list.as_view()),
    # path('book/<int:pk>/', views.book_detail.as_view()),
    
    # path('generic/book/', views.GenericAPIView.as_view()),
    # path('generic/book/<int:pk>/', views.GenericAPIView.as_view()),

    path('', include(router.urls)),
    # path('<int:pk>/', include(router.urls)),
    

]


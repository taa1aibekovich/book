from django.urls import path, include
from .views import *
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r'user', UserProfileViewSet, basename='user-list'),
routers.register(r'hotels', HotelListViewSet, basename='hotel-list'),
routers.register(r'hotels-detail', HotelDetailViewSet, basename='hotel-detail'),
routers.register(r'hotel_photos', HotelPhotosViewSet, basename='hotel_photos-list'),
routers.register(r'room', RoomListViewSet, basename='room-list'),
routers.register(r'room-detail', RoomDetailViewSet, basename='room-detail'),
routers.register(r'room_photos', RoomPhotosViewSet, basename='room_photos-list'),
routers.register(r'booking', BookingViewSet, basename='booking-list'),
routers.register(r'rating', RatingViewSet, basename='rating-list'),

urlpatterns = [
    path('', include(routers.urls)),
    # path('hotels/', HotelListViewSet.as_view(), name='hotels')
]

#     path('', HotelListViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotel_list'),
#     path('<int:pk>/', HotelListViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
#          name='hotel_detail'),
#
#     path('hotelimage/', HotelPhotosViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotelimage_list'),
#     path('hotelimage/<int:pk>/', HotelPhotosViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
#          name='hotelimage_detail'),
#
#     path('room/', RoomListViewSet.as_view({'get': 'list', 'post': 'create'}), name='room_list'),
#     path('room/<int:pk>/', RoomListViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
#          name='room_detail'),
#
#     path('roomimage/', RoomPhotosViewSet.as_view({'get': 'list', 'post': 'create'}), name='roomimage_list'),
#     path('roomimage/<int:pk>/', RoomPhotosViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
#          name='roomimage_detail'),
#
#     path('review/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
#     path('review/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
#          name='review_detail'),
#
#     path('booking/', BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking_list'),
#     path('booking/<int:pk>/', BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
#          name='booking_detail'),
# ]

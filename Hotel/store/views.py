from rest_framework import viewsets, permissions, generics
from .serializer import *
from .models import *
from .permissions import CheckOwner, CheckCRUD, CheckOwnerHotel, CheckRoom, CheckBooking
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import HotelFilter, RoomFilter


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class HotelListViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = HotelFilter
    search_fields = ['hotel_name']
    ordering_fields = ['hotel_stars']
    permission_classes = [CheckCRUD]


class HotelDetailViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer
    permission_classes = [CheckCRUD, CheckOwnerHotel]


class HotelPhotosViewSet(viewsets.ModelViewSet):
    queryset = HotelPhotos.objects.all()
    serializer_class = HotelPhotosSerializer


class RoomListViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = RoomFilter
    search_fields = ['room_number']
    ordering_fields = ['room_price']
    # permission_classes = [permissions.IsAuthenticated,CheckStatus]


class RoomDetailViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer
    permission_classes = [CheckRoom]


class RoomPhotosViewSet(viewsets.ModelViewSet):
    queryset = RoomPhotos.objects.all()
    serializer_class = RoomPhotosSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated, CheckOwner]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [CheckBooking]

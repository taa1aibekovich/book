from django_filters import FilterSet
from .models import Hotel,Room


class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'country':['exact'],
            'city':['exact'],
            'hotel_stars':['gt','lt']
        }


class RoomFilter(FilterSet):
    class Meta:
        model = Room
        fields = {
            'room_type': ['exact'],
            'room_status': ['exact'],
            'all_inclusive': ['exact'],
            'room_price': ['gt', 'lt']
        }
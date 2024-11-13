from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age', 'phone_number', 'status']
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']



class HotelProSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name']


class HotelPhotosSerializer(serializers.ModelSerializer):
    hotel = HotelProSerializer()

    class Meta:
        model = HotelPhotos
        fields = ['hotel', 'image']




class HotelSimplePhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelPhotos
        fields = ['image']


class RoomPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhotos
        fields = '__all__'


class RoomPhotosProSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhotos
        fields = ['room_image']


class RoomDetailSerializer(serializers.ModelSerializer):
    hotel_room = HotelProSerializer()

    class Meta:
        model = Room
        fields = ['id', 'hotel_room', 'rooms_number', 'room_type', 'room_status',
                  'room_price', 'all_inclusive', 'room_description', 'bedroom', 'bathroom', 'person']


class RoomListSerializer(serializers.ModelSerializer):
    room_photos = RoomPhotosProSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['rooms_number', 'room_type', 'room_status',
                  'room_price', 'all_inclusive', 'room_photos']


class RatingSerializer(serializers.ModelSerializer):
    user_name = UserProProfileSerializer()
    date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    hotel = HotelProSerializer()

    class Meta:
        model = Rating
        fields = ['user_name', 'hotel', 'stars', 'parent', 'text', 'date']


class RatingProSerializer(serializers.ModelSerializer):
    user_name = UserProProfileSerializer()
    date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Rating
        fields = ['user_name', 'stars', 'parent', 'text', 'date']


class BookingSerializer(serializers.ModelSerializer):
    user_book = UserProProfileSerializer()
    hotel_book = HotelProSerializer()
    room_book = RoomListSerializer()
    check_in = serializers.DateField(format='%d-%m-%Y')
    check_out = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = Booking
        fields = ['user_book', 'hotel_book', 'room_book', 'check_in',
                  'check_out', 'total_price', 'status_book']


class HotelListSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    hotel_image = HotelSimplePhotosSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    rating = RatingProSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'hotel_description',
                  'hotel_stars', 'address', 'hotel_image', 'create_date','rating','average_rating']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class HotelDetailSerializer(serializers.ModelSerializer):
    owner = UserProProfileSerializer()
    create_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    hotel_image = HotelSimplePhotosSerializer(many=True, read_only=True)
    hotel_rooms = RoomListSerializer(many=True, read_only=True)
    rating = RatingProSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['id', 'owner', 'hotel_name', 'country', 'city', 'hotel_description',
                  'hotel_video', 'hotel_stars', 'create_date', 'address', 'hotel_image',
                  'hotel_rooms', 'rating', 'average_rating']

    def get_average_rating(self, obj):
        return obj.get_average_rating()

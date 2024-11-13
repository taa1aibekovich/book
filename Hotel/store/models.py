from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('simpleUser', 'simpleUser '),
        ('ownerUser', 'ownerUser'),

    )
    status = models.CharField(max_length=32, choices=ROLE_CHOICES, default='simpleUser', null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)],
                                           null=True, blank=True)



class Hotel(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=55)
    country = models.CharField(max_length=32)
    city = models.CharField(max_length=55)
    hotel_description = models.TextField(null=True, blank=True)
    hotel_video = models.FileField(upload_to='hotel_video/', null=True, blank=True)
    hotel_stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    create_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=55)

    def __str__(self):
        return f'{self.hotel_name}-{self.country}-{self.city}'

    def get_average_rating(self):
        rating = self.rating.all()
        if rating.exists():
            return round(sum(rating.stars for rating in rating) / rating.count(), 1)
        return 0


class HotelPhotos(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='hotel_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotel_images/', null=True, blank=True)


class Room(models.Model):
    hotel_room = models.ForeignKey(Hotel, related_name='hotel_rooms', on_delete=models.CASCADE)
    rooms_number = models.PositiveSmallIntegerField(default=1)
    TYPE_CHOICES = (
        ('люкс', 'люкс'),
        ('семейный', 'семейный'),
        ('одноместный', 'одноместный'),
        ('двухместный', 'двухместный'),
    )
    room_type = models.CharField(max_length=32, choices=TYPE_CHOICES)
    STATUS_CHOICES = (
        ('забронирован', 'забронирован'),
        ('Свободен', 'Свободен'),
        ('Занят', 'Занят')
    )
    room_status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='Свободен')
    room_price = models.PositiveIntegerField()
    all_inclusive = models.BooleanField(default=False)
    room_description = models.TextField(null=True, blank=True)
    bedroom = models.IntegerField(default=1)
    bathroom = models.IntegerField(default=1)
    person = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.hotel_room}-{self.rooms_number}-{self.room_type}'


class RoomPhotos(models.Model):
    room = models.ForeignKey(Room, related_name='room_photos', on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to='room_image/', null=True, blank=True)


class Rating(models.Model):
    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, related_name='rating', on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='rating', null=True,
                                blank=True)
    parent = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_name}-{self.hotel}-{self.stars}'


class Booking(models.Model):
    user_book = models.OneToOneField(UserProfile, related_name='bookings', on_delete=models.CASCADE)
    hotel_book = models.ForeignKey(Hotel, related_name='bookings', on_delete=models.CASCADE)
    room_book = models.ForeignKey(Room, related_name='bookings', on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.PositiveIntegerField(default=0)
    STATUS_BOOK_CHOICES = (
        ('отменено', 'отменено'),
        ('подтверждено', 'подтверждено')
    )
    status_book = models.CharField(max_length=32, choices=STATUS_BOOK_CHOICES)

    def __str__(self):
        return f'{self.user_book}-{self.hotel_book}-{self.room_book}-{self.status_book}'

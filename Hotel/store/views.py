from rest_framework import viewsets, permissions, generics
from .serializer import *
from .models import *
from .permissions import CheckOwner, CheckCRUD, CheckOwnerHotel, CheckRoom, CheckBooking
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import HotelFilter, RoomFilter
# import tempfile
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import tempfile

from roboflow import Roboflow


class ImageProductView(APIView):
    rf = Roboflow(api_key="wqtRxJ8JgBgBuPN0BnnO")
    project = rf.workspace().project("numbers-z74nr")
    model = project.version(1).model


from roboflow import Roboflow


class ImageProductView(APIView):
    rf = Roboflow(api_key="wqtRxJ8JgBgBuPN0BnnO")
    project = rf.workspace().project("numbers-z74nr")
    model = project.version(1).model

    def post(self, request):
        # Validate the incoming image file
        serializer = ImageSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Save and process the validated image file using tempfile
        image_file = serializer.validated_data['image']

        # Create a temporary file for storing the image
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            image_path = temp_file.name
            for chunk in image_file.chunks():
                temp_file.write(chunk)

        # Run inference on the saved image
        try:
            prediction = self.model.predict(image_path, confidence=40, overlap=30).json()
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        finally:
            # Clean up the temporary file
            os.remove(image_path)

        # Return the prediction result
        return Response(prediction, status=status.HTTP_200_OK)


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

from rest_framework.permissions import BasePermission
from rest_framework import permissions


class CheckOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'ownerUser':
            return False
        return True


class CheckCRUD(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.status == 'ownerUser'


class CheckOwnerHotel(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class CheckRoom(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.room_status == 'свабоден':
            return True
        return False

class CheckBooking(BasePermission):
    def has_permission(self, request, obj):
        if request.user.status == 'ownerUser':
            return False
        return True

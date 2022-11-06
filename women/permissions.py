from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, requset, view):
        if requset.method in permissions.SAFE_METHODS:
            return True
        return bool(requset.user and requset.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # access for all users
        if request.method in permissions.SAFE_METHODS:
            return True

        # access if user from db is equal user from request
        return obj.user == request.user

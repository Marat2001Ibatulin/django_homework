from rest_framework import permissions


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if obj.draft == "YES":
                return obj.creator == request.user
            return True

        return obj.creator == request.user or request.user.is_staff



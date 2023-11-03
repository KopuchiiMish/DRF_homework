from rest_framework.permissions import BasePermission


class IsNotStaffUser(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_staff
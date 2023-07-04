from rest_framework import permissions

class DoIfOwnerOrRead(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method=='GET':
            return True
        
        if obj.user_name == request.user:
            return True
        else:
            return False
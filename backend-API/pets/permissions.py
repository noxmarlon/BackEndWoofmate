from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Permiso personalizado para permitir solo a los dueños de una mascota actualizarla o eliminarla.
    """

    def has_object_permission(self, request, view, obj):
        # Los permisos solo son otorgados al dueño de la mascota.
        return obj.owner == request.user

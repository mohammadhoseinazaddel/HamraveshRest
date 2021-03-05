# for future features
# from rest_framework import permissions
#
# class NotCreateAndIsAdminUser(permissions.IsAdminUser):
#     def has_permission(self, request, view):
#         return (view.action == 'create'
#                 and super(NotCreateAndIsAdminUser, self).has_permission(request, view))
#
# class NotCreateAndIsAdminUser(permissions.IsAdminUser):
#     def has_permission(self, request, view):
#         return (view.action == 'create'
#                 and super(NotCreateAndIsAdminUser, self).has_permission(request, view))
#
#
# class CreateAndIsAuthenticated(permissions.AllowAny):
#     def has_permission(self, request, view):
#         return (view.action in ['update', 'partial_update', 'destroy', 'list']
#                 and super(CreateAndIsAuthenticated, self).has_permission(request, view))

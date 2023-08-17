# from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token
# from . import views
# from .views import MyTokenObtainPairView

from django.urls import path, re_path
from .views import (
    CustomProviderAuthView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    ProvileView,
    LogoutView
)

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView
# )

urlpatterns = [
    re_path(
        r'^o/(?P<provider>\S+)/$',
        CustomProviderAuthView.as_view(),
        name='provider-auth'
    ),
    path('create/', CustomTokenObtainPairView.as_view()),
    path('refresh/', CustomTokenRefreshView.as_view()),
    path('verify/', CustomTokenVerifyView.as_view()),
    path('logout/', LogoutView.as_view()),
    path("profile/<int:pk>/", ProvileView.as_view(), name="profile_update"),
    path("profile/", ProvileView.as_view(), name="profile_view"),
]
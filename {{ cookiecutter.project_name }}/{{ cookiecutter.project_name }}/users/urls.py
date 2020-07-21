from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
  path('api/v1/signup/', views.UserCreateAPIView.as_view(), name='signup'),
  path('api/v1/profile/', views.ProfileRetrieveAPIView.as_view(), name='profile'),
  path('api/v1/authorize/', views.TokenObtainPairView.as_view(), name='authorize'),
  path('api/v1/token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
  path('api/v1/token/delete/', views.TokenDeleteView, name='token_delete'),
]




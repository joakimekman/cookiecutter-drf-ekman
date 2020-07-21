from django.http import HttpResponse
from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.response import Response  
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class ProfileRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    
    def retrieve(self, request, *args, **kwargs):
        ''' 
        Get user from request.user instead of get_object()
        '''
        instance = request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class TokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        '''
        Store Refresh Token in a httponly cookie instead.
        '''
        response = super().post(request, *args, **kwargs)
        refresh_token = response.data.pop('refresh')
        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            secure=False
        )
        return response


class TokenRefreshView(TokenRefreshView):
    
    def post(self, request, *args, **kwargs):
        ''' 
        Get Refresh Token from cookie, and pass it to the serializer.
        '''
        refresh_token = request.COOKIES['refresh_token']
        request.data['refresh'] = refresh_token

        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            # InvalidToken raises 401 if Refresh Token is invalid
            raise InvalidToken(e.args[0]) 
        
        response = Response(serializer.validated_data, status=status.HTTP_200_OK)
        
        # Move the new Refresh Token to a cookie.
        new_refresh_token = response.data.pop('refresh')
        
        response.set_cookie(
            key="refresh_token",
            value=new_refresh_token,
            httponly=True,
            secure=False
        )

        return response


def TokenDeleteView(request):
    '''
    Simply remove the refresh cookie that is used to get a
    new access token, and thus access to secured endpoints.
    '''
    response = HttpResponse(status=200)
    response.delete_cookie("refresh_token")
    return response
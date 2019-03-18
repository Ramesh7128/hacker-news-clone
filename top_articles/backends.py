import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from .models import User

class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'

    def authenticate(self, request):
        """
        The authenticate method is called for every request.
        """
        request.user = None
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()
        if not auth_header:
            return None
        if len(auth_header) != 2:
            return None
        else:
            prefix =  auth_header[0].decode('utf-8').lower()
            token = auth_header[1].decode('utf-8')
            if prefix != auth_header_prefix:
                return None
            else:
                return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            print(payload)
        except:
            msg = "invalid authentication. could not decode token."
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            msg = "No user matching the token"
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = "User account has been deactivated"
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)
        



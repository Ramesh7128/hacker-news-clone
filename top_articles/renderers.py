import json
from rest_framework.renderers import JSONRenderer

class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    
    def render(self, data, media_type=None, renderer_context=None):
        
        # If the view throw an error with authentication, the data will 
        # have error key so we need to handle this error in default jsonRenderer.
        # errors = data.get('errors', None)

        # if we receive a 'token' key in the response, it will be
        # byte object. Byte object don't serialize well, so we need 
        # decode utf-8 before rendering the User object.

        token = data.get('token', None)

        if token is not None and isinstance(token, bytes):
            data['token'] = token.decode('utf-8')
        
        return json.dumps({
            "user": data
        })
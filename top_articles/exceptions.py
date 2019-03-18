from rest_framework.views import exception_handler

def core_exception_handler(exc, context):

    response = exception_handler(exc, context)

    handlers = {
        'ValidationError': handle_generic_error,
    }

    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response, exception_class)

    return response


def handle_generic_error(exc, context, response, exception_class):
    
    response.data = {
        "error": response.data 
    }
    return response



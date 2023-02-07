def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("before function response")
        response = get_response(request)
        print("After function response")
        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        print("before class response")
        response = self.get_response(request)
        print("After class response")
        # Code to be executed for each request/response after
        # the view is called.

        return response



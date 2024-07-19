from django.http import HttpResponsePermanentRedirect
class SecureRequiredMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if not request.is_secure():
            return HttpResponsePermanentRedirect(f'https://{request.get_host()}{request.get_full_path()}')
            response = self.get_response(request)
            return response 
import re
from django.conf import settings
from django.shortcuts import redirect, reverse
from django.contrib.auth import logout
excluded_urls = []
if hasattr(settings, 'AUTH_EXCLUDED_URL'):
    excluded_urls +=  [re.compile(url) for url in settings.AUTH_EXCLUDED_URL]

print(excluded_urls)

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response;

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        path = request.path_info
        loggedin = request.user.is_authenticated

        excluded_url = any(url.match(path) for url in excluded_urls)
        print(path, loggedin,excluded_url)
        
        # if(loggedin):
        #     if(excluded_url):
        #         return logout(request)
        #     else:
        #         pass
        # else:
        #     if(not excluded_url):
        #         return redirect(reverse('accounts:login'))
 
        if loggedin and excluded_url:
            return logout(request)
        elif not loggedin and not excluded_url:
            return redirect(reverse('accounts:login'))
        else:
            pass
        #if not excluded_url and not loggedin:
            #pass
            

class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response;

    def __call__(self, request):
        response = self.get_response(request)
        return response

    # def process_request(self,request,exception):
    #     print(request.path)

    
    # def process_exception(self, request, exception):
    #     pass
    
    # def process_template_response(self, request, response):
    #     pass
    def process_view(self, request, view_func, view_args, view_kwargs):
       print("LoggerMiddleWare : ",request.path, request.path_info)


    # def process_response(self, request, response):
    #     pass

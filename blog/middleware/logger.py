class MyLogger:
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
       print(request.path, request.path_info)


    # def process_response(self, request, response):
    #     pass

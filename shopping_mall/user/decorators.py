def login_required(function):
    def wrap(request, *args, **kwargs):
        print('login required!')
        return function(request, *args, **kwargs)

    return wrap
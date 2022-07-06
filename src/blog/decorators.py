from django.http import Http404


# simple decorator to check if user is the author for showing delete and edit pages
def user_is_author(function):
    def wrap(request,username,slug):
        if request.user.username == username:
            return function(request,username,slug)
        else:
            raise Http404
    return wrap
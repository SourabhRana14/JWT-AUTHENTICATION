


def IsAuthenticated(request):
    return bool(request.user and request.user.is_authenticated)




def IsAdmin(request):
    return bool(request.user and request.user.is_staff)
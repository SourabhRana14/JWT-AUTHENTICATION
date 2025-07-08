from ninja import NinjaAPI, Router



from .auth import JWTAuth
from .permissions import IsAdmin,IsAuthenticated


# Create your views here.


api = NinjaAPI(auth=JWTAuth())
router = Router()


@router.get("/user-profile")
def user_profile(request):

    if not IsAuthenticated(request):
        return api.create_response(request,{"detail":"Unauthorized"},status=401)
    return {"username":request.user.username,"is_admin":request.user.is_staff}



@router.get("/admin-dashboard")
def admin_dashboard(request):

    if not IsAdmin(request):
        return api.create_response(request,{"detail":"Unauthorized"},status=401)
   

    return {"msg":"Welcome Admin"}


api.add_router("/api",router)
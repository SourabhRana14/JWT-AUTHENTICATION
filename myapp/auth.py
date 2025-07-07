from ninja.security import HttpBearer
from rest_framework_simplejwt.authentication  import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken



class JWTAuth(HttpBearer):

    def authenticate(self,request,token):
        jwt_auth = JWTAuthentication()


        try :

            validate_token = jwt_auth.get_validated_token(token)
            user = jwt_auth.get_user(validate_token)
            return user
        
        except InvalidToken:
            return None
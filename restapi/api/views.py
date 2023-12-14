from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupUserSerializer,LoginUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


#generate token manually
def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return{
        'refresh':str(refresh),
        'access':str(refresh.access_token)
    }


class SignupUser(APIView):
    def post(self,request,format=None):
        data = request.data
        serializer = SignupUserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token =get_token_for_user(user)
        return Response({'token':token,'msg':'Registeration Successful'},status=status.HTTP_201_CREATED)



class UserLogin(APIView):
    def post(self,request):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            token = get_token_for_user(user)
            return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)




        

    
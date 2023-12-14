from rest_framework import serializers
from .models import User


class SignupUserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input-type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ['first_naame','last_name','email','mobile','password','password2']
        extra_kwargs={
      'password':{'write_only':True}
    }

#validate password and confrim password
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError("Password and confrimpassword doesnot match")
        return attrs
    
    def create(self, validated_data):
        return User._create_user(**validated_data)
    


class LoginUserSerializer(serializers.ModelSerializer):
        email = serializers.EmailField(max_length=100)

        class Meta:
            model = User
            fields = ['email','password']
            
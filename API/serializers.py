from rest_framework import serializers
from django.contrib.auth import get_user_model

Account = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True , style = {
        'input_type':'password'
    })

    def create(self, validated_data):
        user = Account.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
        )

        return user

    class Meta:
        model = Account
        fields = ('id', 'email', 'name', 'password',)
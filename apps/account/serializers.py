from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ['pk', 'username', 'password',
                  'first_name', 'last_name',
                  'email', 'city', 'job',
                  'status', 'date_joined']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
            'date_joined': {'read_only': True},
        }

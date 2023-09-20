from rest_framework import serializers
from .models import User, Producer, StoreOwner


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ['id', 'username', "name", 'email', "address", "tin", "type_products", 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        company = Producer(
            username=validated_data['username'],
            name=validated_data['name'],
            email=validated_data['email'],
            role=validated_data['role'],
            address=validated_data['address'],
            tin=validated_data['tin'],
            type_products=validated_data['type_products'],
        )
        company.set_password(validated_data['password'])
        company.save()
        return company


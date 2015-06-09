__all__ = ['UserSerializer', 'EditUserSerializer', 'GroupSerializer']

from django.contrib.auth.models import Group
from extuser.models import ExtUser
from rest_framework import serializers

from helpers import roles


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtUser
        fields = ('first_name', 'last_name', 'email',
                  'date_of_birth', 'age', 'location',
                  'desired_salary', 'register_date',
                  'last_change', 'role', 'is_active',
                  'other', 'password')

    def create(self, validated_data):
        ModelClass = self.Meta.model
        try:
            role = validated_data.get('role')

            if role == roles.ROLE_ADMIN:
                instance = ModelClass.objects.create_superuser(email=validated_data.get('email'),
                                                               date_of_birth=validated_data.get('date_of_birth'),
                                                               location=validated_data.get('location'),
                                                               first_name=validated_data.get('first_name'),
                                                               password=validated_data.get('password'))
            else:
                instance = ModelClass.objects.create_user(email=validated_data.get('email'),
                                                          date_of_birth=validated_data.get('date_of_birth'),
                                                          location=validated_data.get('location'),
                                                          first_name=validated_data.get('first_name'),
                                                          password=validated_data.get('password'),
                                                          last_name=validated_data.get('last_name'),
                                                          age=validated_data.get('age'),
                                                          desired_salary=validated_data.get('desired_salary'),
                                                          other=validated_data.get('other', ""),
                                                          role=validated_data.get('role', roles.ROLE_USER))
        except TypeError as exc:
            msg = (
                'Got a `TypeError` when calling `%s.objects.create_user()`. '
                'This may be because you have a writable field on the '
                'serializer class that is not a valid argument to '
                '`%s.objects.create()`. You may need to make the field '
                'read-only, or override the %s.create() method to handle '
                'this correctly.\nOriginal exception text was: %s.' %
                (
                    ModelClass.__name__,
                    ModelClass.__name__,
                    self.__class__.__name__,
                    exc
                )
            )
            raise TypeError(msg)

        return instance


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name',)


class EditUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=40, required=False)
    last_name = serializers.CharField(max_length=40, required=False)
    email = serializers.EmailField(max_length=40, required=False)
    date_of_birth = serializers.DateField(required=False)
    age = serializers.IntegerField(min_value=1, required=False)
    desired_salary = serializers.IntegerField(min_value=0, required=False)
    location = serializers.CharField(max_length=40, required=False)
    other = serializers.TimeField(required=False)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.age = validated_data.get('age', instance.age)
        instance.desired_salary = validated_data.get('desired_salary', instance.desired_salary)
        instance.location = validated_data.get('location', instance.location)
        instance.other = validated_data.get('other', instance.other)
        instance.save()

        return instance

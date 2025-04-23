from rest_framework import serializers
from apps.users.models import Profile
from apps.users.serializers import UserSerializer

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'created_at']
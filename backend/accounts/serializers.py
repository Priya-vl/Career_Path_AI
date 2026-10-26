from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    current_class = serializers.IntegerField(required=False, min_value=8, max_value=12, allow_null=True)
    state = serializers.CharField(required=False, allow_blank=True)
    board = serializers.CharField(required=False, allow_blank=True)
    role = serializers.ChoiceField(choices=[("student", "Student"), ("parent", "Parent")], required=False, default="student")

    class Meta:
        model = User
        fields = ("username", "email", "password", "first_name", "last_name", "current_class", "state", "board", "role")

    def create(self, validated_data):
        current_class = validated_data.pop("current_class", None)
        state = validated_data.pop("state", "")
        board = validated_data.pop("board", "")
        role = validated_data.pop("role", "student")
        user = User.objects.create_user(**validated_data)
        # Public self-registration is limited to student and parent roles.
        UserProfile.objects.create(user=user, role=role, current_class=current_class if role == "student" else None, state=state, board=board)
        return user

class MeSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="profile.role", read_only=True)
    current_class = serializers.IntegerField(source="profile.current_class", read_only=True)
    state = serializers.CharField(source="profile.state", read_only=True)
    board = serializers.CharField(source="profile.board", read_only=True)
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "role", "current_class", "state", "board")

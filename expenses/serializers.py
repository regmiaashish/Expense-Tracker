from rest_framework import serializers
from .models import ExpenseIncome
from django.contrib.auth.models import User


class ExpenseIncomeSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = ExpenseIncome
        fields = [
            "id",
            "title",
            "description",
            "amount",
            "transaction_type",
            "tax",
            "tax_type",
            "total",
            "created_at",
            "updated_at",
            "user",
        ]
        extra_kwargs = {
            "user": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

    def get_total(self, obj):
        return obj.calculate_total()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user

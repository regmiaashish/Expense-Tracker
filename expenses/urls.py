from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseIncomeViewSet, UserRegistrationView

router = DefaultRouter()
router.register(r"expenses", ExpenseIncomeViewSet, basename="expense-income")

urlpatterns = [
    path("", include(router.urls)),
    path("register/", UserRegistrationView.as_view(), name="user_registration"),
]

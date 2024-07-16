from .serializers import *
from .models import *
from .permissions import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication, BaseAuthentication, SessionAuthentication

class ExpenseViewSet(ModelViewSet):
    serializer_class = ExpenseSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [CustomPermission]

    def get_queryset(self):
        return Expense.objects.filter(user_id=self.request.user.id)

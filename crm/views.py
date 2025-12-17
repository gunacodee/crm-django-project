from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Account
from .serializers import AccountSerializer

@api_view(['POST'])
def create_account(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_accounts(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_account(request, pk):
    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = AccountSerializer(account)
    return Response(serializer.data)

@api_view(['GET'])
def filter_accounts(request):
    industry = request.GET.get("industry")
    owner = request.GET.get("owner")
    queryset = Account.objects.all()
    if industry:
        queryset = queryset.filter(industry=industry)
    if owner:
        queryset = queryset.filter(owner=owner)
    serializer = AccountSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_account(request, pk):
    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = AccountSerializer(account, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_account(request, pk):
    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    account.delete()
    return Response({"message": "Account deleted successfully"})

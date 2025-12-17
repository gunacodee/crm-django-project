from django.urls import path
from . import views

urlpatterns = [
    path('accounts/create/', views.create_account, name='account-create'),
    path('accounts/', views.list_accounts, name='account-list'),
    path('accounts/<int:pk>/', views.get_account, name='account-detail'),
    path('accounts/filter/', views.filter_accounts, name='account-filter'),
    path('accounts/<int:pk>/update/', views.update_account, name='account-update'),
    path('accounts/<int:pk>/delete/', views.delete_account, name='account-delete'),
]

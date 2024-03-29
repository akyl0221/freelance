from django.urls import path

from users import views


urlpatterns = [
    path('sign_up', views.UserCreateView.as_view(), name='sign_up'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('users', views.UserListView.as_view(), name='users'),
    path('users/<int:pk>', views.UserDetailView.as_view(), name='user_detail'),
    path('update_balance', views.TransactionCreateView.as_view(), name='update_balance'),
    path('balance_history', views.BalanceHistoryView.as_view(), name='balance_history'),
]
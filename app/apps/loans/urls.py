from django.urls import path
from apps.loans import views
from apps.loans.views import LoanListView, LoanDeleteView, LoanUpdateView

urlpatterns = [
    path('', views.home, name='home'),
    path('loans/', views.loans, name='loans'),
    path('loans/create/', views.create_loan, name='loans_create'),
    path('loans/<int:loan_id>', views.loan_detail, name='loan_detail'),
    path('loans/<int:loan_id>/delete', views.delete_loan, name='delete_loan'),

    path("loans/list", LoanListView.as_view(), name="loan_list"),
    path("loan/<int:pk>/delete/", LoanDeleteView.as_view(), name="loan_delete"),
    path("loan/<int:pk>/update/", LoanUpdateView.as_view(), name="loan_update"),
]

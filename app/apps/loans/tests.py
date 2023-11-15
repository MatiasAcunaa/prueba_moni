from django.test import TestCase
from apps.loans.models import Loan
from django.urls import reverse
from unittest.mock import patch, MagicMock
from apps.loans.constants import STATUS_ACCEPTED, STATUS_REJECTED


class LoanTestCase(TestCase):
    def setUp(self):
        self.data = {
            'first_name': 'Matias',
            'last_name': 'Acuña',
            'dni': '38123123',
            'email': 'matias@gmail.com',
            'gender': 'M',
            'amount': 1000,
        }
        super().setUp()

    @patch('loans.views.requests.get')
    def test_approve_scoring_in_create_loan(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {'status': 'approve'})
        url = reverse('loans_create')  
        self.client.post(url, self.data)  
        self.assertEqual(Loan.objects.count(), 1) 
        self.assertEqual(Loan.objects.first().status, STATUS_ACCEPTED)


    @patch('loans.views.requests.get')
    def test_reject_scoring_in_create_loan(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {'status': 'rejected'})
        url = reverse('loans_create')
        self.client.post(url, self.data)
        self.assertEqual(Loan.objects.count(), 1)
        self.assertEqual(Loan.objects.first().status, STATUS_REJECTED)

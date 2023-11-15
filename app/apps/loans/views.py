from django.shortcuts import render, redirect, get_object_or_404
from apps.loans.models import Loan
from apps.loans.forms import LoanForm
import requests
from django.contrib.auth.decorators import login_required
from django.conf import settings
from rest_framework import status
from django.views.generic import ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from apps.loans.constants import LOAN_APPROVE, STATUS_ACCEPTED, STATUS_REJECTED
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from serializers import LoanSerializer


def home(request):
    return render(request, 'home.html')


@login_required
def loans(request):
    loans = Loan.objects.all()

    return render(request, 'loans_list.html', {'loans' : loans})


def create_loan(request):
    """
        View for creating a loan application.

        This view handles both GET and POST requests:
        - GET: Renders the 'create_loan.html' template with an empty LoanForm.
        - POST: Processes the LoanForm submitted in the request.
        - Validates the form data.
        - Retrieves additional scoring information from an external API based on the provided DNI.
        - Updates the loan status based on the scoring results (approved or rejected).
        - Saves the loan application in the database.
        - Renders the 'create_loan.html' template with the form and a success/error message.

        Parameters:
        - request (HttpRequest): The HTTP request object.

        Returns:
        - HttpResponse: Rendered HTML response.
    """
    if request.method == 'GET':
        return render(request, 'create_loan.html', {
            'form': LoanForm()
        })
    elif request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():        
            dni = form.cleaned_data.get('dni')
            api_url = '{}{}'.format(settings.URL_LOAD, dni)
            api_headers = {
            'credential': settings.CREDENTIAL
            }
            response = requests.get(api_url, headers=api_headers)
            if response.status_code == status.HTTP_200_OK:
                scoring_data = response.json()
                loan_state = scoring_data.get('status', False)
                new_loan = form.save(commit=False)

                if loan_state == LOAN_APPROVE:
                    new_loan.status = STATUS_ACCEPTED
                    message = 'El prestamo se creo con exito'

                else:
                    new_loan.status = STATUS_REJECTED
                    message = 'El usuario no es apto para el prestamo'

                new_loan = form.save(commit=False)
                new_loan.save()
                return render(request, 'create_loan.html', {
                    'form': form,
                    'error': message
                })
            else:
                return render(request, 'create_loan.html', {
                    'form': form,
                    'error': 'Error al consultar la API de scoring.'
                })
        else:
            return render(request, 'create_loan.html', {
                'form': form,
                'error': 'Por favor proporciona un dato válido'
            })


def loan_detail(request, loan_id):
    if request.method == 'GET':
        loan = get_object_or_404(Loan, pk=loan_id, loan_profile=request.user)
        form = LoanForm(instance=loan)
        return render(request, 'loan_detail.html', {'loan': loan, 'form': form})
    else:
        try:
            loan = get_object_or_404(Loan, pk=loan_id, loan_profile=request.user)
            form = LoanForm(request.POST, instance=loan)
            form.save()
            return redirect('loans')
        except ValueError:
            return render(request, 'loan_detail.html', {'loan': loan, 'form': form,
            'error' : "Error al actualizar el prestamo"})


def delete_loan(request, loan_id):
    loan = get_object_or_404(Loan, pk=loan_id, loan_profile=request.user)
    if request.method == 'POST':
        loan.delete()
        return redirect('loans')
    
@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class LoanListView(ListView):
    model = Loan
    template_name = "loan_list.html"
    context_object_name = "loans"

class LoanDeleteView(DeleteView):
    model = Loan
    template_name = "loan_delete.html"
    success_url = reverse_lazy("loan_list")

class LoanUpdateView(UpdateView):
    model = Loan
    template_name = "loan_update.html"
    form_class = LoanForm
    success_url = reverse_lazy("loan_list")

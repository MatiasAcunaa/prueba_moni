from rest_framework import serializers
from apps.loans.models import Loan

"""
Serializer for the Loan model. Defines how to convert Loan model instances to JSON and vice versa.
It includes the specified fields in the serialized output and marks certain fields as read-only,
indicating that they should not be modified during deserialization (e.g., during object creation or update).
The read-only fields 'status' and 'created_at' are automatically managed and should not be provided in write requests.
"""

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('id', 'dni', 'first_name','last_name','gender','email','amount', 'status', 'created_at', 'loan_profile')
        read_only_fields = ('status', 'created_at',)

from django.db import models
from apps.loans.constants import GENDER_CHOICES, STATUS_CHOICES
from django.core.validators import RegexValidator

dni_validator = RegexValidator(
    regex=r"^\d{8}$",
    message="El DNI debe contener 8 dígitos numéricos.",
)

class Loan(models.Model):
    """
        Model representing a loan application.

        Base model for other models in the project, providing common attributes:
            + dni (IntegerField): Unique identifier for the loan applicant (validated using dni_validator).
            + first_name (CharField): First name of the loan applicant.
            + last_name (CharField): Last name of the loan applicant.
            + gender (CharField): Gender of the loan applicant (choices defined in GENDER_CHOICES).
            + email (EmailField): Email address of the loan applicant.
            + amount (DecimalField): Amount requested in the loan application.
            + created_at (DateTimeField): Timestamp indicating when the loan application was created.
            + status (IntegerField): Status of the loan application (choices defined in STATUS_CHOICES).

        Methods:
            + __str__: String representation of the loan, showing DNI and full name.
            + status_display: Human-readable display of the loan status.

        Meta:
            + app_label: Specifies the app label for the model (loans).
    """
    dni = models.IntegerField(
        validators=[dni_validator],
        null=False,
        blank=False,
        db_index=True,
        unique=True,
    )
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=False, blank=False
    )
    email = models.EmailField(null=False, blank=False)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES)
    
    class Meta:
        app_label = 'loans'

    def __str__(self):
        return f"{self.dni}-{self.first_name} {self.last_name}"
    
    def status_display(self):
        for value, label in STATUS_CHOICES:
            if value == self.status:
                return label



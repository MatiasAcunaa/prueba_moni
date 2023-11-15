STATUS_WAITING = 0
STATUS_ACCEPTED = 1
STATUS_REJECTED = 2
STATUS_ERROR = 3

STATUS_CHOICES = (
    (STATUS_WAITING, 'En espera'),
    (STATUS_ACCEPTED, 'Aceptado'),
    (STATUS_REJECTED, 'Rechazado'),
    (STATUS_ERROR, 'Error'),
)

GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
]

LOAN_APPROVE = 'approve'

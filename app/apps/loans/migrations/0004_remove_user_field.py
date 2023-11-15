from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0003_alter_loan_dni_alter_loan_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='loan_profile',
        ),
    ]
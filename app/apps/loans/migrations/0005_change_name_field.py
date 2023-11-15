from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0004_remove_user_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='monto',
            new_name='amount',
        ),
    ]
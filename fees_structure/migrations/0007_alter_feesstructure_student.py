# Generated by Django 4.1 on 2023-11-04 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mkuapi', '0004_alter_student_regno'),
        ('fees_structure', '0006_feesstructure_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feesstructure',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mkuapi.student'),
        ),
    ]

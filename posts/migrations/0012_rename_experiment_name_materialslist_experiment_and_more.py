# Generated by Django 4.1 on 2022-09-04 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_alter_experiment_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materialslist',
            old_name='experiment_name',
            new_name='experiment',
        ),
        migrations.RenameField(
            model_name='procedure',
            old_name='experiment_name',
            new_name='experiment',
        ),
        migrations.AlterField(
            model_name='experiment',
            name='subject',
            field=models.CharField(choices=[('P', 'Physics'), ('C', 'Chemistry'), ('B', 'Biology'), ('GS', 'Gneral Science')], max_length=100, null=True),
        ),
    ]

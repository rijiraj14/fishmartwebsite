# Generated by Django 3.2.8 on 2022-03-08 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('martapp', '0002_rename_email_contactdb_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='registerdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200, null=True)),
                ('lastname', models.EmailField(max_length=200, null=True)),
                ('phonenumber', models.IntegerField(null=True)),
                ('username', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='contactdb',
            old_name='Message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='contactdb',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contactdb',
            old_name='Phone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='contactdb',
            old_name='Subject',
            new_name='subject',
        ),
    ]

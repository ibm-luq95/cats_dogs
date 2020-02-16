# Generated by Django 3.0.3 on 2020-02-15 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('avatar', models.ImageField(upload_to='avatars/')),
                ('typed', models.CharField(choices=[('C', 'Cats'), ('D', 'Dogs')], max_length=5)),
            ],
        ),
    ]

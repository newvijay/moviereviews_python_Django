# Generated by Django 3.0.2 on 2020-01-05 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(max_length=500)),
                ('movierating', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
    ]

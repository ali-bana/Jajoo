# Generated by Django 2.1.5 on 2019-02-02 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=models.BooleanField(null=True), null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_host',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='national_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='national_id_card',
            field=models.ImageField(blank=models.BooleanField(null=True), null=True, upload_to=''),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-27 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=20, null=True)),
                ('user_name', models.CharField(blank=True, max_length=20, null=True)),
                ('category_L', models.CharField(blank=True, max_length=20, null=True)),
                ('category_M', models.CharField(blank=True, max_length=20, null=True)),
                ('category_S', models.CharField(blank=True, max_length=20, null=True)),
                ('financial_statement', models.CharField(blank=True, max_length=20, null=True)),
                ('note', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(blank=True, max_length=20, null=True)),
                ('product_name', models.CharField(blank=True, max_length=20, null=True)),
                ('package_unit', models.CharField(blank=True, max_length=20, null=True)),
                ('pharmacist', models.CharField(blank=True, max_length=20, null=True)),
                ('insurance_code', models.CharField(blank=True, max_length=20, null=True)),
                ('standard_code', models.CharField(blank=True, max_length=20, null=True)),
                ('base_price', models.CharField(blank=True, max_length=20, null=True)),
                ('pay', models.CharField(blank=True, max_length=20, null=True)),
                ('division', models.CharField(blank=True, max_length=20, null=True)),
                ('ingredient_code', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
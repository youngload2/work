from django.db import models

# Create your models here.

class Coa(models.Model):
    code = models.CharField(max_length=20, null=True, blank=True)
    user_name = models.CharField(max_length=20, null=True, blank=True)
    category_L = models.CharField(max_length=20, null=True, blank=True)
    category_M = models.CharField(max_length=20, null=True, blank=True)
    category_S = models.CharField(max_length=20, null=True, blank=True)
    financial_statement = models.CharField(max_length=20, null=True, blank=True) 
    note = models.CharField(max_length=20, null=True, blank=True)

    def get_coa_url(self):
        return f'/coa/{self.pk}'


class Product(models.Model):
    product_code = models.CharField(max_length=20, null=True, blank=True)
    product_name = models.CharField(max_length=20, null=True, blank=True)
    package_unit = models.CharField(max_length=20, null=True, blank=True)
    pharmacist = models.CharField(max_length=20, null=True, blank=True)
    insurance_code = models.CharField(max_length=20, null=True, blank=True)
    standard_code = models.CharField(max_length=20, null=True, blank=True)
    base_price = models.CharField(max_length=20, null=True, blank=True)
    pay = models.CharField(max_length=20, null=True, blank=True)
    division = models.CharField(max_length=20, null=True, blank=True)
    ingredient_code = models.CharField(max_length=20, null=True, blank=True)

    def get_product_url(self):
        return f'/product/{self.pk}'
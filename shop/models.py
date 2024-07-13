from django.db import models


# Create your models here.

class Product(models.Model):
    product_id = models.AutoField  # Autofield automatically increments integer value
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=5000)  # Discription
    pub_date = models.DateField()  # Date of Publication
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name  # shows the name of product on my admin page


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)  # Autofield automatically increments integer value
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=13 , default='')
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=150)

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default='')
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+' ...'
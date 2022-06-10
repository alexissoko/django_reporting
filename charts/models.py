from django.db import models

# Create your models here.
class Input(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField(null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    price=models.IntegerField()
    
    def __str__(self) -> str:
        return self.name

# Create your models here.
class SubProduct(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField(null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    price=models.ForeignKey(Input, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
    

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField(null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    price=models.ForeignKey(SubProduct, on_delete=models.CASCADE, blank=True, null=True)
    report = models.BooleanField(default=False)

    
    def __str__(self) -> str:
        return self.name
    
# Create your models here.
class Provider(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField(null=True, blank=True)
    description=models.TextField()
    
    def __str__(self) -> str:
        return self.name

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField(null=True, blank=True)
    description=models.TextField()
    
    def __str__(self) -> str:
        return self.name
    

# Create your models here.
class Sale(models.Model):
    invoice=models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer=models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    date=models.DateField(null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    payment=models.CharField(max_length=100, null=True, blank=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    
    
    def __str__(self) -> str:
        return self.invoice.name
    

# Create your models here.
class Purchase(models.Model):
    invoice=models.ForeignKey(Input, on_delete=models.CASCADE)
    seller=models.ForeignKey(Provider, on_delete=models.CASCADE, blank=True, null=True)
    date=models.DateField(null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    payment=models.CharField(max_length=100, null=True, blank=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    
    def __str__(self) -> str:
        return self.invoice.name

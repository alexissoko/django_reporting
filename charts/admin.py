from django.contrib import admin
from.models import *


# Register your models here.
admin.site.register(Input)
admin.site.register(SubProduct)
admin.site.register(Product)
admin.site.register(Provider)
admin.site.register(Customer)
admin.site.register(Sale)
admin.site.register(Purchase)
admin.site.site_header = 'Pedidos'
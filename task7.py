from unicodedata import name
from kodecamp.models import Product

#Insert a new record into the Product Model

sneakers = Product(
    name='Michael Jordan Sneakers Limted Version',
    price=100,
    description = 'A shoe specifically designed for all your needs!'
    )
sneakers.save()



#Get all the records in the Product table

allProducts = Product.objects.all()



#Filter products by their name

productName = Product.objects.order_by(name)



#Get a single record from the product table

specificProduct = Product.objects.filter(name__contains="Apple Cidar")



#Change a product price

productPriceChange = Product.objects.get(pk=1)
productPriceChange.price = 150
productPriceChange.save()
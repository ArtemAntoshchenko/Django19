from django.shortcuts import render, HttpResponse
from .models import Product, Store, Metadata
from django.db.models import Avg, Min, Max, Sum

def index(request):
    bulk_store=[
        Store(name='Супермаркет'),
        Store(name='Продуктовый'),
        Store(name='Строительный'),
    ]
    bulk_product=[
        Product(name='Хлеб'),
        Product(name='Сыр'),
        Product(name='Гвозди'),
        Product(name='Шоколад'),
        Product(name='Молоко'),
        Product(name='Вода'),
        Product(name='Мясо'),
        Product(name='Кофе'),

    ]
    # delete=Store.objects.all().delete()
    # supermarkets=Store.objects.bulk_create(bulk_store)
    # products=Product.objects.bulk_create(bulk_product)

    bread=Product.objects.get(name='Хлеб')
    chees=Product.objects.get(name='Сыр')
    nails=Product.objects.get(name='Гвозди')
    chocolate=Product.objects.get(name='Шоколад')
    milk=Product.objects.get(name='Молоко')
    water=Product.objects.get(name='Вода')
    coffee=Product.objects.get(name='Кофе')
    meat=Product.objects.get(name='Мясо')

    supermarket=Store.objects.get(name='Супермаркет')
    productoviy=Store.objects.get(name='Продуктовый')
    stroitelniy=Store.objects.get(name='Строительный')

    # supermarket.products.add(bread,chees,nails,chocolate,milk,water,coffee,meat)
    # productoviy.products.add(bread,chees,chocolate,milk,water,meat)
    # stroitelniy.products.add(nails)

    # milk_stores=milk.store_set.all()
    # for i in milk_stores:
    #     print(i.name)

    # chees_stores=chees.store_set.all()
    # for i in chees_stores:
    #     print(i.name)

    # delete_all=supermarket.products.clear()

    # chocolate_stores=chocolate.store_set.all().filter(name='Шоколад')
    # print(chocolate_stores)
    # # for i in chocolate_stores:
    # #     i.objects.filter(name='Шоколад').delete()
    # chocolate_stores=Store.objects.all()
    # for i in chocolate_stores:
    #     i.products.remove(chocolate)


    # supermarket.products.add(bread, through_defaults={'quantity':10, 'price':90})
    # supermarket.products.add(chees, through_defaults={'quantity':10, 'price':140})
    # supermarket.products.add(nails, through_defaults={'quantity':100, 'price':40})
    # supermarket.products.add(chocolate, through_defaults={'quantity':15, 'price':110})
    # supermarket.products.add(milk, through_defaults={'quantity':10, 'price':100})
    # supermarket.products.add(water, through_defaults={'quantity':20, 'price':50})
    # supermarket.products.add(coffee, through_defaults={'quantity':5, 'price':250})
    # supermarket.products.add(meat, through_defaults={'quantity':16, 'price':200})
    # productoviy.products.add(bread, through_defaults={'quantity':12, 'price':95})
    # productoviy.products.add(chees, through_defaults={'quantity':12, 'price':95})
    # productoviy.products.add(bread, through_defaults={'quantity':15, 'price':75})
    # productoviy.products.add(chocolate, through_defaults={'quantity':5, 'price':210})
    # productoviy.products.add(milk, through_defaults={'quantity':8, 'price':120})
    # productoviy.products.add(water, through_defaults={'quantity':17, 'price':45})
    # productoviy.products.add(meat, through_defaults={'quantity':14, 'price':225})
    # stroitelniy.products.add(nails, through_defaults={'quantity':1000, 'price':25})

    # apple=Product.objects.create(name='Яблоко')
    # farm=Store.objects.create(name='Фермерский')
    # apple_farm=Metadata(store=farm, product=apple, quantity=100, price=45)
    # apple_farm.save()

    coffee_price_up=coffee.store_set.all()
    for i in coffee_price_up:
        i.metadata__price*1,1
        i.update()
    water_count=water.store_set.all().aggregate(Sum('metadata__quantity'))
    print(water_count)

    meat_search=meat.store_set.all().filter(metadata__price__lt=210, metadata__quantity__gt=10)
    for i in meat_search:
        print(i.name)
    return HttpResponse()


from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2023-06-27

time = datetime.now()
print(time)  # 2023-06-27 14:51:01.953234

print(type(time))  # <class 'datetime.datetime'>
#
tomorrow = today + timedelta(days=1)
print(tomorrow)

print(time.hour)
print(today.day)

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': tomorrow, 'price': 50.0},
    {'sku': 3, 'exp_date': today, 'price': 20},
]

print(products)

for product in products:
    print(product)
    if product['exp_date'] != today:
        continue  # wraca na początek pętli

    product['price'] *= 0.8
    print(f"""
    Price for sku={product['sku']}
    is now {product['price']}""")

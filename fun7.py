# argumenty słownikowe
def connect(**kwargs):
    print(kwargs)
    print(type(kwargs))  # <class 'dict'>

    connect_param = {
        'host': '127.0.0.1',
        'port': '8080'
    }
    print(connect_param)  # {'host': '127.0.0.1', 'port': '8080'}
    connect_param['pwd'] = kwargs
    print(connect_param)


connect(a=5)
# {'a': 5}
connect(user="root")  # {'user': 'root'}
connect(user="root", b=7)  # {'user': 'root'}
# {'host': '127.0.0.1', 'port': '8080', 'pwd': {'user': 'root', 'b': 7}}
#

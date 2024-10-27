from pprint import pprint


def introspection_info(obj):
    if hasattr(obj, '__name__'):
        print(f'Имя: {obj.__name__}')
    if hasattr(obj, '__class__'):
        print(f'Класс: {obj.__class__.__name__}')
    print(f'Тип: {type(obj)}')
    print(f'Значение: {repr(obj)}')
    if callable(obj):
        print('Можно вызвать')
    else:
        print('Нельзя вызвать')
    print('Атрибуты объекта:')
    pprint(dir(obj))


introspection_info(introspection_info)

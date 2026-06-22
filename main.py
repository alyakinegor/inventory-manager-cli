from crud import (create_category, 
                  get_all_categories, 
                  create_supplier,
                  get_all_suppliers,
                  deactivate_sipplier,
                  create_product,
                  get_all_products,
                  get_product_via_id,
                  change_purchase_price, 
                  change_selling_price,
                  deactivate_product,
                  create_movement,
                  get_all_movements,
                  get_movements_by_product_id)

from reports import (
    get_quality_by_product,
    running_out_products,
    total_purchase_sum,
    total_revenue,
    total_selling_price,
    get_count_products_by_category,
    get_count_products_by_supplier

)

while True:
    print("""Inventory Manager CLI

1. Создать категорию
2. Показать все категории

3. Создать поставщика
4. Показать всех поставщиков
5. Деактивировать поставщика

6. Создать товар
7. Показать все товары
8. Показать товар по id
9. Обновить закупочную цену товара
10. Обновить продажную цену товара
11. Деактивировать товар

12. Добавить поступление товара
13. Добавить списание товара
14. Добавить корректировку остатка

15. Показать историю операций
16. Показать операции по товару
          
17. Показать текущие остатки
18. Показать товары, которые заканчиваются
19. Показать общую стоимость склада
20. Показать товары по категориям
21. Показать товары по поставщикам

0. Выход""")
    ch = input()
    if ch == '1':
        id = int(input('Введите id категории: '))
        name = input('Введите name категории: ')
        create_category(id, name)
    if ch == '2':
        for el in get_all_categories():
            print(el)
    if ch == '3':
        id = int(input('Введите id поставщика: '))
        name = input('Введите name поставщика: ')
        phone = input('Введите phone поставщика: ')
        email = input('Введите email поставщика: ')
        create_supplier(id, name, phone, email)
    if ch == '4':
        for el in get_all_suppliers():
            print(el)
    if ch == '5':
        id = int(input('Введите id поставщика: '))
        deactivate_sipplier(id)
    if ch == '6':
        id = int(input('Введите id товара: '))
        name = input('Введите name товара: ')
        sku = input('Введите sku товара: ')
        cat_id = int(input('Введите category_id товара: '))
        sup_id = int(input('Введите supplier_id товара: '))
        purchase_price = int(input('Введите purchase_price товара: '))
        selling_price = int(input('Введите selling_price товара: '))
        min_qua = int(input('Введите min_quality товара: '))
        create_product(id, name, sku, cat_id, sup_id, purchase_price, selling_price, min_qua)
    if ch == '7':
        for el in get_all_products():
            print(el)
    if ch == '8':
        id = int(input('Введите id товара: '))
        print(get_product_via_id(id))
    if ch == '9':
        id = input('Введите id товара: ')
        price = input('Введите price товара: ')
        change_purchase_price(id, price)
    if ch == '10':
        id = input('Введите id товара: ')
        price = input('Введите price товара: ')
        change_selling_price(id, price)
    if ch == '11':
        id = input('Введите id товара: ')
        deactivate_product(id)
    if ch == '12':
        id = input('Введите id операции: ')
        pr_id = input('Введите id товара: ')
        qua = input('Введите quantity товара: ')
        coment = input('Введите coment к операции: ')
        create_movement(id, pr_id, 'IN', qua, coment)
    if ch == '13':
        id = input('Введите id операции: ')
        pr_id = input('Введите id товара: ')
        qua = input('Введите quantity товара: ')
        coment = input('Введите coment к операции: ')
        create_movement(id, pr_id, 'OUT', qua, coment)
    if ch =='14':
        id = input('Введите id операции: ')
        pr_id = input('Введите id товара: ')
        qua = input('Введите quantity товара: ')
        coment = input('Введите coment к операции: ')
        create_movement(id, pr_id, 'ADJUST', qua, coment)
    if ch == '15':
        for el in get_all_movements():
            print(el)
    if ch == '16':
        id = input('Введите id товара: ')
        for el in get_movements_by_product_id(id):
            print(el)
    if ch == '17':
        get_quality_by_product()
    if ch == '18':
        running_out_products()
    if ch == '19':
        print('Сумма закупочных цен: ')
        total_purchase_sum()
        print()
        print('Сумма продажных цен: ')
        print('Выручка: ')
        total_revenue()
    if ch == '20':
        get_count_products_by_category()
    if ch == '21':
        get_count_products_by_supplier()
    
    if ch == '0':
        break














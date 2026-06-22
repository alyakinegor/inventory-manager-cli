from crud import create_category, create_supplier, create_product, create_movement

create_category(1, 'Electronics')
create_category(2, 'Furniture')
create_category(3, 'Office Supplies')
create_category(4, 'Tools')

create_supplier(1, 'TechTrade', '+7 900 400-30-40', 'email@TechTrade')
create_supplier(2, 'OfficeMarket', '+7 960 500-10-10', 'email@OfficeMarket')
create_supplier(3, 'WoodFactory', '+7 965 333-16-18', 'email@WoodFactory')
create_supplier(4, 'GlobalTools', '+7 980 800-60-80', 'email@GlobalTools')

create_product(1, 'Laptop Lenovo ThinkPad', 'GOOD-100', 1, 1, 1500, 2700, 4)
create_product(2, 'Wireless Mouse', 'GOOD-110', 1, 1, 700, 1000, 10)
create_product(3, 'Office Chair', 'GOOD-120', 2, 2, 5000, 7400, 5)
create_product(4, 'A4 Paper Pack', 'GOOD-130', 3, 3, 2000, 2500, 3)
create_product(5, 'Screwdriver Set', 'GOOD-140', 4, 4, 800, 1200, 6)
create_product(6, 'Monitor 27 inch', 'GOOD-150', 1, 1, 3000, 3500, 2)

create_movement(1, 1, 'IN', 10, 'поступление 10 ноутбуков')
create_movement(2, 2, 'IN', 30, 'поступление 30 мышек')
create_movement(3, 3, 'IN', 15, 'поступление 15 офисных кресел')
create_movement(4, 4, 'IN', 200, 'поступление 200 пачек бумаги')
create_movement(5, 5, 'IN', 25, 'поступление 25 наборов отверток')
create_movement(6, 1, 'OUT', 2, 'списание 2 ноутбуков')
create_movement(7, 2, 'OUT', 5, 'списание 5 мышек')
create_movement(8, 4, 'OUT', 80, 'списание 80 пачек бумаги')
create_movement(9, 3, 'ADJUST', 1, 'корректировка 1 офисного кресла')


print('Данные загружены!')
















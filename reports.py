from models import Stock_movement, Product, Category, Supplier
from sqlalchemy import func, select
from database import sesion_local


def calculate_remains(product_id):
    with sesion_local() as s:
        stmt_in = select(func.sum(Stock_movement.quantity)).where(Stock_movement.product_id == product_id, Stock_movement.movement_type=='IN')
        stmt_out = select(func.sum(Stock_movement.quantity)).where(Stock_movement.id == product_id, Stock_movement.movement_type=='OUT')
        stmt_adjust = select(func.sum(Stock_movement.quantity)).where(Stock_movement.id == product_id, Stock_movement.movement_type=='ADJUST')
        q_in = s.execute(stmt_in).scalar()
        q_out = s.execute(stmt_out).scalar()
        q_adjust = s.execute(stmt_adjust).scalar()

        return q_in + q_adjust - q_out
    
def get_products_with_category_and_supplier():
    with sesion_local() as s:
        stmt = select(Product.id, Product.name, Product.sku, Category.name, Supplier.name, 
                      Product.purchase_price, Product.selling_price, Product.is_active).join(Category, Category.id == Product.id).join(Supplier, Supplier.id == Product.supplier_id)
        arrs = s.execute(stmt).scalars().all()
        for arr in arrs:
            print(' | '.join(arr))
    
def get_movements_with_product():
    with sesion_local() as s:
        stmt = select(Stock_movement.created_at, Product.name, Product.sku, Stock_movement.movement_type, Stock_movement.quantity, Stock_movement.coment).join(Product, Product.id == Stock_movement.product_id)
        arrs = s.execute(stmt).scalars().all()
        for arr in arrs:
            print(' | '.join(arr))
        
def get_products_by_category_id(category_id):
    with sesion_local() as s:
        stmt = select(Product.name).join(Category, Category.id==Product.category_id).where(Category.id == category_id)
        res = s.execute(stmt).scalars().all()
        return res

def get_products_by_supplier_id(sup_id):
    with sesion_local() as s:
        stmt = select(Product.name).join(Supplier, Supplier.id==Product.supplier_id).where(Supplier.id == sup_id)
        res = s.execute(stmt).scalars().all()
        return res

def get_movements_by_product_id(product_id):
    with sesion_local() as s:
        stmt = select(Stock_movement).where(Stock_movement.product_id == product_id)
        res = s.execute(stmt).scalars().all()
        return res

def get_count_products_by_category():
    with sesion_local() as s:
        stmt = select(Category.name, func.count()).join(Product, Product.category_id == Category.id).group_by(Category.name)
        res = s.execute(stmt).scalars().all()
        for el in res:
            print(el[0], ' : ', el[1])
        
def get_count_products_by_supplier():
    with sesion_local() as s:
        stmt = select(Supplier.name, func.count()).join(Product, Product.supplier_id == Supplier.id).group_by(Supplier.name)
        res = s.execute(stmt).scalars().all()
        for el in res:
            print(el[0], ' : ', el[1])

def get_quality_by_product():
    with sesion_local() as s:
        stmt = select(Product.name, calculate_remains(Product.id))
        res = s.execute(stmt).scalars().all()
        for el in res:
            print(el[0], ' : ', el[1])

def running_out_products():
    with sesion_local() as s:
        stmt = select(Product.name, calculate_remains(Product.id), Product.min_quantity).where(calculate_remains(Product.id)<= Product.min_quantity)
        res = s.execute(stmt).scalars().all()
        for el in res:
            print(f'{el[0]}\nОстаток: {el[1]}\n Минимальный остаток: {el[2]}')

running_out_products()
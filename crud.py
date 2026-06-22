from database import sesion_local
from models import Category, Product, Stock_movement, Supplier
from datetime import date
from sqlalchemy import select, update, delete

def create_category(id: int, name: str):
    with sesion_local() as s:
        category = Category(id=id, name=name)
        s.add(category)
        s.commit()
        s.refresh(category)
        return category

def create_supplier(id: int, name: str, phone: str, email: str):
    with sesion_local() as s:
        supplier = Supplier(id=id, name=name, phone=phone, email=email)
        s.add(supplier)
        s.commit()
        s.refresh(supplier)
        return supplier

def create_product(id, name, sku, cat_id, sup_id, purchase_price, selling_price, min_qua):
    with sesion_local() as s:
        pr = Product(id=id, name=name, sku=sku, category_id=cat_id, supplier_id=sup_id, 
                     purchase_price=purchase_price, selling_price=selling_price, min_quantity=min_qua)
        s.add(pr)
        s.commit()
        s.refresh(pr)
        return pr
    
def create_movement(id, product_id, movement_type, quantity, coment):
    with sesion_local() as s:
        mv = Stock_movement(id=id, product_id=product_id, movement_type=movement_type, quantity=quantity, coment=coment)
        s.add(mv)
        s.commit()
        s.refresh(mv)
        return mv
    
def get_all_categories():
    with sesion_local() as s:
        stmt = select(Category)
        cats = s.execute(stmt).scalars().all()
        return cats
    

def get_all_suppliers():
    with sesion_local() as s:
        stmt = select(Supplier)
        sups = s.execute(stmt).scalars().all()
        return sups
    
def get_all_products():
    with sesion_local() as s:
        stmt = select(Product)
        prods = s.execute(stmt).scalars().all()
        return prods
    
def get_product_via_id(id):
    with sesion_local() as s:
        stmt = select(Product).where(Product.id == id)
        product = s.execute(stmt).scalars().all()
        return product
    
def get_product_via_category_id(category_id):
    with sesion_local() as s:
        stmt = select(Product).where(Product.category_id == category_id)
        product = s.execute(stmt).scalars().all()
        return product

    
def get_product_via_supplier_id(supplier_id):
    with sesion_local() as s:
        stmt = select(Product).where(Product.supplier_id == supplier_id)
        product = s.execute(stmt).scalars().all()
        return product

def get_all_movements():
    with sesion_local() as s:
        stmt = select(Stock_movement)
        res = s.execute(stmt).scalars().all()
        return res
    
def get_movements_by_product_id(product_id):
    with sesion_local() as s:
        stmt = select(Stock_movement).where(Stock_movement.product_id == product_id)
        res = s.execute(stmt).scalars().all()
        return res
    
def change_category_name(category_id, new_name):
    with sesion_local() as s:
        stmt = update(Category).where(Category.id == category_id).values(name=new_name)
        s.execute(stmt)
        s.commit()
        return True
    
def change_supplier_contacts(sup_id, new_phone, new_email):
    with sesion_local() as s:
        stmt = update(Supplier).where(Supplier.id == sup_id).values(phone=new_phone, email=new_email)
        s.execute(stmt)
        s.commit()
        return True

def change_purchase_price(product_id, new_price):
    with sesion_local() as s:
        stmt = update(Product).where(Product.id==product_id).values(purchase_price=new_price)
        s.execute(stmt)
        s.commit()
        return True
    
def change_selling_price(product_id, new_price):
    with sesion_local() as s:
        stmt = update(Product).where(Product.id==product_id).values(selling_price=new_price)
        s.execute(stmt)
        s.commit()
        return True
    
def change_min_quantity(product_id, new_quantity):
    with sesion_local() as s:
        stmt = update(Product).where(Product.id == product_id).values(min_quantity=new_quantity)
        s.execute(stmt)
        s.commit()
        return True

def deactivate_product(product_id):
    with sesion_local() as s:
        stmt = update(Product).where(Product.id == product_id).values(is_active=False)
        s.execute(stmt)
        s.commit()
        return True
    
def deactivate_sipplier(sup_id):
    with sesion_local() as s:
        stmt = update(Supplier).where(Supplier.id == sup_id).values(is_active=False)
        s.execute(stmt)
        s.commit()
        return True

def delete_category(category_id):
    with sesion_local() as s:
        stmt = select(Product.id).join(Category, Category.id == Product.id).where(Category.id == category_id)
        check = s.execute(stmt).scalars().all()
        if check:
            raise ValueError('Нельзя удалить категорию, если в ней есть товары')
        stmt = delete(Category).where(Category.id == category_id)
        s.execute(stmt)
        s.commit()
        return True

def delete_supplier(sup_id):
    with sesion_local() as s:
        stmt = select(Product.supplier_id)
        check = s.execute(stmt).scalars().all()
        for id in check:
            if int(id) == int(sup_id):
                raise ValueError('Нельзя удалить поставщика, если к нему привязаны товары')
        stmt = delete(Supplier).where(Supplier.id == sup_id)
        s.execute(stmt)
        s.commit()
        return True
    
def delete_product(product_id):
    with sesion_local() as s:
        stmt = select(Stock_movement.product_id)
        check = s.execute(stmt).scalars().all()
        for id in check:
            if int(id) == int(product_id):
                raise ValueError('Нельзя удалить товар, если по нему есть складские операции')
        stmt = delete(Product).where(Product.id == product_id)
        s.execute(stmt)
        s.commit()
        return True

def delete_stock_movement(movement_id):
    with sesion_local() as s:
        stmt = delete(Stock_movement).where(Stock_movement.id == movement_id)
        s.execute(stmt)
        s.commit()
        return True

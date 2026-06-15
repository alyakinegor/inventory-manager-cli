from database import sesion_local
from models import Category, Product, Stock_movement, Supplier
from datetime import date
from sqlalchemy import select

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
        stmt = 
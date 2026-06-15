from sqlalchemy.orm import Mapped, mapped_column,relationship
from database import Base
from sqlalchemy import Integer, Text, CheckConstraint, ForeignKey, Boolean, Date, text
from datetime import date

class Category(Base):
    __tablename__= 'categories'
    __table_args__ = (
        CheckConstraint('length(name) > 0', name='check_name_not_empty'),
    )
    id: Mapped[int] = mapped_column(ForeignKey("products.category_id"), primary_key=True)
    name:Mapped[str] = mapped_column(Text, unique=True)
    # products: Mapped[list['Products']] = relationship(back_populates='category')

class Supplier(Base):
    __tablename__ = 'suppliers'
    __table_args__ = (
        CheckConstraint('length(name) > 0', name='check_name_not_empty'),
    )
    id: Mapped[int] = mapped_column(ForeignKey('products.supplier_id'), primary_key=True)
    name: Mapped[str] = mapped_column(Text, unique=True)
    phone: Mapped[str] = mapped_column(Text)
    email: Mapped[str] = mapped_column(Text, nullable=True, unique=True)
    is_active:Mapped[bool] = mapped_column(Boolean, server_default=('TRUE'))
    created_at = mapped_column(Date, server_default=text('CURRENT_DATE'))

class Product(Base):
    __tablename__ = 'products'
    __table_args__ = (
        CheckConstraint('length(name) > 0', name='check_name_not_empty'),
        CheckConstraint('purchase_price >= 0', name='check_prch_price'),
        CheckConstraint('selling_price >= 0', name='check_selling_price'),
        CheckConstraint('min_quantity >= 0', name='check_min_qua'),
    )
    id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(Text)
    sku: Mapped[str] = mapped_column(Text, unique=True)
    category_id: Mapped[int] = mapped_column(Integer)
    supplier_id: Mapped[int] = mapped_column(Integer)
    purchase_price: Mapped[int] = mapped_column(Integer)
    selling_price: Mapped[int] = mapped_column(Integer)
    min_quality: Mapped[int] = mapped_column(Integer)
    is_active: Mapped[bool] = mapped_column(Boolean, server_default=('TRUE'))
    created_at: Mapped[date] = mapped_column(Date, server_default=text('CURRENT_DATE'))
    
    # category = relationship(back_populates='products')

class Stock_movement(Base):
    __tablename__ = 'stock_movements'
    __table_args__ = (
        CheckConstraint('movement_type in ("IN", "OUT", "ADJUST")', name='mv_type'),
        CheckConstraint('quantity > 0', name='qua')
    )
    id: Mapped[int] = mapped_column(Integer)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'), nullable=False)
    movement_type: Mapped[str] = mapped_column(Text)
    quantity: Mapped[int] = mapped_column(Integer)
    coment: Mapped[str] = mapped_column(Text)
    created_at: Mapped[date] = mapped_column(Date, server_default=text('CURRENT_DATE'))




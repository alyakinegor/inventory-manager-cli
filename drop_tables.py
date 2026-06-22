from database import Base, engine
from models import Stock_movement, Product, Category, Supplier

Base.metadata.drop_all(engine)
print('Таблицы удалены')
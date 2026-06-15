from database import Base, engine

Base.metadata.drop_all(engine)
print('Таблицы удалены')
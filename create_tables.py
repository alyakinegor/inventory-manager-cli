from database import Base, engine

Base.metadata.create_all(engine)
print('Таблицы созданы')
from database import sesion_local
from sqlalchemy import select
with sesion_local() as s:
    stmt = select(1)
    res = s.execute(stmt).scalar()
    print(res)
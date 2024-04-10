import json

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_table,Publisher,Book,Shop,Stock,Sale


DSN = 'postgresql://postgres:1996@localhost:5432/test_py'
engine = sqlalchemy.create_engine(DSN)

create_table(engine)

Session = sessionmaker(bind=engine)
session = Session()

# with open('data_json/tests_data.json', 'r') as fd:
#     data = json.load(fd)

# for record in data:
#     model = {
#         'publisher': Publisher,
#         'shop': Shop,
#         'book': Book,
#         'stock': Stock,
#         'sale': Sale,
#     }[record.get('model')]
#     session.add(model(id=record.get('pk'), **record.get('fields')))
# session.commit()

def Select_from_table(nname : str):
    for pub,boo,st,sho,sal in session.query(Publisher,Book,Stock,Shop,Sale).join(Book,Publisher.id == Book.id_publisher).join(Stock,Book.id == Stock.id_book).join(Shop,Stock.id_shop == Shop.id).join(Sale,Stock.id == Sale.id_stock).filter(Publisher.name == nname ).all():
        print(boo,sho,sal)
    return

name = str(input("Введите имя... Пример : O’Reilly"))
Select_from_table(name)


session.close()
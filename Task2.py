def take_publisher_sales(publisher ="", publisher_id = 0):
    import sqlalchemy
    import sqlalchemy as sq
    from sqlalchemy.orm import declarative_base, relationship, sessionmaker

    DSN = "postgresql://postgres:postgres@localhost:5432/books_test"
    engine = sqlalchemy.create_engine(DSN)

    Session = sessionmaker(bind=engine)
    session = Session()
    if publisher != "":
        subq1 = session.query(Publisher).filter(Publisher.name.like("%publisher%")).subquery()
        subq2 = session.query(Book).join(subq1, Book.id_publisher == subq.c.id).subquery()
        q = session.query(Stock).join(subq2, Stock.id_book == subq.c.id).subquery()
        for s in q.all():
            print(" | ", s.book.name, s.shop.name, s.sale.price, s.sale.count)
    elif publisher_id != 0:
        subq1 = session.query(Publisher).filter(Publisher.id == publisher_id).subquery()
        subq2 = session.query(Book).join(subq1, Book.id_publisher == subq.c.id).subquery()
        q = session.query(Stock).join(subq2, Stock.id_book == subq.c.id).subquery()
        for s in q.all():
            print(" | ", s.book.name, s.shop.name, s.sale.price, s.sale.count)

if __name__ == "__main__":
    name_id = input("Введите имя или ID автора: ")
    try:
        id = int(name_id)
    except:
        id = 0
    if id != 0:
        take_publisher_sales("", id)
    else:
        take_publisher_sales(name_id, 0)
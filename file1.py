import psycopg2


def connect():
    db_con = psycopg2.connect(
        database='practice',
        user='postgres',
        password='***',
        host='localhost',
        port=5432
    )
    return db_con


def create(name, price=10.2):
    con = connect()
    cur = con.cursor()
    query = f'''
        insert into product(name, price) values (%s, %s);
    '''
    values = (name, price)
    cur.execute(query, values)
    con.commit()
    con.close()


def read():
    con = connect()
    cur = con.cursor()
    query = '''SELECT product.id, product.name, product.price, category.name FROM product
               INNER JOIN category ON product.category_id = category.id;
    '''
    cur.execute(query)
    result = cur.fetchall()
    con.close()
    return result

def read_category(id):
    con = connect()
    cur = con.cursor()
    query = '''SELECT product.id, product.name, product.price, category.name FROM product
               INNER JOIN category ON product.category_id = category.id
               WHERE product.category_id = %s;
    '''
    values = (id,)
    cur.execute(query, values)
    result = cur.fetchall()
    con.close()
    return result

def read_one(id):
    con = connect()
    cur = con.cursor()
    query = '''
        select * from product where id=%s
    '''
    values = (id,)
    cur.execute(query, values)
    result = cur.fetchone()
    con.close()
    return result


def update(id, name, price):
    con = connect()
    cur = con.cursor()

    query = '''
        update product set name=(%s), price=(%s)
        where id=%s 
    '''
    values = (name, price, id)

    cur.execute(query, values)
    con.commit()
    con.close()


def delete(id):
    con = connect()
    cur = con.cursor()
    query = '''
        delete from product where id=%s
    '''
    values = (id,)
    cur.execute(query, values)
    con.commit()
    con.close()

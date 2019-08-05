import sqlite3
import pandas as pd
DB = 'product-roulette.db'


def create_product_table():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE products (
        id TEXT PRIMARY KEY,
        product_name TEXT NOT NULL,
        created_at timestamp,
        updated_at timestamp
    )''')
    conn.commit()


def create_users_table():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE users (
        id TEXT PRIMARY KEY,
        persona TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        created_at timestamp,
        updated_at timestamp
    )''')
    conn.commit()


def create_feedback_table():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE feedbacks (
        id TEXT PRIMARY KEY,
        product_id TEXT NOT NULL,
        user_id TEXT NOT NULL,
        review TEXT ,
        rating INTEGER,
        created_at timestamp,
        updated_at timestamp
    )''')
    conn.commit()


def get_top_5_products(persona):
    if persona != "all":
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute("""
        select product_name as product, sum(rating)/count(rating) as avg_rating
        from products p
        inner join feedbacks fb
        on fb.product_id = p.id
        where fb.user_id in (select u.id from users u where persona = '%s' or persona = 'all')
        group by 1
        order by 2 desc
        limit 5
        """%(persona))
        dataframe = pd.DataFrame(cur.fetchall())
        print(dataframe)

    else:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute("""
                select product_name as product, sum(rating)/count(rating) as avg_rating
                from products p
                inner join feedbacks fb
                on fb.product_id = p.id
                group by 1
                order by 2 desc
                limit 5
                """ )
        dataframe = pd.DataFrame(cur.fetchall())
        print(dataframe)


def insert_users(id, persona, username, password, created_at, updated_at):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        insert into users values ('%s', '%s', '%s', '%s', '%s', '%s')
    """ % (id, persona, username, password, created_at, updated_at))
    conn.commit()


def insert_product(id, product_name, created_at, updated_at):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        insert into products values ('%s', '%s', '%s', '%s')
    """ % (id, product_name, created_at, updated_at))
    conn.commit()


def insert_feedback(id, product_id, user_id, rating, review, created_at, updated_at):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        insert into feedbacks values ('%s', '%s', '%s', '%s', '%s', '%s', '%s')
    """ %(id, product_id, user_id, review, rating, created_at, updated_at))
    conn.commit()


def is_user_exists(username, password):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""select id from users where username = '%s' and password = '%s' """ %(username, password))
    dataframe = pd.DataFrame(cur.fetchall())
    if len(dataframe) == 1:
        return True
    else:
        return False


def get_user_details(username, password):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""select id, persona from users where username = '%s' and password = '%s' """ % (username, password))
    dataframe = pd.DataFrame(cur.fetchall())
    if len(dataframe) == 1:
        dataframe.columns = ['user_id', 'persona']
        return dataframe
    else:
        return False


def get_product_details(product_name):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""select id as product_id, product_name from products where product_name = '%s' """ % (product_name))
    dataframe = pd.DataFrame(cur.fetchall())
    if len(dataframe) == 1:
        dataframe.columns = ['product_id', 'product_name']
        return dataframe['product_id'].iloc[0], dataframe['product_name'].iloc[0]
    else:
        return pd.DataFrame()


def drop_table(table_name):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""drop table '%s' """ % (table_name))
    conn.commit()


def is_product_exists(product_name):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""select id from products where product_name = '%s' """ % (product_name))
    dataframe = pd.DataFrame(cur.fetchall())
    if len(dataframe) == 1:
        return True
    else:
        return False


def is_username_exists(username):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""select id from users where username = '%s' """ % (username))
    dataframe = pd.DataFrame(cur.fetchall())
    if len(dataframe) == 0:
        return True
    else:
        return False


def update_user_data(username, persona):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        update users
        set persona = '%s'
        where username = '%s'
    """ %(persona, username))
    conn.commit()


def update_ratings(rating, review, user_id, product_id):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
            update feedbacks
            set rating = {}, review = {}
            where user_id = {}
            and product_id = {}
        """ .format(rating, review, user_id, product_id))
    conn.commit()


def is_feedback_exists(user_id, product_id):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""select id from feedbacks 
    where user_id = '%s'
    and product_id = '%s' 
    """ % (user_id, product_id))
    dataframe = pd.DataFrame(cur.fetchall())
    if len(dataframe) == 1:
        return True
    else:
        return False

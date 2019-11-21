import pymysql
import datetime
import settings
import os

def _open_db_connection():
    # Connect to the database
    connection = pymysql.connect(host=os.getenv("DB_HOST"),
                                user=os.getenv("DB_USER"),
                                password=os.getenv("DB_PASSWORD"),
                                db=os.getenv("DB_DBNAME"),
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection

def _close_db_connection(connection):
    connection.close()

def show_all_coupons():
    connection = _open_db_connection()

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `coupons`"
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    finally:
        _close_db_connection(connection)

"""
reads coupon details from the database. 
"""
def read_one(coupon_code):
    connection = _open_db_connection()

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `coupons` WHERE code = %s"
            cursor.execute(sql, (coupon_code))
            row = cursor.fetchone()
            return row
    finally:
        _close_db_connection(connection)

def is_valid_coupon(coupon_code):
    coupon = read_one(coupon_code)

    if coupon == None:
        raise Exception('coupon_code does not exist')

    today = datetime.datetime.now()

    return (today >= coupon['start_date']) & (today <= coupon['end_date'])


#================================
# load_dotenv()

# show_all_coupons()
# print(read_one('blah'))
print(read_one('code1'))
# print(is_valid_coupon('code1'))
# print(is_valid_coupon('code2'))
# is_valid_coupon('code3')

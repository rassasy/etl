import pymysql

def get_connection():
    return pymysql.connect(host='localhost',
                           database='rassasy',
                           user='root',
                           password='root')

def insert_restaurants(restaurants):
    try:
        conn = get_connection()
        conn.autocommit = False
        cursor = conn.cursor()

        for restaurant in restaurants:
            restaurant.toSQL(cursor)

        conn.commit()
        print ("Record Updated successfully ")
    except Exception as error :
        print(f"Failed to update records due to {error}. Rolling back transaction...")
        conn.rollback()
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("MySQL connection closed successfully")
import pymysql


def get_connection():
    return pymysql.connect(host='localhost',
                           database='rassasy',
                           user='root',
                           password='root')

def insert_restaurants(restaurants):
    try:
        connection = get_connection()
        connection.autocommit = False
        cursor = connection.cursor()

        for restaurant in restaurants:
            print (f"Inserting {restaurant.name} into the MySQL database...")
            restaurant.toSQL(cursor)

        connection.commit()
        print ("Record Updated successfully ")
    except Exception as error :
        print(f"Failed to update records due to {error}. Rolling back transaction...")
        connection.rollback()
    finally:
        if connection.open:
            cursor.close()
            connection.close()
            print("MySQL connection closed successfully")
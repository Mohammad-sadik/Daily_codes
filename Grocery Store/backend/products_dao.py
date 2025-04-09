from sql_connection import get_sql_connection

def get_all_products(connection):

    cursor = connection.cursor()
    query = """SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name
    FROM grocery_store.products inner join grocery_store.uom 
    ON products.uom_id = uom.uom_id
    order by products.product_id; """
    cursor.execute(query)
    response = []

    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                "product_id": product_id,
                "name": name,
                "uom_id": uom_id,
                "price_per_unit": price_per_unit,
                "uom_name": uom_name
            }
        )
    connection.close()
    return response


def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = """ insert into grocery_store.products (name, uom_id, price_per_unit)
                values(%s, %s, %s)
                """
    data = (product['name'], product['uom_id'], product["price_per_unit"])
    cursor.execute(query, data)
    connection.commit()
    connection.close()
    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = 'DELETE FROM grocery_store.products WHERE product_id =' + str(product_id)
    cursor.execute(query)
    connection.commit()
    connection.close()
    return f"Deleted successfully, product id is {product_id}"

if __name__ == "__main__":
    connection = get_sql_connection()
    print(delete_product(connection, 12))


# if __name__ == "__main__":
#     connection = get_sql_connection()
#     print(insert_new_product(connection,{
#                 "name": 'cabbage',
#                 "uom_id": '1',
#                 "price_per_unit": '50'
#     }))


# if __name__ == "__main__":
#     connection = get_sql_connection()
#     for _ in get_all_products(connection):
#         print(_)
from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name, products.BarCode from products inner join uom on products.uom_id=uom.uom_id")
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name, BarCode) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name,
            'BarCode': BarCode
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name,uom_id, price_per_unit,BarCode )"
             "VALUES (%s, %s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'],product['BarCode'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    for i in get_all_products(connection):
        print(i)
    # print(insert_new_product(connection, {
    #     'product_name': 'potatoes',
    #     'BarCode' : '100000011',
    #     'uom_id': '1',
    #     'price_per_unit': 10
    # }))
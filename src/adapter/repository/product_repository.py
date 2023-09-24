from domain import ProductProtocol, ProductModel

class ProductRepository(ProductProtocol):
    def __init__(self, connection) -> None:
        self.connection = connection

    def values(self) -> list:
        products = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT name, space, value, quantity FROM products")
        for product in cursor:
            for _ in range(product[3]):
                products.append(
                    ProductModel(name=product[0], 
                                space=product[1], 
                                value=product[2]))
        cursor.close()
        return products
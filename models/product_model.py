from models.db_context import DbContext
from domain.product import Product

class ProductModel(DbContext):
    """
    Class that contains the interactions with Product table in the database
    """
    def __init__(self) -> None:
        """
        Method that defines the constructor of the class
        """
        super().__init__()
        
    def get_products(self) -> list:
        """
        Method that recovers all the Products in the database
        """
        products_list = []
        try:
            query = "SELECT T0.Id, T0.Name, T0.Description, T0.Type, T0.Unit_Price FROM Product T0 ORDER BY T0.Type DESC"
            rows = self.run_query(query)
            for row in rows:
                product = Product(row[0],
                                  row[1],
                                  row[2],
                                  row[3],
                                  row[4],
                                  )
                products_list.append(product)
        except Exception as ex:
            raise ex
        return products_list
from domain.client import Client
from models.db_context import DbContext
from domain.order import Order

class OrderModel(DbContext):
    """
    Class that contains the interactions with Order table in the database
    """
    def __init__(self) -> None:
        """
        Method that defines the constructor of the class
        """
        super().__init__()
        
    def create_order(self,
                     order: Order) -> bool:
        """
        Method that creates an Order in the database
        """
        result = False
        try:
            query = "INSERT INTO [Order] VALUES(NULL, ?, ?, ?)"
            parameters = (order.product.id, order.client.name, order.tax_percentage)
            self.run_query(query, parameters)
            result = True
        except Exception as ex:
            raise ex
        return result
    
    def get_orders(self) -> list:
        """
        Method that recovers all the Orders in the database
        """
        orders_list = []
        try:
            query = "SELECT T0.Name_Client, group_concat(T1.Name, ', ') AS Ordered_Products, T0.Tax_Percentage, (SUM(T1.Unit_Price) + ((T0.Tax_Percentage * SUM(T1.Unit_Price))/100)) AS Total_Amount FROM [Order] T0 INNER JOIN Product T1 ON T0.Id_Product = T1.Id GROUP BY T0.Name_Client ORDER BY T0.Id DESC"
            rows = self.run_query(query)
            for row in rows:
                client = Client(row[0])
                order = Order(0,
                              None,
                              client,
                              row[2])
                order.products_summary = row[1]
                order.total_amount = row[3]
                orders_list.append(order)
        except Exception as ex:
            raise ex
        return orders_list
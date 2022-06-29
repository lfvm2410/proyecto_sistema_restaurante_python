from domain.client import Client
from domain.product import Product

class Order:
    """
    Class that containts the Order attributes
    """
    def __init__(self,
                 id: int,
                 product: Product,
                 client: Client,
                 tax_percentage: float) -> None:
        """
        Method that defines the constructor of the class
        """
        self.id = id
        self.product = product
        self.client = client
        self.tax_percentage = tax_percentage
        self.products_summary = ""
        self.total_amount = 0
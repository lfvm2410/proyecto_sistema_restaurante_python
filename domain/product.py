class Product:
    """
    Class that containts the Product attributes
    """
    def __init__(self,
                 id: int,
                 name: str,
                 description: str,
                 type: str,
                 unit_price) -> None:
        """
        Method that defines the constructor of the class
        """
        self.id = id
        self.name = name
        self.description = description
        self.type = type
        self.unit_price = unit_price

from tkinter import Tk
from models.product_model import ProductModel
from views.product_view import ProductView

class ProductController:
    """
    Class controller for Product screen
    """
    def __init__(self) -> None:
        """
        Method that defines the constructor of the class
        """
        self.window = Tk()
        self.product_model = ProductModel()
        
    def configure_ui(self) -> None:
        """
        Method that configures the ui of Product view
        """
        try:
            self.__product_view = ProductView(self.window)
            self.__product_view.configure_view()
        except Exception as ex:
            raise ex
        
    def fill_products_table(self) -> None:
        """
        Method that loads up the Products table
        """
        try:
            self.__product_view.tbl_products.delete(*self.__product_view.tbl_products.get_children())
            products_list = self.product_model.get_products()
            for product in products_list:
                self.__product_view.tbl_products.insert("", "end", values=[product.name, product.description, product.type, product.unit_price])
        except Exception as ex:
            raise ex
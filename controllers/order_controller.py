from tkinter import Tk
from domain.client import Client
from domain.order import Order
from domain.product import Product
from models.order_model import OrderModel
from models.product_model import ProductModel
from views.order_view import OrderView

class OrderController:
    """
    Controller class for Order
    """
    def __init__(self,
                 window: Tk) -> None:
        """
        Method that defines the constructor of the class
        """
        self.window = window
        self.product_model = ProductModel()
        self.order_model = OrderModel()
        self.tax_percentage = 0
        self.products_list_box = {}
        
    def configure_ui(self) -> None:
        """
        Method that configures the ui of order window
        """
        try:
            self.order_view = OrderView(self.window)
            self.order_view.configure_view()
            self.__fill_products_listbox()
            self.__bind_view_buttons()
            self.__fill_orders_table()
            self.order_view.display_screen()
            self.__get_tax_percentage()
        except Exception as ex:
            raise ex
        
    def __fill_products_listbox(self) -> None:
        """
        Method loads up the listbox of products
        """
        try:
            products_list = self.product_model.get_products()
            for index, product in enumerate(products_list):
                self.order_view.listbox_products.insert(product.id, 
                                                        product.name)
                self.products_list_box[index] = {
                    "product_id" : product.id,
                    "product_name" : product.name
                    }
        except Exception as ex:
            raise ex
        
    def __bind_view_buttons(self) -> None:
        """
        Method that add listeners to buttons available in the orders view
        """
        try:
            self.order_view.btn_save.configure(command=self.__save_order)
        except Exception as ex:
            raise ex
        
    def __save_order(self) -> None:
        """
        Method that saves an order in the database
        """
        try:
            client_name = self.order_view.ipt_client_name.get()
            create_counter = 0
            if len(client_name) != 0 and len(self.order_view.listbox_products.curselection()) != 0:
                client = Client(client_name.strip())
                for index in self.order_view.listbox_products.curselection():
                    product = Product(self.products_list_box[index]["product_id"], 
                                      "", 
                                      "", 
                                      "", 
                                      0)
                    order = Order(0, 
                                  product, 
                                  client, 
                                  self.tax_percentage)
                    result = self.order_model.create_order(order)
                    if result:
                         create_counter = create_counter + 1
                if create_counter == len(self.order_view.listbox_products.curselection()):
                    self.order_view.ipt_client_name.delete(0, "end")
                    self.order_view.listbox_products.selection_clear(0, "end")
                    self.__fill_orders_table()
                    self.order_view.show_message("info",
                                                 "Orden registrada",
                                                 f"La orden para {client_name} se ha registrado satisfactoriamente")
                else:
                    self.order_view.show_message("error",
                                                 "Orden no registrada",
                                                 f"Hubo un problema al tratar de registrar la orden para {client_name}")
            else:
                self.order_view.show_message("info",
                                             "Orden incompleta",
                                             f"El 'Nombre del cliente' no puede estar vacío y debe seleccionar al menos un producto del menú para continuar")
        except Exception as ex:
            self.order_view.show_message("error", 
                                         "Orden no registrada", 
                                         f"Hubo un problema al tratar de registrar la orden para {client_name}. Detalles:\n{str(ex)}")
            
    def __fill_orders_table(self) -> None:
        """
        Method that loads up the orders table in the ui
        """
        try:
            self.order_view.tbl_orders.delete(*self.order_view.tbl_orders.get_children())
            orders_list = self.order_model.get_orders()
            for order in orders_list:
                self.order_view.tbl_orders.insert("", "end", values=[order.client.name, order.products_summary, order.tax_percentage, order.total_amount])
        except Exception as ex:
            raise ex
        
    def __get_tax_percentage(self) -> None:
        """
        Method that requests the tax percentage to the user
        """
        try:
            self.tax_percentage = float(self.order_view.show_input_dialog("Porcentaje de impuesto", "Digite el porcentaje de impuesto que desea agregar al cálculo del monto de las ordenes"))
            self.order_view.lbl_tax_percentage.config(text=f"{self.order_view.lbl_tax_percentage['text']} {self.tax_percentage}%")
        except Exception as ex:
            self.tax_percentage = 0
            self.order_view.show_message("error",
                                         "Valor inválido",
                                         f"Por favor digite un valor númerico")
            raise ex
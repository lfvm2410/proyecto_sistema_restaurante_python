from tkinter import *
from tkinter import ttk

class ProductView:
    """
    Class for define/build the product view
    """
    def __init__(self,
                 window: Tk) -> None:
        """
        Method that defines the constructor of the class
        """
        self.window = window
        self.__configure_window()
        
    def __configure_window(self) -> None:
        """
        Method for configure the window layout
        """
        try:
            self.window.title("Restaurante - Menú Principal")
            self.window.rowconfigure(0, weight=1)
            self.window.columnconfigure(0, weight=1)
        except Exception as ex:
            raise ex
    
    def configure_view(self) -> None:
        """
        Method for configure the Product window
        """
        try:
            #Creating a frame container for all elements of this screen
            self.frame_main = Frame(master=self.window)
            self.frame_main.grid(row=0, column=0)
            #Creating table for visualize the menu
            self.tbl_products = ttk.Treeview(master=self.frame_main ,height=10, columns=["#1", "#2", "#3", "#4"], show=["headings"])
            self.tbl_products.grid(row=1, column=0, columnspan=2)
            self.tbl_products.heading(column="#1", text="Name", anchor=CENTER)
            self.tbl_products.heading(column="#2", text="Description", anchor=CENTER)
            self.tbl_products.heading(column="#3", text="Type", anchor=CENTER)
            self.tbl_products.heading(column="#4", text="Unit Price", anchor=CENTER)
        except Exception as ex:
            raise ex
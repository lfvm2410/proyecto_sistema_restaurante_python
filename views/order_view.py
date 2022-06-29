from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from typing import Literal

class OrderView:
    """
    Class for define/build the order view
    """
    def __init__(self,
                 window: Tk) -> None:
        """
        Method that defines the constructor of the class
        """
        self.window = window
        self.window.title("Restaurante - Menú Principal")

    def configure_view(self) -> None:
        """
        Method that builds the complete UI for Order screen
        """
        try:
            #Creating a frame container for all elements of this screen
            self.frame_main = Frame(master=self.window)
            self.frame_main.grid(row=0, column=0)
            #Creating a frame container for order form
            self.frame_create_order_form = LabelFrame(master=self.frame_main, text="Registrar orden")
            self.frame_create_order_form.grid(row=1, column=0, columnspan=3, pady=20)
            #Creating Client Name Label
            self.lbl_client_name = Label(master=self.frame_create_order_form, text="Nombre del cliente: ")
            self.lbl_client_name.grid(row=2, column=0)
            #Creating Client Name Input
            self.ipt_client_name = Entry(master=self.frame_create_order_form)
            self.ipt_client_name.focus()
            self.ipt_client_name.grid(row=2, column=1)
            #Creating Products Label
            self.lbl_products = Label(master=self.frame_create_order_form, text="Productos: ")
            self.lbl_products.grid(row=3, column=0, sticky="w")
            #Creating Products Listbox
            self.listbox_products = Listbox(master=self.frame_create_order_form, selectmode="multiple")
            self.listbox_products.grid(row=3, column=1, columnspan=2)
            #Creating Save Button
            self.btn_save = Button(master=self.frame_create_order_form, text="Guardar")
            self.btn_save.grid(row=4, columnspan=2, sticky=EW)
            #Creating table for visualize the orders
            self.tbl_orders = ttk.Treeview(master=self.frame_main ,height=10, columns=["#1", "#2", "#3", "#4"], show=["headings"])
            self.tbl_orders.grid(row=5, column=0, columnspan=2, pady=20)
            self.tbl_orders.heading(column="#1", text="Cliente", anchor=CENTER)
            self.tbl_orders.heading(column="#2", text="Productos Ordenados", anchor=CENTER)
            self.tbl_orders.heading(column="#3", text="% Impuesto", anchor=CENTER)
            self.tbl_orders.heading(column="#4", text="Precio Total", anchor=CENTER)
            #Creating Tax Percentage Label
            self.lbl_tax_percentage = Label(master=self.frame_main, text="Porcentaje de impuesto: ", foreground="blue", font=('Helvetica', 14, 'bold'))
            self.lbl_tax_percentage.grid(row=6, column=0, pady=20)
        except Exception as ex:
            raise ex
    
    def show_input_dialog(self,
                          title: str,
                          prompt: str) -> str:
        """
        Method that shows an input dialog
        """
        input_result = ""
        try:
            input_result = simpledialog.askstring(title=title, 
                                                  prompt=prompt)
        except Exception as ex:
            raise ex
        return input_result
        
    def show_message(self,
                     type: Literal['info', 'error'],
                     title: str,
                     message: str) -> None:
        """
        Method that shows a message popup
        """
        try:
            if type.strip().lower() == "info":
                messagebox.showinfo(title=title, message=message)
            elif type.strip().lower() == "error":
                messagebox.showerror(title=title, message=message)
        except Exception as ex:
            raise ex
    
    def display_screen(self) -> None:
        """
        Method that shows up the UI for Order screen
        """
        try:
            self.frame_main.tkraise()
        except Exception as ex:
            raise ex
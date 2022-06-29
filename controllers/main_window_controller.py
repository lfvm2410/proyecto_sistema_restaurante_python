from tkinter import Tk
from controllers.product_controller import ProductController
from views.main_window import MainWindow

class MainWindowController:
    """
    Controller class for main window
    """
    def __init__(self) -> None:
        """
        Method that defines the constructor of the class
        """
        self.window = Tk()
    
    def configure_ui(self) -> None:
        """
        Method that configure the main window widgets
        """
        try:
            self.__main_window = MainWindow(self.window)
            self.__main_window.configure_main_menu_bar()
            self.__bind_view_buttons()
        except Exception as ex:
            raise ex
        
    def __bind_view_buttons(self) -> None:
        """
        Method that adds listeners to menu bar items
        """
        try:
            #Adding sub menus to the bar
            self.__main_window.menu_bar.add_command(label="Ver Menú", command=self.__open_product_view)
            self.__main_window.menu_bar.add_command(label="Salir", command=self.__close_application)
        except Exception as ex:
            raise ex
        
    def __open_product_view(self) -> None:
        """
        Method that opens up a external window with the menu of products
        """
        try:
            self.__product_controller = ProductController()
            self.__product_controller.configure_ui()
            self.__product_controller.fill_products_table()
        except Exception as ex:
            raise ex
        
    def __close_application(self) -> None:
        """
        Method that close the window when 'Exit' menu item is pressed
        """
        try:
            self.__main_window.window.quit()
        except Exception as ex:
            raise ex
        
    def display_window(self) -> None:
        """
        Method that shows up the window
        """
        try:
            self.window.mainloop()
        except Exception as ex:
            raise ex
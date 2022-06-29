from tkinter import *

class MainWindow:
    """
    Class for define/build the main window specifications
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
    
    def configure_main_menu_bar(self) -> None:
        """
        Method for configure the main menu bar
        """
        try:
            #Create main menu bar and sub menus
            self.menu_bar = Menu(self.window)
            #Adding menu bar to the window
            self.window.config(menu=self.menu_bar)
        except Exception as ex:
            raise ex
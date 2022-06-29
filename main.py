from controllers.main_window_controller import MainWindowController
from controllers.order_controller import OrderController

if __name__ == "__main__":
    """
    Main thread of execution inside the application
    """
    try:
        main_window_controller = MainWindowController()
        main_window_controller.configure_ui()
        order_controller = OrderController(main_window_controller.window)
        order_controller.configure_ui()
        main_window_controller.display_window()
    except Exception as ex:
        print(f"An error has ocurred: {str(ex)}")
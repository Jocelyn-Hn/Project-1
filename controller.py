from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        """
        Function to set up application object.
        :param name: Controller
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_submit.clicked.connect(lambda: self.submit())
        self.button_clear.clicked.connect(lambda: self.clear())

    def submit(self):
        """
        Function that calculates the price amounts on user input.
        :return:
        """
        try:
            amount_cookie = float(self.input_cookie.text())
            amount_sandwich = float(self.input_sandwich.text())
            amount_soup = float(self.input_soup.text())
            amount_water = float(self.input_water.text())
            amount_coffee = float(self.input_coffee.text())

            if (amount_cookie % 1 != 0) or (amount_sandwich % 1 != 0) or \
                    (amount_soup % 1 != 0) or (amount_water % 1 != 0) or (amount_coffee % 1 != 0):
                raise ValueError

            quantity = amount_cookie + amount_sandwich + amount_soup + amount_water + amount_coffee
            cookie = amount_cookie * 1.5
            sandwich = amount_sandwich * 4
            soup = amount_soup * 3
            water = amount_water * 1
            coffee = amount_coffee * 2.5
            subtotal = cookie + sandwich + soup + water + coffee
            tax = float((cookie + sandwich + soup + water + coffee) * 0.10)
            total = cookie + sandwich + soup + water + coffee + tax

            self.error_summary.setText('')
            self.label_cartmenu.setText('- - - - - CART MENU - - - - -')
            self.output_labels.setText(f'Cookies: \n'
                                       f'Sandwiches: \n'
                                       f'Soups: \n'
                                       f'Waters: \n'
                                       f'Coffees: \n'
                                       f'\n'
                                       f'SUBTOTAL: \n'
                                       f'Tax (10%): \n'
                                       f'\n'
                                       f'TOTAL: \n'
                                       f'\n'
                                       f'# ITEMS SOLD: \n')

            self.output_prices.setText(f'${cookie:.2f} \n'
                                       f'${sandwich:.2f} \n'
                                       f'${soup:.2f} \n'
                                       f'${water:.2f} \n'
                                       f'${coffee:.2f} \n'
                                       f'\n'
                                       f'${subtotal:.2f} \n'
                                       f'${tax:.2f} \n'
                                       f'\n'
                                       f'${total:.2f} \n'
                                       f'\n'
                                       f'{quantity:.0f}')
        except ValueError:
            self.output_labels.setText('')
            self.output_prices.setText('')
            self.label_cartmenu.setText('- - - - - - - ERROR - - - - - - -')
            self.error_summary.setText(f'Quantity amounts \n'
                                       f'need to be numeric and \n'
                                       f'whole number values \n'
                                       f'e.g. 3 not 3.5, 3 not \'e\' \n'
                                       f'\n'
                                       f'Put 0 for no quantity \n'
                                       f'desired.')

    def clear(self):
        """
        Function that resets application.
        :return:
        """
        self.label_cartmenu.setText('')
        self.error_summary.setText('')
        self.output_labels.setText('')
        self.output_prices.setText('')
        self.input_cookie.setText('')
        self.input_sandwich.setText('')
        self.input_soup.setText('')
        self.input_water.setText('')
        self.input_coffee.setText('')

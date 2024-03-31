import requests
from bs4 import BeautifulSoup


class Stock():
    '''
    this is the main stock class which which store data of perticular stock
    and do specific computation on that
    '''

    def __init__(self, symbol, exchange='NSE'):
        self.symbol = symbol
        self.exchange = exchange
        self.data = self.get_data()
    

    def get_data(self):
        url = f'https://www.google.com/finance/quote/{self.symbol}:{self.exchange}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        return soup
    

    def smart_str_to_number(self, s:str) -> float :
        '''
        this funtion convert a stry int float 
        with smart way by first removing all other unnecessary char like
        $22.83:) -> 22.85

        but for remember to check the s that give as a input 
        '''
        valid_chr = [i for i in '0123456789.']
        modified_s = ''
        for i in s:
            if i in valid_chr:
                modified_s += i
        
        return float(modified_s)


    def ltp(self):
        class_price ="YMlKec fxKbKc"
        price = self.data.find(class_ = class_price).text
        num_price = self.smart_str_to_number(price)

        return num_price

    def pe_ration(self):
        css_selector = r".eYanAe > .gyFHrc:nth-child(7) >.P6K39c"
        price = self.data.select_one(css_selector).text
        return price


def symboltxt_to_list(file:str):
    '''
    this function will read the symbol txt file
    which contail symbols names in below format
    SYM1
    SYM2
    [AN EMPTY LINE AT THE END IMPORTANT]
    
    and this funtion return a list like
    ['SYM1', 'SYM2']
    '''
    symbol = []
    with open('nse_all_symbol.txt', 'r') as nse_symbol:
        for i in nse_symbol.readlines():
            symbol.append(i[0:-1])
        return symbol

symbols = symboltxt_to_list('noting')
# print(symbols)

for i in symbols:
    print(Stock(i).ltp())

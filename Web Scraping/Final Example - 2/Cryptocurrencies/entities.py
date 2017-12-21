

class Exchange():

    def __init__(self, name, markets=None):
        self.name = name
        self.markets = markets or {}

    def add_market(self, market):
        if market.name in self.markets:
            raise Exception(f"Market {market.name} already exists in Exchange {exchange.name}")
        
        self.markets[market.name] = market


class Market():

    def __init__(self, currency_main, currency_base, price:float):
        '''
        @param currency_main is tha AAA in AAA/BBB
        @param currency_base is tha BBB in AAA/BBB
        '''
        self.currency_main = currency_main
        self.currency_base = currency_base
        self.name = f"{currency_main}/{currency_base}"
        self.price = price

    def parse(market_currencies:str, price):
        '''
        Create a market from the text "AAA/BBB"
        '''
        
        try:
            currencies = market_currencies.split("/")
            if len(currencies) == 2:
                return Market(currencies[0], currencies[1], price)
            else:
                raise Exception(f"Fail to parse market from {market_currencies}")
        except Exception as err:
            raise Exception(f"Fail to parse market from {market_currencies}")


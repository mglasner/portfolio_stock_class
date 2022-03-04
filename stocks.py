"""Simple Portfolio Class."""
import datetime
import random
from typing import Tuple


class Stock(object):
    """Simple Stock Class for testing porpouses."""

    def __init__(self, name: str):
        self.name = name

    def Price(self, date: datetime) -> int:
        """Random integer for the stock price."""
        return random.randint(1, 100)

    def get_name(self):
        return self.name


class Portfolio(object):
    """Portfolio class made by a collection of stocks."""

    def __init__(self, stocks: list):
        self.stocks = stocks

    def Profit(
        self, initial_date: datetime, final_date: datetime
    ) -> Tuple[float, float]:
        """Method to return the total profit and annualized return between two dates.

        Args:
            initial_date (datetime): Initial date.
            final_date (datetime): Final date.

        Returns:
            Tuple[float, float]: total profit (usd) and annualized return (rate).
        """
        portfolio_initial_price, portfolio_final_price = 0, 0
        for stock in self.stocks:
            initial_price = stock.Price(initial_date)
            final_price = stock.Price(final_date)
            portfolio_initial_price += initial_price
            portfolio_final_price += final_price

        profit = portfolio_final_price - portfolio_initial_price
        profit_rate = profit / portfolio_initial_price

        invest_time = (final_date - initial_date).days
        annualized_return = (1 + profit_rate) ** (invest_time / 365) - 1
        return profit, annualized_return


# Run testing script
if __name__ == "__main__":
    stock1 = Stock("stock1")
    stock2 = Stock("stock2")
    stock3 = Stock("stock3")
    p = Portfolio([stock1, stock2, stock3])
    print(*p.Profit(datetime.datetime(2008, 8, 18), datetime.datetime.now()))

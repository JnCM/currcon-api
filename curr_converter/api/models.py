from api.utils import get_quote


class Converter:
    """Class to convert a currency into another currency.
    
    Parameters
    ----------
        - from_curr (str): The origin currency.
        - to_curr (str): The target currency.
        - amount (float): The amount to convert.
    """

    def __init__(self, from_curr: str, to_curr: str, amount: float):
        self.__from_curr = from_curr
        self.__to_curr = to_curr
        self.__amount = amount

    def convert_amount(self):
        """Returns the amount converted for the target currency.
        
        Returns
        -------
            - amount_converted (float): The amount converted.
        """

        # Getting the quote
        rate = get_quote(self.__from_curr, self.__to_curr)
        
        if rate == 0.0:
            return rate

        # Returning the amount converted
        amount_converted = round(rate*self.__amount, 2)
        return amount_converted

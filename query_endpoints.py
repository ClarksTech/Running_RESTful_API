import requests
from typing import Any, Dict, Optional

class MileageTransformer:
    """
    A class to perform various mileage transformations by making HTTP requests
    to specified endpoints.
    """
    BASE_URL = 'http://127.0.0.1:5000'
    
    def __init__(self):
        """Initialize the MileageTransformer class."""
        pass
    
    def _request(self, endpoint: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Helper method to make a GET request to the given endpoint with the provided parameters.
        
        Args:
            endpoint (str): The API endpoint to send the request to.
            **kwargs: Arbitrary keyword arguments representing query parameters.
            
        Returns:
            dict: The JSON response from the server.
        """
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = requests.get(f'{self.BASE_URL}/{endpoint}', params=params)
        return response.json()

    def forward_transform(self, n: int, target_mileage: Optional[float]=None, starting_mileage: Optional[float]=None,
                           a: Optional[float]=None, b: Optional[float]=None) -> Dict[str, Any]:
        """
        Perform the forward transformation.
        
        Args:
            n (int): Week number.
            target_mileage (float, optional): The target mileage.
            starting_mileage (float, optional): The starting mileage.
            a (float, optional): Parameter a.
            b (float, optional): Parameter b.
            
        Returns:
            dict: The JSON response from the server.
        """
        return self._request('forward_transform', n=n, target_mileage=target_mileage, starting_mileage=starting_mileage, a=a, b=b)

    def reverse_transform(self, weekly_mileage: float, target_mileage: Optional[float]=None, starting_mileage: Optional[float]=None,
                           a: Optional[float]=None, b: Optional[float]=None) -> Dict[str, Any]:
        """
        Perform the reverse transformation.
        
        Args:
            weekly_mileage (float): The weekly mileage.
            target_mileage (float, optional): The target mileage.
            starting_mileage (float, optional): The starting mileage.
            a (float, optional): Parameter a.
            b (float, optional): Parameter b.
            
        Returns:
            dict: The JSON response from the server.
        """
        return self._request('reverse_transform', weekly_mileage=weekly_mileage, target_mileage=target_mileage, starting_mileage=starting_mileage, a=a, b=b)

    def rate_of_change(self, n: int, target_mileage: Optional[float]=None, starting_mileage: Optional[float]=None, a: Optional[float]=None,
                        b: Optional[float]=None) -> Dict[str, Any]:
        """
        Calculate the rate of change.
        
        Args:
            n (int): Week number.
            target_mileage (float, optional): The target mileage.
            starting_mileage (float, optional): The starting mileage.
            a (float, optional): Parameter a.
            b (float, optional): Parameter b.
            
        Returns:
            dict: The JSON response from the server.
        """
        return self._request('rate_of_change', n=n, target_mileage=target_mileage, starting_mileage=starting_mileage, a=a, b=b)

if __name__ == "__main__":
    transformer = MileageTransformer()
    
    week_number = 10
    weekly_mileage = 12.5

    print(f'Forward Transform for week {week_number}:')
    print(transformer.forward_transform(week_number))

    print(f'\nReverse Transform for weekly mileage {weekly_mileage}:')
    print(transformer.reverse_transform(weekly_mileage))

    print(f'\nRate of Change for week {week_number}:')
    print(transformer.rate_of_change(week_number))

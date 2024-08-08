# training_model/base_model.py
from abc import ABC, abstractmethod

class TrainingModel(ABC):
    """
    Abstract base class for a training model that calculates mileage.

    Attributes:
        target_mileage (float): The target mileage to be achieved.
        starting_mileage (float): The starting mileage.
        a (float): Parameter 'a' for the model. Must be between 0 and 1.
        b (float): Parameter 'b' for the model. Must be greater than 0.
    """

    def __init__(self, target_mileage: float, starting_mileage: float, a: float, b: float) -> None:
        """
        Initializes the TrainingModel with the given parameters.

        Args:
            target_mileage (float): The target mileage.
            starting_mileage (float): The starting mileage.
            a (float): Parameter 'a'.
            b (float): Parameter 'b'.
        """
        self.target_mileage = target_mileage
        self.starting_mileage = starting_mileage
        self.a = a
        self.b = b
        self.validate_parameters()

    def validate_parameters(self) -> None:
        """
        Validates the parameters of the model.
        
        Raises:
            ValueError: If any parameter does not meet its constraints.
        """
        if not (0 < self.a < 1):
            raise ValueError("Parameter 'a' must satisfy: 0 < a < 1")
        if self.b <= 0:
            raise ValueError("Parameter 'b' must satisfy: b > 0")
        if self.starting_mileage >= self.target_mileage:
            raise ValueError("Starting mileage must be less than target mileage")

    @abstractmethod
    def calculate_weekly_mileage(self, n: int) -> float:
        """
        Abstract method to calculate weekly mileage.

        Args:
            n (int): The week number.

        Returns:
            float: The mileage for the nth week.
        """
        pass

    @abstractmethod
    def inverse_transform(self, weekly_mileage: float) -> float:
        """
        Abstract method to perform inverse transformation.

        Args:
            weekly_mileage (float): The weekly mileage.

        Returns:
            float: The current week n.
        """
        pass

    @abstractmethod
    def rate_of_change(self, n: int) -> float:
        """
        Abstract method to calculate the rate of change in mileage.

        Args:
            n (int): The week number.

        Returns:
            float: The rate of change.
        """
        pass


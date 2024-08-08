# training_model/existing_model.py
import math
from .base_model import TrainingModel

class ExistingTrainingModel(TrainingModel):
    """
    Existing training model that extends the abstract TrainingModel.
    """

    def __init__(self, target_mileage: float, starting_mileage: float, a: float, b: float) -> None:
        """
        Initializes the ExistingTrainingModel with the given parameters.

        Args:
            target_mileage (float): The target mileage.
            starting_mileage (float): The starting mileage.
            a (float): Parameter 'a'.
            b (float): Parameter 'b'.
        """
        super().__init__(target_mileage, starting_mileage, a, b)

    def calculate_weekly_mileage(self, n: int) -> float:
        """
        Calculates the weekly mileage for the nth week.

        Args:
            n (int): The week number.

        Returns:
            float: The mileage for the nth week.
        """
        return self.target_mileage - (self.target_mileage - self.starting_mileage) * (self.a ** (n / self.b))

    def inverse_transform(self, weekly_mileage: float) -> float:
        """
        Performs inverse transformation on the weekly mileage.

        Args:
            weekly_mileage (float): The weekly mileage.

        Returns:
            float: The current week n.
        """
        if weekly_mileage == self.target_mileage:
            return float('inf')
        else:
            return self.b * math.log((self.target_mileage - weekly_mileage) / (self.target_mileage - self.starting_mileage), self.a)

    def rate_of_change(self, n: int) -> float:
        """
        Calculates the rate of change in mileage for the nth week.

        Args:
            n (int): The week number.

        Returns:
            float: The rate of change.
        """
        return -(((self.target_mileage - self.starting_mileage) * math.log(self.a) * (self.a ** (n / self.b))) / self.b)

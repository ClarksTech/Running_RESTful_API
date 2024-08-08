# training_model/new_model.py
from .base_model import TrainingModel

class NewTrainingModel(TrainingModel):
    """
    New training model that extends the abstract TrainingModel.
    """

    def __init__(self, target_mileage: float, starting_mileage: float, a: float, b: float) -> None:
        """
        Initializes the NewTrainingModel with the given parameters.

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
        return min(self.starting_mileage + (self.a * n) / self.b, self.target_mileage)

    def inverse_transform(self, weekly_mileage: float) -> float:
        """
        Performs inverse transformation on the weekly mileage.

        Args:
            weekly_mileage (float): The weekly mileage.

        Returns:
            float: The current week n.
        """
        return (weekly_mileage - self.starting_mileage) * self.b / self.a

    def rate_of_change(self, n: int) -> float:
        """
        Calculates the rate of change in mileage for the nth week.

        Args:
            n (int): The week number.

        Returns:
            float: The rate of change.
        """
        if (self.starting_mileage + (self.a * n) / self.b) < self.target_mileage:
            return self.a / self.b
        else:
            return 0

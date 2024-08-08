import unittest
from abc import ABC
from typing import Type, Dict, List, Tuple

class BaseTestTrainingModel(unittest.TestCase, ABC):
    """
    Base test class for TrainingModel tests.

    Attributes:
        model_class (type): The class of the model to be tested.
        model_args (dict): The arguments to initialize the model.
        weekly_mileage_tests (list): List of tuples containing week number and expected weekly mileage.
        inverse_transform_tests (list): List of tuples containing weekly mileage and expected week number.
        rate_of_change_tests (list): List of tuples containing week number and expected rate of change.
    """
    
    model_class: Type = None
    model_args: Dict[str, float] = {}
    weekly_mileage_tests: List[Tuple[int, float]] = []
    inverse_transform_tests: List[Tuple[float, int]] = []
    rate_of_change_tests: List[Tuple[int, float]] = []

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up the model instance for the test class.
        """
        print(f"Setting up {cls.__name__}")
        if cls is BaseTestTrainingModel:
            raise unittest.SkipTest("Skipping BaseTestTrainingModel tests (base class)")
        if cls.model_class is None:
            raise TypeError("model_class is not set")
        cls.model = cls.model_class(**cls.model_args)


    def test_calculate_weekly_mileage(self) -> None:
        """
        Test the calculate_weekly_mileage method of the model.
        """
        for week, expected in self.weekly_mileage_tests:
            with self.subTest(week=week):
                self.assertAlmostEqual(self.model.calculate_weekly_mileage(week), expected, places=1)

    def test_inverse_transform(self) -> None:
        """
        Test the inverse_transform method of the model.
        """
        for mileage, expected in self.inverse_transform_tests:
            with self.subTest(mileage=mileage):
                self.assertAlmostEqual(self.model.inverse_transform(mileage), expected, places=1)

    def test_rate_of_change(self) -> None:
        """
        Test the rate_of_change method of the model.
        """
        for week, expected in self.rate_of_change_tests:
            with self.subTest(week=week):
                self.assertAlmostEqual(self.model.rate_of_change(week), expected, places=1)

import unittest
from training_model.new_model import NewTrainingModel
from tests.base_unit_test import BaseTestTrainingModel
from typing import Dict, List, Tuple

class TestNewTrainingModel(BaseTestTrainingModel):
    """
    Test class for the NewTrainingModel.
    """
    
    model_class = NewTrainingModel
    model_args: Dict[str, float] = {'target_mileage': 200, 'starting_mileage': 20, 'a': 0.3, 'b': 3}
    weekly_mileage_tests: List[Tuple[int, float]] = [(7, 20.7), (0, 20), (1, 20.1)]
    inverse_transform_tests: List[Tuple[float, float]] = [(120, 1000), (200, 1800), (20, 0)]
    rate_of_change_tests: List[Tuple[int, float]] = [(4, 0.1), (1850, 0), (0, 0.1)]

    def test_calculate_weekly_mileage(self) -> None:
        super().test_calculate_weekly_mileage()
    
    def test_inverse_transform(self) -> None:
        super().test_inverse_transform()
    
    def test_rate_of_change(self) -> None:
        super().test_rate_of_change()

if __name__ == '__main__':
    unittest.main()

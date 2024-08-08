import unittest
from training_model.existing_model import ExistingTrainingModel
from tests.base_unit_test import BaseTestTrainingModel
from typing import Dict, List, Tuple

class TestExistingTrainingModel(BaseTestTrainingModel):
    """
    Test class for the ExistingTrainingModel.
    """
    
    model_class = ExistingTrainingModel
    model_args: Dict[str, float] = {'target_mileage': 50, 'starting_mileage': 10, 'a': 0.9, 'b': 5}
    weekly_mileage_tests: List[Tuple[int, float]] = [(10, 17.6), (0, 10.0), (1, 10.83)]
    inverse_transform_tests: List[Tuple[float, float]] = [(17.6, 10.0), (50, float('inf')), (12.5, 3.06)]
    rate_of_change_tests: List[Tuple[int, float]] = [(7, 0.7464), (0, 0.8428)]
    
    def test_calculate_weekly_mileage(self) -> None:
        super().test_calculate_weekly_mileage()
    
    def test_inverse_transform(self) -> None:
        super().test_inverse_transform()
    
    def test_rate_of_change(self) -> None:
        super().test_rate_of_change()

if __name__ == '__main__':
    unittest.main()


from flask import request
from flask_restful import Resource
from abc import ABC, abstractmethod
import os
from typing import Tuple

class BaseTransform(Resource, ABC):
    """
    Abstract base class for API endpoint transform resources.
    """

    def __init__(self, **kwargs: dict) -> None:
        self.training_model_class = kwargs['training_model']

    def get_parameters(self) -> Tuple[float, float, float, float]:
        """
        Retrieve parameters from the request or environment variables.
        """
        target_mileage = float(request.args.get('target_mileage', os.getenv('TARGET_MILEAGE')))
        starting_mileage = float(request.args.get('starting_mileage', os.getenv('STARTING_MILEAGE')))
        a = float(request.args.get('a', os.getenv('A')))
        b = float(request.args.get('b', os.getenv('B')))
        return target_mileage, starting_mileage, a, b

    @abstractmethod
    def get(self) -> None:
        """
        Handle GET requests (to be implemented by subclasses).
        """
        pass

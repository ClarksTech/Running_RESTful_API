from flask import jsonify, request
from .base_transform import BaseTransform
from typing import Dict

class RateOfChange(BaseTransform):
    """
    API resource returning rate of change for a given week.
    """

    def get(self) -> Dict[str, str]:
        """
        Handle GET request, return rate of change for week n.
        """
        n = int(request.args.get('n'))
        target_mileage, starting_mileage, a, b = self.get_parameters()
        model = self.training_model_class(target_mileage, starting_mileage, a, b)
        rate = model.rate_of_change(n)
        return jsonify({'week': n, 'rate_of_change': format(rate, ".2f")})

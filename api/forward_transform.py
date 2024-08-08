from flask import jsonify, request
from .base_transform import BaseTransform
from typing import Dict

class ForwardTransform(BaseTransform):
    """
    API resource returning weekly mileage for a given week.
    """

    def get(self) -> Dict[str, str]:
        """
        Handle GET request, return weekly mileage for week n.
        """
        n = int(request.args.get('n'))
        target_mileage, starting_mileage, a, b = self.get_parameters()
        model = self.training_model_class(target_mileage, starting_mileage, a, b)
        weekly_mileage = model.calculate_weekly_mileage(n)
        return jsonify({'week': n, 'weekly_mileage': format(weekly_mileage, ".2f")})
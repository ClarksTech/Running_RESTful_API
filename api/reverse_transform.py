from flask import jsonify, request
from .base_transform import BaseTransform
from typing import Dict

class ReverseTransform(BaseTransform):
    """
    API resource returning training week for a given weekly mileage.
    """

    def get(self) -> Dict[str, str]:
        """
        Handle GET request, return week n for given weekly mileage.
        """
        weekly_mileage = float(request.args.get('weekly_mileage'))
        target_mileage, starting_mileage, a, b = self.get_parameters()
        model = self.training_model_class(target_mileage, starting_mileage, a, b)
        week = model.inverse_transform(weekly_mileage)
        return jsonify({'weekly_mileage': weekly_mileage, 'n': format(week, ".2f")})

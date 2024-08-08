from flask import Flask
from flask_restful import Api
import os
from dotenv import load_dotenv
from training_model.existing_model import ExistingTrainingModel
from training_model.new_model import NewTrainingModel
from api.forward_transform import ForwardTransform
from api.reverse_transform import ReverseTransform
from api.rate_of_change import RateOfChange

# Load environment variables from .env file
load_dotenv('.env')

# Determine which model to use based on the environment variable
chosen_model = os.getenv('TRAINING_MODEL')

if chosen_model == '0':
    TrainingModelClass = ExistingTrainingModel
elif chosen_model == '1':
    TrainingModelClass = NewTrainingModel
else:
    raise ValueError(f"Unsupported value for TRAINING_MODEL environment variable: {chosen_model}")

# Flask app setup
app = Flask(__name__)
api = Api(app)

# Setup the three API endpoints, passing the model class for class-based dependency injection
api.add_resource(ForwardTransform, '/forward_transform', resource_class_kwargs={'training_model':TrainingModelClass})
api.add_resource(ReverseTransform, '/reverse_transform', resource_class_kwargs={'training_model':TrainingModelClass})
api.add_resource(RateOfChange, '/rate_of_change', resource_class_kwargs={'training_model':TrainingModelClass})

if __name__ == "__main__":
    app.run()


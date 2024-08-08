# Running_RESTful_API

## Background

Consider an equation that determines a runner's `weekly_mileage` for a given week `n` of their training plan:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Equation 1: `weekly_mileage`=`target_mileage`−(`target_mileage`−`starting_mileage`) * `a` ^ (`n`/`b`)
Equation 2: `weekly_mileage` = min(`starting_mileage` + (`a` * `n`) / `b`, `target_mileage`)

Where:
- `n` is the week number (in the first week `n==0`).
- `target_mileage` is the weekly mileage they would build to, given infinite training time.
- `starting_mileage` is their starting mileage in the first week (`n==0`).
- `a` is a parameter that governs the shape of the curve i.e. how the runner's weekly mileage progresses. 
    - `0 < a < 1`.
- `b` is a parameter that governs the shape of the curve i.e. how the runner's weekly mileage progresses.
    - `b > 0`.

# Instructions
This segment contains instructions on how to:
- Setup and run the code
- Perform tests
- Query the endpoints

# NOTE on rate of change calculation
The exact rate of change has been implemented (i.e. differential over infinity small interval).
- This was selected over an approximation as the data is:
    1. Very clean - these are outputs from data models with no noise hence exact rate of change cannot be disrupted by local noise
    2. Equation 1 is an exponential curve - no artifacts that can cause miss-representative gradients
    3. Equation 2 is linear to a point where it becomes flat - no artifacts capable of causing miss-representative gradients

## SETUP AND RUN THE CODE
1. SETUP
    - This project uses poetry for dependency management so please make sure poetry is installed using the following command:

    - Windows:
    ```ps1
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
    ```
    - Linux, macOS, Windows (WSL)
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
    - Ensure poetry is added to your PATH and run the following command to install all program dependencies:
    ```bash
    poetry install --no--root
    ```
2. RUNNING
    - To run the API on a development server (localhost) first activate the python environment with the following command:
    ```bash
    poetry shell
    ```
    - Next run the flask app using the following command:
    ```bash
    poetry run python app.py
    ```
    - The API will now be running on port 5000 of localhost and ready to receive client queries

The API is running on a development server not intended for deployment, given more time a production server would be used.
The API would also need key and request quotas implementing

## PERFORMING TESTS
1. UNIT TESTS
    - To run the unit tests ensure you are in the root directory
    - Activate the poetry environment using the following command:
    ```bash
    poetry shell
    ```
    - Run all unit tests using the following command:
    ```bash
    pytest -v
    ```
    - Note the BaseTestTrainingModel is intentionally skipped as it is an abstract base class

2. E2E API TESTS

    SETUP
    - E2E API testing is achieved using Postman so please ensure you have downloaded the desktop application or vs code extension
    - Open the desktop application or vs code extension of Postman
    - click import collection and browse to the two provided .json collections:
        - '/tests/api_tests_postman_collection_existing_model.json' 
        - '/tests/api_tests_postman_collection_new_model.json'
    - import the collections

    NOTE: 
    - The API development server will need re-starting each time the 'TRAINING_MODEL' env variable is changed
    - vscode may also need closing and re-opening for the change to take effect
        - This is important otherwise the API will still be running on the old env variable causing E2E tests to fail
        - Given more time this could be developed using flask fixture to auto build and teardown the API

    RUNNING FOR EXISTING TRAINING MODEL
    - Ensure environmental variable 'TRAINING_MODEL' is set to '= 0' in the .env file
    - Run the API on the development server as per 'SETUP AND RUN THE CODE'
    - Open Postman collection 'API Test Existing Model'
    - Click Run > Run manually

    RUNNING FOR NEW TRAINING MODEL
    - Ensure environmental variable 'TRAINING_MODEL' is set to '= 1' in the .env file
    - Run the API on the development server as per 'SETUP AND RUN THE CODE'
    - Open Postman collection 'API Test New Model'
    - Click Run > Run manually

Given more time all tests could be automated to run on any code changes

## QUERY THE ENDPOINT
1. ENDPOINT QUERY FORMAT:
    - The endpoints are queried using HTTP GET requests in the following formats (shown with default arguments):
        - Weekly Mileage = 
        
        http://127.0.0.1:5000/forward_transform?n=10&target_mileage=50&starting_mileage=10&a=0.9&b=5
        - Week Number = 
        
        http://127.0.0.1:5000/reverse_transform?weekly_mileage=12.5&target_mileage=50&starting_mileage=10&a=0.9&b=5
        - Week rate of change = 
        
        http://127.0.0.1:5000/rate_of_change?n=7&target_mileage=50&starting_mileage=10&a=0.9&b=5
2. Querying the endpoints
    - Run the API on the development server as per 'SETUP AND RUN THE CODE'
    - Open a browser and enter an endpoint from above (editing or omitting arguments where desired to change output)
        - the page will display the returned json dict
    - Alternatively an example python script 'query_endpoints.py' has been included to demonstrate querying each endpoint
        - with the API running on the development server first activate the python environment with the following command:
        ```bash
        poetry shell
        ```
        - Next run the following command to query the endpoints using the 'query_endpoints.py' script
        ```bash
        poetry run python query_endpoints.py
        ```

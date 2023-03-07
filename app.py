# Importing Necessary modules
from fastapi import FastAPI
import uvicorn
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from pydantic import BaseModel, constr, conlist
from typing import List


# Creating class to define the request body
# and the type hints of each attribute
class request_body(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# Loading Iris Dataset
iris = load_iris()

# Getting our Features and Targets
X = iris.data
Y = iris.target

# Creating and Fitting our Model
clf = GaussianNB()
clf.fit(X, Y)


# Declaring our FastAPI instance
app = FastAPI()

# Defining path operation for root endpoint


@app.get('/')
def main():
    return {'message': 'Welcome to GeeksforGeeks!'}

# Defining path operation for /name endpoint


@app.get('/{name}')
def hello_name(name: str):
    # Defining a function that takes only string as input and output the
    # following message.
    return {'message': f'Welcome to GeeksforGeekss!, {name}'}


# Creating an Endpoint to receive the data
# to make prediction on.


@app.post('/predict')
def predict(data: request_body):
    # Making the data in a form suitable for prediction
    test_data = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    # Predicting the Class
    class_idx = clf.predict(test_data)[0]

    # Return the Result
    return {'class': iris.target_names[class_idx]}

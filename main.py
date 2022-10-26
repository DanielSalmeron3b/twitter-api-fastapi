# Python
import json
from typing import List
from uuid import uuid4

# FastAPI
from fastapi import (
    FastAPI, status,
    Body
    )

app = FastAPI()

# Import models
from models import User, UserBase, UserLogin, UserRegister
from models import Tweet

# Path Operations


## Users

### Register a user
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"],
)
def signup(user: UserRegister = Body(...)):
    """
    Signup

    This path operation registers a user in the app and saves it to the database.

    Parameters:
        - Request body parameter
            - user: UserRegister

    Returns a JSON with the basic user information:
        - user_id : UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    with open("users.json", "r+", encoding="utf-8") as file:
        results = json.load(file)
        user_dict = user.dict() # Creating a dict from the Request Body
        user_dict["user_id"] = str(uuid4())
        user_dict["birth_date"] = str(user_dict["birth_date"])
        user_dict["gender"] = str(user_dict["gender"])
        results.append(user_dict) # Adding the new user to the dict
        file.seek(0) # Moving to the beginning of the file to keep appending elements to it
        json.dump(results, file) # Writing the results in the JSON file/"database"

    return user

### Login a user
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"],
)
def login():
    pass

### Show all users
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"],
)
def show_all_users():
    pass

### Show a registered user
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show an User",
    tags=["Users"],
)
def show_user():
    pass

### Delete an existing user
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete an User",
    tags=["Users"],
)
def delete_user():
    pass

### Update an existing user
@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update an User",
    tags=["Users"],
)
def update_user():
    pass


## Tweets

### Show all tweets
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show Tweets",
    tags=["Tweets"],
    )
def home():
    return {"Twitter API": "Working!"}

### Post a tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a Tweet",
    tags=["Tweets"],
)
def post_tweet():
    pass

### Show a tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Post a Tweet",
    tags=["Tweets"],
)
def show_tweet():
    pass

### Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a Tweet",
    tags=["Tweets"],
)
def delete_tweet():
    pass

### Update a tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a Tweet",
    tags=["Tweets"],
)
def delete_tweet():
    pass
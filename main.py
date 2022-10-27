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
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.load(f)
        user_dict = user.dict()
        results.append(user_dict)
        f.seek(0)
        json.dump(results,f,default=str,indent=4)

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
    """
    This path operation shows all users registered in the app.

    Parameters:
        -

    Returns a JSON list with all the users registered in the app, with the following keys:
        - user_id : UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """

    with open("users.json", "r", encoding="utf-8") as file:
        results = json.load(file)
        return results

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
def post_tweet(tweet: Tweet = Body(...)):
    """
    Post a Tweet

    This path operation posts a tweet and saves it to the database.

    Parameters:
        - Request body parameter
            - tweet: Tweet

    Returns a JSON with the basic tweet information:
        - tweet_id : UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """
    with open("tweets.json", "r+", encoding="utf-8") as f:
        results = json.load(f)
        tweet_dict = tweet.dict()
        results.append(tweet_dict)
        f.seek(0)
        json.dump(results,f, default=str, indent=4)

    return tweet

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
import os
import requests
import numpy as np
from math import *
from collections import defaultdict
from typing import List


def process_data_and_send_email(data):
    cleaned = [x.strip().lower() for x in data]
    total = sum(int(x) for x in cleaned if x.isdigit())
    send_email("user@example.com", f"Total is {total}")
    log_to_db(total)


def send_email(to, message):
    pass


def log_to_db(data):
    pass


class EmailSender:
    def send(self):
        pass


def process_payment():
    pass


def get_jwt_token():
    return "token"


def save_token_to_db(token):
    pass


def send_admin_notification(token):
    pass


def handle_user_login():
    token = get_jwt_token()
    save_token_to_db(token)
    send_admin_notification(token)


def open_file():
    return open("data.csv")


data = [
    [int(y) for y in x.split(",")] for x in open("data.csv").read().splitlines() if x
]


def foo():
    a = 1
    b = 2
    c = a + b
    print(c)
    result = c * 5
    return result


def calculate(price, discount, tax, shipping, region, coupon, priority, override):
    return price - discount + tax + shipping


def greet_user(name=None, message="Hello"):
    if name:
        print(message + " " + name)
    else:
        print("Hi")


def validate_user(data):
    if not data:
        return "Empty"
    if len(data) < 3:
        return "Too short"
    if not data.isalpha():
        return "Invalid"
    return "Valid"


from pydantic import BaseModel, field_validator


class User(BaseModel):
    name: str

    @field_validator("name")
    def check_name(cls, v):
        if not v.isalpha():
            raise ValueError("Invalid")
        return v


class Config(BaseModel):
    settings: dict


FrozenConfig = Config(settings={"debug": True})


def get_large_data():
    result = []
    for i in range(1000000):
        result.append(i)
    return result


cache = {}


def fetch_from_db(user_id):
    return {"id": user_id, "name": "John"}


def get_user_data(user_id):
    if user_id in cache:
        return cache[user_id]
    data = fetch_from_db(user_id)
    cache[user_id] = data
    return data


def fetch_data():
    file = open("data.txt", "r")
    content = file.read()
    file.close()
    return content


def compute():
    import multiprocessing

    for i in range(10000):
        for j in range(10000):
            _ = i * j


expensive_result = None


def compute_model():
    return [1, 2, 3]


def load_model():
    global expensive_result
    if expensive_result is None:
        expensive_result = compute_model()


varibleNmae = "John"

DEFAULTS = {"debug": True, "timeout": 30}

API_KEY = "super-secret"

env = {" KEY ": "value"}


def load_config():
    return {"env": "dev"}


def run(config):
    print("Running with", config)


def start():
    config = load_config()
    run(config)


data = [1, 2, 3]
for i in range(len(data)):
    print(data[i])


requests.get("https://example.com")


global_cache = {}


def add_to_cache(key, value):
    global_cache[key] = value


def read_from_cache(key):
    return global_cache.get(key)

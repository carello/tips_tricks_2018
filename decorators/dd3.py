from dd1 import debug, timer, do_twice, repeat, count_calls, slow_down2, singleton, cache

import functools

@count_calls
def greet(name):
    print(f"Hello {name}")

#greet("chet")
#greet("chet")
#greet("chet")

class Counter(object):
    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        self.count += 1
        print(f"The current count is {self.count}")
#counter = Counter()
#counter()
#counter()
#print(counter.count)

class CountCalls(object):
    def __init__(self, func):
        functools.wraps(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)
@CountCalls
def say_whee():
    print("Whee!")
#say_whee()
#say_whee()
#print(say_whee.num_calls)

@slow_down2()
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)
#countdown(3)

@singleton
class TheOne:
    pass

#first_one = TheOne()
#another_one = TheOne()
#print(id(first_one))
#print(id(another_one))
#print(first_one is another_one)

@cache
@count_calls
def fib(num):
    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)

#fib(10)
#print(fib.num_calls)
#fib(18)
#print(fib.num_calls)


@functools.lru_cache(maxsize=6)
def fibonacci(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

#fibonacci(10)
#fibonacci(8)
#fibonacci(5)
#fibonacci(8)
#fibonacci(5)
#print(fibonacci.cache_info())


##############
from flask import Flask, request, abort
import functools
#app = Flask(__name__)


def validate_json(*expected_args):                  # 1
    def decorator_validate_json(func):
        @functools.wraps(func)
        def wrapper_validate_json(*args, **kwargs):
            #json_object = request.get_json()
            json_object = {"student_idx": 101}
            for expected_arg in expected_args:      # 2
                if expected_arg not in json_object:
                    abort(400)
            return func(*args, **kwargs)
        return wrapper_validate_json
    return decorator_validate_json


#@app.route("/grade", methods=["POST"])
@validate_json("student_id")
def update_grade():
    #json_data = request.get_json()
    json_data = {"student_id": 100}
    # Update database.
    print(json_data)
    return "success!"

print(update_grade())
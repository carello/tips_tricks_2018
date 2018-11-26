from dd1 import do_twice, timer, debug, slow_down
import random
PLUGINS = dict()


def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func


@do_twice
def say_whee(name):
    print("Creating Greeting...")
    return "Whee! {}".format(name)
#print(say_whee("chet"))

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        result = sum([i**2 for i in range(1000)])
        return result
#print(waste_some_time(1))
#waste_some_time(999)

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are grown"
#make_greeting("chet")
#make_greeting("connie", age=112)

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("LIFTOFF!!!")
    else:
        print(from_number)
        countdown(from_number - 1)
#countdown(3)

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"You {name}, you are awesome!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)
#print(PLUGINS)
#print(randomly_greet("Alice"))
#print(globals())


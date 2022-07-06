from functools import wraps


def type_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Call for: {func.__name__}")
        print(", ".join([f"{i}: {type(i)}" for i in args]))
        if len(kwargs) > 0:
            print(", ".join([f"'{key}' = {val}: {type(val)}" for key, val in kwargs.items()]))
        result = func(*args)
        print(f"Rezult: {result}  type: {type(result)}")
        return result
    return wrapper


@type_logger
def render_input(*args, **kwargs):
   return 1

@type_logger
def calc_cube(x):
   return x**3

render_input(1,2,3)
render_input(1,2,"new")
render_input(1, a = 2, b = True, c = "q")

calc_cube(5)



def val_checker(func_checker):
    def decorator_simple(source_func):
        def wrapper(*args, **kwargs):
            if func_checker(*args):
                return source_func(*args, **kwargs)
            else:
                raise ValueError
        return wrapper
    return decorator_simple



@val_checker(lambda x: x>0)
def calc_cube(x):
   return x**3
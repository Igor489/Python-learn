def val_checker(validator_func):

    def decorator(func):

        def validated_func(*args, **kwargs):
            if validator_func(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                raise ValueError(f'{validator_func}.__name__ failed')

        return validated_func

    return decorator

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

print(calc_cube(5))
print(calc_cube(-5))

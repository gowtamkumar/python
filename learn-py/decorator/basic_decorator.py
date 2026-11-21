from functools import wraps


def my_decorator(func):

  @wraps(func)
  def wrapper():
    print("Before function runs")
    func()
    print("after function runs")
    
  return wrapper


@my_decorator
def greet():
  print("Hello From Decorators class from chaicode")
  
  
greet()


print(greet.__name__)
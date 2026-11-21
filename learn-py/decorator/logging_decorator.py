from functools import wraps


def log_activity(func):
  
  @wraps(func)  
  def wrapper(*args, **kwards):
    print(f"Calling: {func.__name__} ")
    result = func(*args, **kwards)
    print(f"Finished: {func.__name__}")
    return result
  
  return wrapper

@log_activity
def brew_chai(type, milk="No"):
  print(f"Brewing {type} chai with milk {milk}")
  
brew_chai("Masala", "Yes")
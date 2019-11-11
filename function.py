# Complete this function to return either
# "Hello, [name]!" or "Hello there!"
# based on the input

def say_hello(name):
  # you can print to STDOUT to debug if you need to:
  print(name)
  
  # but to complete the challenge you need to return a value
  if name:
    return "Hello, " + name + "!"
  else: 
    return "Hello there!"
  

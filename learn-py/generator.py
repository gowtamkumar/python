def serve_chai():
  yield "Cup 1: Masala Chai"
  yield "Cup 2: Ginger Chai"
  yield "Cup 3: Elaichi Chai"


for i in serve_chai():
  print(i)
  
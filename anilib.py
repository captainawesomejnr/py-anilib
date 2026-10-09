def typewriter(text, duration, trailing = "\n"):
    for char in text:
      print(char, end = "")
    print("", end = trailing)


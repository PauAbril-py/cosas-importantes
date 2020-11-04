import time

st = 0.04
def p(str, x):
  if x == 1:
    for letter in str:
      sys.stdout.write(bright_blue + letter)
      sys.stdout.flush()
      time.sleep(st)
    print()
  else:
    for letter in str:
      sys.stdout.write(bright_blue + letter)
      sys.stdout.flush()
      time.sleep(st)
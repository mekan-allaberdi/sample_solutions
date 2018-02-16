# python3

from datetime import datetime as dt

def time_delta(t1, t2):
    format = '%a %d %b %Y %H:%M:%S %z'
    diff = abs((dt.strptime(t1, format) - dt.strptime(t2, format)))
    return int(diff.total_seconds())

if __name__ == "__main__":
  t1 = 'Fri 16 Feb 2017 17:34:20 -0500'
  t2 = 'Fri 15 Feb 2017 15:34:20 +0330'
  delta = time_delta(t1, t2)
  print(delta)

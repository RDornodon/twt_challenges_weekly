import time
from typing import final

@final
def sleep(self):
  time.sleep(0.1)


class slowlist(list):
  @final
  def __next__(self):
    sleep()
    return self.__iter.__next__()

  @final
  def __getitem__(self, item):
    sleep()
    return super().__getitem__(item)

  @final
  def index(*_):
    raise Exception("Do not use index!")

  @final
  def __iter__(self):
    self.__iter = super().__iter__()
    return self


# class self-test
if __name__ == '__main__':
  t = time.time()
  l = slowlist(range(100))
  L = [*l]
  print(l[3], l[5], l[7], l[11], l[44])
  print(f'{time.time() - t:.2f} secs elapsed')

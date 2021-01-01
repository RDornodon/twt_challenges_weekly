import time


class slowlist(list):
  def __next__(self):
    time.sleep(0.01)
    return self.__iter.__next__()

  def __getitem__(self, item):
    time.sleep(0.01)
    return super().__getitem__(item)

  def index(self, __value, __start=..., __stop=...):
    raise Exception("Do not use index!")

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

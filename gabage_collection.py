# import sys
# x = [1, 2, 3]
# print(f"xの参照カウント：{sys.getrefcount(x) - 1}")
# y = x
# print(f"xの参照カウント：{sys.getrefcount(x) - 1}")

import trace
import tracemalloc
tracemalloc.start()

def foo():
  x = [0] * (10**6)
  y = x
  ss = tracemalloc.take_snapshot()
  for s in ss.statistics("filename"):
    print('関数内',s)

foo()
ss = tracemalloc.take_snapshot()
for s in ss.statistics("filename"):
    print('関数外',s)

tracemalloc.stop()
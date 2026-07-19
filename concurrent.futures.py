from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

def func_1(x):
  for n in range(3):
    time.sleep(2)
    print(f'func_1 - {n} ({x})')
  return f'結果-{x}'

# def func_2(x, y):
#   for n in range(3):
#     time.sleep(1)
#     print(f'func_2 - {n} ({x}, {y})')
#   return '結果2'

def main():
  print('start')
  with ProcessPoolExecutor(max_workers=4) as executor:
    # for arg in ['A', 'B', 'C', 'D']:
    #   executor.submit(func_1, arg)

    results = executor.map(func_1, ['A', 'B', 'C', 'D'])
    print(list(results))
  # with ThreadPoolExecutor(max_workers=2) as executor:
  #   future_1 = executor.submit(func_1)
  #   future_2 = executor.submit(func_2, 'A' , 'B')
  #   future_2 = executor.submit(func_2, 'C' , 'D')
  
  # result_1=future_1.result()
  # result_2=future_2.result()

  # print(f'result_1: {result_1}')
  # print(f'result_2: {result_2}')

  print('fin')

if __name__ == '__main__':
  main()

# 関数のオブジェクト化
# 関数内関数

# def print_apple():
#   print('これはりんごです')

# # func = print_apple
# def repeat_func_twice(func):
#   func()
#   func()

# repeat_func_twice(print_apple)

# def print_text_twice(text):
#   def add_exclamation(text):
#     return text + '!'

#   text_e = add_exclamation(text)
#   print(text)
#   print(text_e)

# print_text_twice('これはりんごです')


# 関数のスコープ

# x = 'これはりんごです'

# def func():
#   print(x)

# func()

def start_end(func):
  def add_start_end(_text):
    print('start')
    func(_text)
    print('end')
  return add_start_end

@start_end
def print_text(text):
  print(text + '!')

print_text('これはりんごです')

# def print_apple():
#   print('これはりんごです')

# print_apple()

# start_end(print_apple)()
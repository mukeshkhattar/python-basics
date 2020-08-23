#function within function
def operator(op_text):
  def add_num(num1,num2):
    return num1+num2
  def subtract_num(num1,num2):
    return num1-num2
  if op_text == '+':
    return add_num
  elif op_text == '-':
    return subtract_num
  else:
    return None

# driver code
if __name__ == '__main__':
  add_fn=operator('-')
  x=add_fn(4,6)
  print(x) # prints -2

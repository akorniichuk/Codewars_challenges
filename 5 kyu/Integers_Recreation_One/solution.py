def list_squared(m, n):

  def calculate_divisors(num):
    divisors = []
    sqrt = round(num**0.5)
    for i in range(1, sqrt+1):
      if num%i == 0:
        div = num / i
        if div == i:
          divisors.append(int(div))
        else:
          divisors.append(int(div))
          divisors.append(int(i))
    return divisors

  def sum_squared_elements(lst):
    squared_elements = []
    for elem in lst:
      squared_elements.append(elem**2)
    return sum(squared_elements)

  final_result = []
  if m >=1 and (n >= 1 and n >= m):
    numbers = list(range(m,n+1))
    for number in numbers:
      final_divisors = calculate_divisors(number)
      sum_squared = sum_squared_elements(final_divisors)
      root = sum_squared**0.5
      if root%round(root) == 0:
        result = [number, sum_squared]
        final_result.append(result)

  return final_result
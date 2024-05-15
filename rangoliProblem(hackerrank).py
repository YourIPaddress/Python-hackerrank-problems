# By entering a number as an input, the following code generates a rangoli using enlish alphabets and creates a cool diamond pattern :)

def print_rangoli(size):
  alphabet = [chr(i) for i in range(97, 123)]
  alphabet = alphabet[:size]
  indices = list(range(size))
  indices = indices[:-1] + indices[::-1]
  for i in indices:
    start_index = i + 1
    original = alphabet[-start_index:]
    reverse = original[::-1]
    row = reverse + original[1:]
    row = "-".join(row)
    width = size*4 - 3
    row = row.center(width, "-")
    print(row)


n = int(input())
print_rangoli(n)
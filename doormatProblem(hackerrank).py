#give inputs such that M = 3 times of N
N, M = input().split()
N, M = int(N), int(M)
width = M
pattern = '.|.'
k = 1
halfM = (M // 2) + 2
for j in range(0, (N // 2)):
  chunk = "-" * ((halfM) -(3 * (j + 1))) + pattern * (j + k) + "-" * ((halfM) - (3 * (j + 1)))
  print(chunk)
  k += 1

print("WELCOME".center(width, '-'))
k = k - 1
for j in range((N // 2) - 1, -1, -1):
  chunk = "-" * ((halfM) - (3 * (j + 1))) + pattern * (j + k) + "-" * ((halfM) - (3 * (j + 1)))
  print(chunk)
  k -= 1

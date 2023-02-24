# Funkcja zwracająca sumę indeksów wszystkich par sumujących się do n

def get_pair_num(arr, n):
    count = 0  # rozpoczynamy zliczanie od 0
    l = len(arr) # pobieramy długośc tablicy

    for i in range(0, l):
        for j in range(i + 1, l):
            if arr[i] + arr[j] == n:
                count = count + i + j #sumowanie indeksów

    return count

print("Suma indeksów to",
      get_pair_num([7, 9, 11, 13, 15, 5, 9, 11], 16))



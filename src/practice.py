def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def custom_sort(arr):
    # Bubble sort (no built-in sort)
    arr = arr[:]  # make a copy
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    print(f"factorial(5) = {factorial(5)}")
    print(f"is_palindrome('racecar') = {is_palindrome('racecar')}")
    print(f"is_palindrome('hello world') = {is_palindrome('hello world')}")
    print(f"custom_sort([3,1,4,1,5,9,2]) = {custom_sort([3,1,4,1,5,9,2])}")
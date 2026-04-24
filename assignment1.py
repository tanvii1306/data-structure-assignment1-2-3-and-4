class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


call_naive = 0
def fib_naive(n):
    global call_naive
    call_naive += 1
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)


call_memo = 0
def fib_memo(n, memo={}):
    global call_memo
    call_memo += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


def hanoi(n, src, aux, dest):
    if n == 1:
        print(f"Move disk 1 from {src} to {dest}")
        return
    hanoi(n-1, src, dest, aux)
    print(f"Move disk {n} from {src} to {dest}")
    hanoi(n-1, aux, src, dest)

def binary_search(arr, key, low, high):
    if low > high:
        return -1
    mid = (low + high)//2
    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid-1)
    else:
        return binary_search(arr, key, mid+1, high)


if __name__ == "__main__":
    print("Factorial:", factorial(5))

    print("\nFibonacci Naive:", fib_naive(10), "Calls:", call_naive)
    print("Fibonacci Memo:", fib_memo(10), "Calls:", call_memo)

    print("\nHanoi (3 disks):")
    hanoi(3, 'A', 'B', 'C')

    arr = [1,3,5,7,9,11,13]
    print("\nBinary Search 7:", binary_search(arr, 7, 0, len(arr)-1))
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

print("calculator module loaded")
print("calculator __name__ =", __name__)

if __name__ == "__main__":
    print("calculator is running directly")
    print("Testing functions:")
    print("10 + 5 =", add(10,5))
    print("10 - 5 =", sub(10,5))

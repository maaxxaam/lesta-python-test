def isEven(value) -> bool:
	return value % 2 == 0

def isEven2(value) -> bool:
	return value & 1 == 0

print(isEven(42))
print(isEven2(42))
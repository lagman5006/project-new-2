def func1(prime: list, prime2: int)->list:
    return [prime3 for prime3 in prime if prime3 < prime2]



func2=func1([1,2,3],10)
print(func2)
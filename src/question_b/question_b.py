#write functions here, don't add input('') statements here!

def is_prime(q):
    if q <= 1:
        return False
    for i in range(2, int(q ** 0.5) + 1):
        if q % i == 0:
            return False
    return True  

import number_utils as nu

def main():
    print("=== Number Utilities Demo ===\n")
    
    # Test numbers
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 28]
    
    # Test even/odd
    print("1. Even/Odd Check:")
    for num in numbers[:5]:  # Test first 5 numbers
        print(f"   {num}: {'Even' if nu.is_even(num) else 'Odd'}")
    
    # Test prime numbers
    print("\n2. Prime Numbers (1-20):")
    primes = [num for num in range(1, 21) if nu.is_prime(num)]
    print(f"   {' '.join(map(str, primes))}")
    
    # Test perfect numbers
    print("\n3. Perfect Numbers (1-1000):")
    perfect_nums = [num for num in range(1, 1001) if nu.is_perfect(num)]
    print(f"   {' '.join(map(str, perfect_nums))}" if perfect_nums else "   No perfect numbers in this range")
    
    # Number properties
    print("\n4. Number Properties (1-20):")
    print("   Num  Even  Odd  Prime  Perfect")
    print("   " + "-" * 30)
    for num in range(1, 21):
        print(f"   {num:2d}   {str(nu.is_even(num)):5} {str(nu.is_odd(num)):5} {str(nu.is_prime(num)):6} {str(nu.is_perfect(num)):7}")
    
    # Number theory examples
    print("\n5. Number Theory Examples:")
    mersenne = 2**5 - 1  # 31 (Mersenne prime)
    print(f"   Is {mersenne} a Mersenne prime? {nu.is_prime(mersenne)}")
    
    # Fibonacci numbers
    def is_fibonacci(n):
        """Check if a number is a Fibonacci number"""
        return (5*n*n + 4) in [x*x for x in range(1, n+2)] or (5*n*n - 4) in [x*x for x in range(1, n+2)]
    
    fibs = [num for num in range(1, 21) if is_fibonacci(num)]
    print(f"   Fibonacci numbers up to 20: {' '.join(map(str, fibs))}")
    
    # Test some special cases
    print("\n6. Special Cases:")
    test_cases = [0, 1, 2, -5, 28, 496, 8128, 33550336]
    for num in test_cases:
        print(f"   {num:9d}: " +
              f"Even={str(nu.is_even(num)):5} " +
              f"Odd={str(nu.is_odd(num)):5} " +
              f"Prime={str(nu.is_prime(num)):5} " +
              f"Perfect={str(nu.is_perfect(num)):5}")
    
    # Goldbach's conjecture (even numbers > 2 can be expressed as sum of two primes)
    print("\n7. Goldbach's Conjecture Examples:")
    def goldbach(n):
        if n <= 2 or n % 2 != 0:
            return None
        for i in range(2, n//2 + 1):
            if nu.is_prime(i) and nu.is_prime(n-i):
                return (i, n-i)
        return None
    
    for num in range(4, 21, 2):
        pair = goldbach(num)
        if pair:
            print(f"   {num} = {pair[0]} + {pair[1]}")
        else:
            print(f"   {num}: No Goldbach pair found!")

if __name__ == "__main__":
    main()

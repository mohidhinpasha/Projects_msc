def find_non_primes(start, end):
 """provides a list of all non-prime numbers, inclusive, between start and finish."""
 non_primes = []
 for num in range(start, end + 1):
   is_prime = True
   for divisor in range(2, int(num**0.5) + 1):  # Optimized prime checking
     if num % divisor == 0:
       is_prime = False
       break
   if not is_prime:
     non_primes.append(num)
 return non_primes

while True:
 try:
   start_str = input("Enter the first positive integer: ")
   start = int(start_str)
   end_str = input("Enter the second positive integer: ")
   end = int(end_str)

   if start <= 0 or end <= 0:
     raise ValueError("Please enter positive integers only.")

   if start > end:
     start, end = end, start  # Swap if start is larger

   non_primes = find_non_primes(start, end)

   print("Non-prime numbers between", start, "and", end, "are:")
   count = 0
   for num in non_primes:
     print(num, end=" ")
     count += 1
     if count % 10 == 0:  # Print 10 numbers per line
       print()

   break

 except ValueError:
   print("Invalid input. Please enter positive integers only.")
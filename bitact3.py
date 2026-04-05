def reverse_bits(n):
    rev = 0
    
    while n > 0:
        bit = n % 2          
        rev = rev * 2 + bit  
        n = n // 2           
    
    return rev


nums = [13, 1, 10, 45, 100]

for num in nums:
    print(num, "->", reverse_bits(num))
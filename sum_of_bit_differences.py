numbers = list(map(int, input().split(" ")))
length_of_numbers = len(numbers)

sum_pair_bits = 0 
for i in range(0, 32):
    number_of_elements = 0
    for j in range(0, length_of_numbers):
        if((numbers[j]) & (1 << i)):
            number_of_elements+=1
    sum_pair_bits = sum_pair_bits + (number_of_elements * (length_of_numbers - number_of_elements) * 2)
print(sum_pair_bits)
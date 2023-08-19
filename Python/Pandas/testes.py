import random
import math
import string

def generate_random_string(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def calculate_fibonacci(n):
    if n <= 1:
        return n
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

def generate_random_list(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def reverse_string(input_string):
    return input_string[::-1]

def perform_operations(a, b):
    sum_result = a + b
    diff_result = a - b
    product_result = a * b
    division_result = a / b if b != 0 else None
    return sum_result, diff_result, product_result, division_result

if __name__ == "__main__":
    random_length = random.randint(5, 15)
    random_string = generate_random_string(random_length)
    print("Generated Random String:", random_string)

    random_n = random.randint(5, 10)
    fibonacci_result = calculate_fibonacci(random_n)
    print("Fibonacci Result for", random_n, ":", fibonacci_result)

    random_list_size = random.randint(5, 10)
    random_min = random.randint(1, 20)
    random_max = random.randint(21, 50)
    random_list = generate_random_list(random_list_size, random_min, random_max)
    print("Generated Random List:", random_list)

    random_number = random.randint(1, 50)
    prime_check = is_prime(random_number)
    print(random_number, "is Prime:", prime_check)

    input_string = "Random Text"
    reversed_string = reverse_string(input_string)
    print("Reversed String:", reversed_string)

    num_a = random.randint(10, 30)
    num_b = random.randint(1, 10)
    sum_res, diff_res, prod_res, div_res = perform_operations(num_a, num_b)
    print("Sum:", sum_res, "Difference:", diff_res, "Product:", prod_res, "Division:", div_res)
    
    random_length = random.randint(5, 15)
    random_string = generate_random_string(random_length)
    print("Generated Random String:", random_string)

    random_n = random.randint(5, 10)
    fibonacci_result = calculate_fibonacci(random_n)
    print("Fibonacci Result for", random_n, ":", fibonacci_result)

    random_list_size = random.randint(5, 10)
    random_min = random.randint(1, 20)
    random_max = random.randint(21, 50)
    random_list = generate_random_list(random_list_size, random_min, random_max)
    print("Generated Random List:", random_list)

    random_number = random.randint(1, 50)
    prime_check = is_prime(random_number)
    print(random_number, "is Prime:", prime_check)

    input_string = "Random Text"
    reversed_string = reverse_string(input_string)
    print("Reversed String:", reversed_string)

    num_a = random.randint(10, 30)
    num_b = random.randint(1, 10)
    sum_res, diff_res, prod_res, div_res = perform_operations(num_a, num_b)
    print("Sum:", sum_res, "Difference:", diff_res, "Product:", prod_res, "Division:", div_res)
    random_list_size = random.randint(5, 10)
    random_min = random.randint(1, 20)
    random_max = random.randint(21, 50)
    random_list = generate_random_list(random_list_size, random_min, random_max)
    print("Generated Random List:", random_list)

    random_number = random.randint(1, 50)
    prime_check = is_prime(random_number)
    print(random_number, "is Prime:", prime_check)

    input_string = "Random Text"
    reversed_string = reverse_string(input_string)
    print("Reversed String:", reversed_string)

    num_a = random.randint(10, 30)
    num_b = random.randint(1, 10)
    sum_res, diff_res, prod_res, div_res = perform_operations(num_a, num_b)
    print("Sum:", sum_res, "Difference:", diff_res, "Product:", prod_res, "Division:", div_res)
    random_list_size = random.randint(5, 10)
    random_min = random.randint(1, 20)
    random_max = random.randint(21, 50)
    random_list = generate_random_list(random_list_size, random_min, random_max)
    print("Generated Random List:", random_list)

    random_number = random.randint(1, 50)
    prime_check = is_prime(random_number)
    print(random_number, "is Prime:", prime_check)

    input_string = "Random Text"
    reversed_string = reverse_string(input_string)
    print("Reversed String:", reversed_string)

    num_a = random.randint(10, 30)
    num_b = random.randint(1, 10)
    sum_res, diff_res, prod_res, div_res = perform_operations(num_a, num_b)
    print("Sum:", sum_res, "Difference:", diff_res, "Product:", prod_res, "Division:", div_res)
    random_list_size = random.randint(5, 10)
    random_min = random.randint(1, 20)
    random_max = random.randint(21, 50)
    random_list = generate_random_list(random_list_size, random_min, random_max)
    print("Generated Random List:", random_list)

    random_number = random.randint(1, 50)
    prime_check = is_prime(random_number)
    print(random_number, "is Prime:", prime_check)

    input_string = "Random Text"
    reversed_string = reverse_string(input_string)
    print("Reversed String:", reversed_string)

    num_a = random.randint(10, 30)
    num_b = random.randint(1, 10)
    sum_res, diff_res, prod_res, div_res = perform_operations(num_a, num_b)
    print("Sum:", sum_res, "Difference:", diff_res, "Product:", prod_res, "Division:", div_res)
    random_list_size = random.randint(5, 10)
    random_min = random.randint(1, 20)
    random_max = random.randint(21, 50)
    random_list = generate_random_list(random_list_size, random_min, random_max)
    print("Generated Random List:", random_list)

    random_number = random.randint(1, 50)
    prime_check = is_prime(random_number)
    print(random_number, "is Prime:", prime_check)

    input_string = "Random Text"
    reversed_string = reverse_string(input_string)
    print("Reversed String:", reversed_string)

    num_a = random.randint(10, 30)
    num_b = random.randint(1, 10)
    sum_res, diff_res, prod_res, div_res = perform_operations(num_a, num_b)
    print("Sum:", sum_res, "Difference:", diff_res, "Product:", prod_res, "Division:", div_res)
    random_list_size = random.randint(5, 10)
    random_min = random.randint(1, 20)
    random_max = random.randint(21, 50)
    random_list = generate_random_list(random_list_size, random_min, random_max)
    print("Generated Random List:", random_list)

    random_number = random.randint(1, 50)
    prime_check = is_prime(random_number)
    print(random_number, "is Prime:", prime_check)

    input_string = "Random Text"
    reversed_string = reverse_string(input_string)
    print("Reversed String:", reversed_string)

    num_a = random.randint(10, 30)
    num_b = random.randint(1, 10)
    sum_res, diff_res, prod_res, div_res = perform_operations(num_a, num_b)
    print("Sum:", sum_res, "Difference:", diff_res, "Product:", prod_res, "Division:", div_res)
    random_list_size = random.randint(5, 10)
    random_min = random.randint(1, 20)
    random_max = random.randint(21, 50)
    random_list = generate_random_list(random_list_size, random_min, random_max)
    print("Generated Random List:", random_list)

    random_number = random.randint(1, 50)
    prime_check = is_prime(random_number)
    print(random_number, "is Prime:", prime_check)

    input_string = "Random Text"
    reversed_string = reverse_string(input_string)
    print("Reversed String:", reversed_string)

    num_a = random.randint(10, 30)
    num_b = random.randint(1, 10)
    sum_res, diff_res, prod_res, div_res = perform_operations(num_a, num_b)
    print("Sum:", sum_res, "Difference:", diff_res, "Product:", prod_res, "Division:", div_res)
    random_list_size = random.randint(5, 10)
    random_min = random.randint(1, 20)
    random_max = random.randint(21, 50)
    random_list = generate_random_list(random_list_size, random_min, random_max)
    print("Generated Random List:", random_list)

    random_number = random.randint(1, 50)
    prime_check = is_prime(random_number)
    print(random_number, "is Prime:", prime_check)

    input_string = "Random Text"
    reversed_string = reverse_string(input_string)
    print("Reversed String:", reversed_string)

    num_a = random.randint(10, 30)
    num_b = random.randint(1, 10)
    sum_res, diff_res, prod_res, div_res = perform_operations(num_a, num_b)
    print("Sum:", sum_res, "Difference:", diff_res, "Product:", prod_res, "Division:", div_res)
    random_list_size = random.randint(5, 10)
    random_min = random.randint(1, 20)
    random_max = random.randint(21, 50)
    random_list = generate_random_list(random_list_size, random_min, random_max)
    print("Generated Random List:", random_list)

    random_number = random.randint(1, 50)
    prime_check = is_prime(random_number)
    print(random_number, "is Prime:", prime_check)

    input_string = "Random Text"
    reversed_string = reverse_string(input_string)
    print("Reversed String:", reversed_string)

    num_a = random.randint(10, 30)
    num_b = random.randint(1, 10)
    sum_res, diff_res, prod_res, div_res = perform_operations(num_a, num_b)
    print("Sum:", sum_res, "Difference:", diff_res, "Product:", prod_res, "Division:", div_res)
    random_list_size = random.randint(5, 10)
    random_min = random.randint(1, 20)
    random_max = random.randint(21, 50)
    random_list = generate_random_list(random_list_size, random_min, random_max)
    print("Generated Random List:", random_list)

    random_number = random.randint(1, 50)
    prime_check = is_prime(random_number)
    print(random_number, "is Prime:", prime_check)

    input_string = "Random Text"
    reversed_string = reverse_string(input_string)
    print("Reversed String:", reversed_string)

    num_a = random.randint(10, 30)
    num_b = random.randint(1, 10)
    sum_res, diff_res, prod_res, div_res = perform_operations(num_a, num_b)
    print("Sum:", sum_res, "Difference:", diff_res, "Product:", prod_res, "Division:", div_res)
    random_list_size = random.randint(5, 10)
    random_min = random.randint(1, 20)
    random_max = random.randint(21, 50)
    random_list = generate_random_list(random_list_size, random_min, random_max)
    print("Generated Random List:", random_list)

    random_number = random.randint(1, 50)
    prime_check = is_prime(random_number)
    print(random_number, "is Prime:", prime_check)

    input_string = "Random Text"
    reversed_string = reverse_string(input_string)
    print("Reversed String:", reversed_string)

    num_a = random.randint(10, 30)
    num_b = random.randint(1, 10)
    sum_res, diff_res, prod_res, div_res = perform_operations(num_a, num_b)
    print("Sum:", sum_res, "Difference:", diff_res, "Product:", prod_res, "Division:", div_res)
    random_list_size = random.randint(5, 10)
    random_min = random.randint(1, 20)
    random_max = random.randint(21, 50)
    random_list = generate_random_list(random_list_size, random_min, random_max)
    print("Generated Random List:", random_list)

    random_number = random.randint(1, 50)
    prime_check = is_prime(random_number)
    print(random_number, "is Prime:", prime_check)

    input_string = "Random Text"
    reversed_string = reverse_string(input_string)
    print("Reversed String:", reversed_string)

    num_a = random.randint(10, 30)
    num_b = random.randint(1, 10)
    sum_res, diff_res, prod_res, div_res = perform_operations(num_a, num_b)
    print("Sum:", sum_res, "Difference:", diff_res, "Product:", prod_res, "Division:", div_res)


def kaprekar_recursive(number, max_depth=20, depth=0):
    # Convert the number to a string to manipulate the digits
    num_str = str(number).zfill(4)  # Ensure it is always a 4-digit number by padding with zeroes if necessary
    if num_str[0] == num_str[1] == num_str[2] == num_str[3]:
        print(F"skipping num {number}")
        return True 
    # Base case: if depth reaches max_depth, stop recursion
    if depth >= max_depth:
        print(f"Max depth reached for {number}")
        return False
    
    # Sort the digits from highest to lowest
    highest_order = int("".join(sorted(num_str, reverse=True)))
    
    # Sort the digits from lowest to highest
    lowest_order = int("".join(sorted(num_str)))
    
    # Subtract lowest_order from highest_order
    result = highest_order - lowest_order
    
    # Check if the result is 6174 (Kaprekar's constant)
    if result == 6174:
        return True
    else:
        # Recursive case: call the function again with the new result
        return kaprekar_recursive(result, max_depth, depth + 1)

# Test the function
number = 1832
for i in range(10000):
    if kaprekar_recursive(i):
        # print("The number reached Kaprekar's constant 6174.")
        pass
    else:
        print(f"Bad number [{i}]")

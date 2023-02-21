def expanding_square_code(message):
    # Remove spaces and convert to lowercase
    message = message.replace(" ", "").lower()
    n = len(message)

    # Calculate the size of the matrix
    side_length = 1
    while side_length**2 < n:
        side_length += 2

    # Fill the matrix with the message and asterisks
    matrix = [["*"]*side_length for _ in range(side_length)]
    i, j = side_length//2, side_length//2
    k = 0
    while k < n:
        matrix[i][j] = message[k]
        if i == j or (i < side_length//2 and i == j-1) or (i > side_length//2 and i == j+1):
            j += 1
        elif j > side_length//2 and i < j:
            i += 1
        elif i > side_length//2 and i > j:
            i -= 1
        elif j < side_length//2 and i > j:
            j -= 1
        k += 1

    # Retrieve the message from the matrix
    result = ""
    for i in range(side_length):
        for j in range(side_length):
            if matrix[i][j] != "*":
                result += matrix[i][j]

    return result


# Test the function with an example message
message = "This is a test message!!"
encoded = expanding_square_code(message)
decoded = expanding_square_code(encoded)
print("Original message: ", message)
print("Encoded message: ", encoded)
print("Decoded message: ", decoded)

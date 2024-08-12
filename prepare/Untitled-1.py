if __name__ == '__main__':
    X = int(input())  # Read X
    Y = int(input())  # Read Y
    Z = int(input())  # Read Z
    N = int(input())  # Read N

    # List comprehension to generate the coordinates
    result = [[x, y, z] for x in range(X + 1) for y in range(Y + 1) for z in range(Z + 1) if x + y + z != N]
    
    # Print the result list
    print(result)

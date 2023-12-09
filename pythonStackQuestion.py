def generate_alternative_pattern():
    # Initial values
    x, y = 0, 0
    step = 10

    # Print the first two sets of values
    print(x, y)
    print(x + step, y + step)

    # Generate the alternative pattern
    for _ in range(5):
        # Increment x and y
        x += step
        y += step
        print(x, y)

        # Decrement y
        y -= step
        print(x, y)

        # Increment y
        y += 2 * step
        print(x, y)

generate_alternative_pattern()
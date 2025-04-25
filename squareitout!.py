def square_and_filter(start, end):
    squares = [num ** 2 for num in range(start, end + 1)]
    
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]
    
    print(f"All square values from {start} to {end}: {squares}")
    print(f"Even square values: {even_squares}")
    print(f"Odd square values: {odd_squares}")

# Example usage:
square_and_filter(1, 10)

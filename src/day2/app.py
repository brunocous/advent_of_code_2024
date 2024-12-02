import polars as pl
import numpy as np
from pathlib import Path

def is_safe_sequence(sequence):
    if len(sequence) < 2:
        return False
        
    # Calculate differences
    diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    
    if not diffs:  # Skip sequences that are too short
        return False
        
    # Check conditions
    all_same_sign = all(d > 0 for d in diffs) or all(d < 0 for d in diffs)
    all_at_least_one = all(abs(d) >= 1 for d in diffs)
    all_at_most_three = all(abs(d) <= 3 for d in diffs)
    
    return all_same_sign and all_at_least_one and all_at_most_three

def part1():
    # Read the file line by line and create a list of lists
    with open(Path(__file__).parent / "input.txt", 'r') as f:
        data = [list(map(int, line.strip().split())) for line in f]
    
    return sum(1 for sequence in data if is_safe_sequence(sequence))

def part2():
    # Read the file line by line and create a list of lists
    with open(Path(__file__).parent / "input.txt", 'r') as f:
        data = [list(map(int, line.strip().split())) for line in f]
    
    count = 0
    for sequence in data:
        # Check if sequence is safe without removing any number
        if is_safe_sequence(sequence):
            count += 1
            continue
            
        for i in range(len(sequence)):
            test_sequence = sequence[:i] + sequence[i+1:]
            if is_safe_sequence(test_sequence):
                count += 1
                break
    
    return count

def main():
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

if __name__ == "__main__":
    main()

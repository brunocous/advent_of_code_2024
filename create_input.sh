#!/bin/bash

# Find the latest day number by listing directories in src/
latest_day=$(ls -d src/day* 2>/dev/null | grep -o '[0-9]\+' | sort -n | tail -1)

# If no existing day folders, start with day 1, otherwise increment
if [ -z "$latest_day" ]; then
    next_day=1
else
    next_day=$((latest_day + 1))
fi

# Create the new directory
new_dir="src/day${next_day}"
mkdir -p "$new_dir"

# Create empty input.txt file
touch "$new_dir/input.txt"

# Create app.py with basic template
cat > "$new_dir/app.py" << 'EOF'
import polars as pl
from pathlib import Path

def part1(input_data):
    return None

def part2(input_data):
    return None

def main():
    df = pl.read_csv(
        Path(__file__).parent / "input.txt",
        separator="\t",
        has_header=False
    )
    
    print(f"Part 1: {part1(df)}")
    print(f"Part 2: {part2(df)}")

if __name__ == "__main__":
    main()
EOF

echo "Created new day ${next_day} structure in ${new_dir}"


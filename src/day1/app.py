import polars as pl
from pathlib import Path


def part1():
    df = pl.read_csv(
        Path(__file__).parent / "input.txt",
        separator=" ",
        has_header=False,
    ).select(pl.col("column_1").alias("x"), pl.col("column_4").alias("y"))
    print(df)

    # sort both columns independently
    df = pl.DataFrame({"x": df.get_column("x").sort(), "y": df.get_column("y").sort()})
    print(df)

    return df.select((pl.col("x") - pl.col("y")).abs().sum())


def part2():
    df = pl.read_csv(
        Path(__file__).parent / "input.txt",
        separator=" ",
        has_header=False,
    ).select(pl.col("column_1").alias("x"), pl.col("column_4").alias("y"))

    value_counts_y = df["y"].value_counts()
    x = pl.DataFrame({"x": df["x"]})

    print(x)

    combined = x.join(value_counts_y, left_on="x", right_on="y", how="left")

    print(combined)
    metric = (combined["x"] * combined["count"]).sum()
    print(metric)

    return metric


def main():
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()

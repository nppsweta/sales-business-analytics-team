
import pandas as pd
import argparse
from pathlib import Path


def inspect_dataset(file_path):
    """Load and inspect the Superstore sales dataset."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    df = pd.read_csv(path)

    print("SUPERSTORE DATASET INSPECTION")
    print("-" * 40)

    print(f"Dataset file: {path.name}")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nData types:")
    print(df.dtypes.to_string())

    print("\nMissing values by column:")
    print(df.isnull().sum().to_string())

    print(f"\nDuplicate rows: {df.duplicated().sum()}")

    print("\nFirst five rows:")
    print(df.head().to_string(index=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Inspect the Superstore sales dataset."
    )
    parser.add_argument(
        "csv_path",
        help="Path to the Superstore CSV file"
    )
    args = parser.parse_args()

    inspect_dataset(args.csv_path)
  

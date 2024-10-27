import pandas as pd
import argparse
import os

def convert_csv_to_parquet(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Convert to Parquet format
    df.to_parquet(output_file, index=False)
    print(f"Converted {input_file} to {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Convert CSV dataset to Parquet format.')
    parser.add_argument('input_file', type=str, help='Path to the input CSV file')
    parser.add_argument('output_file', type=str, help='Path to the output Parquet file')

    args = parser.parse_args()

    # Check if the input file exists
    if not os.path.isfile(args.input_file):
        print(f"Error: The file {args.input_file} does not exist.")
        return

    # Convert the CSV to Parquet
    convert_csv_to_parquet(args.input_file, args.output_file)

if __name__ == '__main__':
    main()

import pandas as pd
import os


def append_large_csv_files(csv_files, output_file, chunksize=100000):
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Open the output file
    with open(output_file, 'w') as outfile:
        # Loop through each file
        for i, file in enumerate(csv_files):
            print(f"Processing {file}...")

            # Read the file in chunks and append to the output file
            for chunk in pd.read_csv(file, chunksize=chunksize):
                # Write header only for the first file
                chunk.to_csv(outfile, header=(i == 0), index=False, mode='a')

    print(f"All files have been appended successfully into {output_file}!")


if __name__ == "__main__":
    # List of CSV files to append (replace with actual file paths)
    working_directory = 'C:/Users/Pia/Downloads'  # Replace with your actual working directory
    os.chdir(working_directory)

    csv_files = [
        'parquet_part-1.csv',
        'parquet_part-2.csv',
        'parquet_part-3.csv',
        'parquet_part-4.csv',
        'parquet_part-5.csv',
        'parquet_part-6.csv',
        'parquet_part-7.csv',
        'parquet_part-8.csv',
        'parquet_part-9.csv',
        'parquet_part-10.csv',
    ]

    # Output CSV file path (where the combined file will be saved)
    output_file = 'C:/Users/Pia/Downloads/combined_parquet_train.csv'

    # Call the function to append files
    append_large_csv_files(csv_files, output_file, chunksize=100000)

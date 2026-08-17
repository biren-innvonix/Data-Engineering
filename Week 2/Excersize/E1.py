import pandas as pd
from pathlib import Path

input_folder = Path("Excersize/E1_CSVS")
output_file = "merged.csv"

csv_files = list(input_folder.glob("*.csv"))

dataframes = []

for file in csv_files:
    df = pd.read_csv(file)
    dataframes.append(df)

merged_df = pd.concat(dataframes, ignore_index=True)

merged_df.to_csv(output_file, index=False)

print("Files merged successfully.")
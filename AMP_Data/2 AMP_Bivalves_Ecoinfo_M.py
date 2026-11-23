import pandas as pd
from pathlib import Path

# Set the folder and file paths.
folder = Path(__file__).resolve().parent
input_file = folder / "1 AMP_Bivalves_Ecoinfo.csv"
output_file = folder / "2 AMP_Bivalves_Ecoinfo_M.csv"

# Read the input and keep rows whose habitat contains uppercase "M".
df = pd.read_csv(input_file)
marine = df[df["habitat"].str.contains("M")]

# Save the rows and print the count.
marine.to_csv(output_file, index=False)
print(f"Saved {len(marine)} rows.")
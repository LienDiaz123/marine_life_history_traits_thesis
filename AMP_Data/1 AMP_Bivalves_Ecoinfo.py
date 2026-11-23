import pandas as pd
from pathlib import Path

# Set the folder and file paths.
folder = Path(__file__).resolve().parent
input_file = Path(r"C:\Users\liena\Documents\1 Ugent\1 Master\Jaar 2\Thesis\AMP data\1 AMP_Ecoinfo.csv")
output_file = folder / "1 AMP_Bivalves_Ecoinfo.csv"

# Read the input and keep rows where class is "Bivalvia".
df = pd.read_csv(input_file)
bivalves = df[df["class"] == "Bivalvia"]

# Save the rows and print the count.
bivalves.to_csv(output_file, index=False)
print(f"Saved {len(bivalves)} rows.")
import pandas as pd
from pathlib import Path

# Set the folder and file paths.
folder = Path(__file__).resolve().parent
eco_file = folder / "2 AMP_Bivalves_Ecoinfo_M.csv"
collection_file = Path(r"C:\Users\liena\Documents\1 Ugent\1 Master\Jaar 2\Thesis\AMP data\3 AMP_collection.csv")
output_file = folder / "4 AMP_Bivalves_M_collection.csv"

# Read the files and keep collection rows whose IDs appear in the eco data.
eco = pd.read_csv(eco_file)
collection = pd.read_csv(collection_file)
matches = collection[collection["ID"].isin(eco["ID"])]

# Save the rows and print the count.
matches.to_csv(output_file, index=False)
print(f"Saved {len(matches)} rows.")
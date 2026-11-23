import pandas as pd
from pathlib import Path

# Find the folder containing this script.
folder = Path(__file__).resolve().parent

# Read the ID columns and convert them to sets for comparison.
eco = set(pd.read_csv(folder / "2 AMP_Bivalves_Ecoinfo_M.csv")["ID"])
species = set(pd.read_csv(folder / "3 AMP_Bivalves_M_species.csv")["ID"])
collection = set(pd.read_csv(folder / "4 AMP_Bivalves_M_collection.csv")["ID"])

# Compare the IDs in files 2 and 3.
print("In 2 but not 3:", sorted(eco - species))
print("In 3 but not 2:", sorted(species - eco))

# Compare the IDs in files 2 and 4.
print("\nIn 2 but not 4:", sorted(eco - collection))
print("In 4 but not 2:", sorted(collection - eco))

# Compare the IDs in files 3 and 4.
print("\nIn 3 but not 4:", sorted(species - collection))
print("In 4 but not 3:", sorted(collection - species))
import pandas as pd
from pathlib import Path

# Find the folder containing this script and read the input CSV.
folder = Path(__file__).resolve().parent
data = pd.read_csv(folder / "4 AMP_Bivalves_M_collection.csv")

# Keep the listed columns and sort by family, scientific name, and description.
traits = data[
    ["Family", "ScientificName", "Data", "Description", "Observed", "Predicted", "Unit"]
].sort_values(["Family", "ScientificName"])

# Save the sorted records and print how many were saved.
traits.to_csv(folder / "6 Traits_by_species.csv", index=False)
print(f"Saved {len(traits)} trait records.")
import pandas as pd
import requests
from pathlib import Path

# Find the folder containing this script and read the input CSV.
folder = Path(__file__).resolve().parent
traits = pd.read_csv(folder / "6 Traits_by_species.csv")

# Get unique species with a family listed.
species = traits[["Family", "ScientificName"]].dropna().drop_duplicates()

# Request the OBIS record count for each species.
counts = []
for row in species.itertuples(index=False):
    response = requests.get("https://api.obis.org/v3/occurrence", params={"scientificname": row.ScientificName, "size": 1}, timeout=30,)
    response.raise_for_status()
    counts.append({"Family": row.Family, "ScientificName": row.ScientificName, "OBIS_records": response.json()["total"],})

# Keep species with records and sort the results.
result = pd.DataFrame(counts)
result = result[result["OBIS_records"] > 0]
result = result.sort_values(["Family", "ScientificName"])

# Save the results and print the number of species included.
result.to_csv(folder / "7 AMP_OBIS.csv", index=False)
print(f"\nSaved counts for {len(result)} species with OBIS records.")
import pandas as pd

# Define file paths
source_csv = r"E:/Thesis/Understand python/main-mahout_v_14.1.csv"  # All Java class metrics
smelly_csv = r"LazyClass-mahout_v_14.1.csv"  # Smelly class metrics
output_csv = r"E:/Thesis/Understand python/new-LazyClass-mahout_v_14.1.csv"  # Final output file

# Load both datasets
df_source = pd.read_csv(source_csv)   # All Java classes
df_smelly = pd.read_csv(smelly_csv)   # Smelly classes

# Ensure "Full Path" is a string and trim spaces
df_source["Full Path"] = df_source["Full Path"].astype(str).str.strip()
df_smelly["Full Path"] = df_smelly["Full Path"].astype(str).str.strip()

#  Merge the datasets using "Full Path" as key (outer join to keep all classes)
df_merged = df_source.merge(df_smelly[["Full Path"]], on="Full Path", how="left", indicator=True)

# Assign "Yes" to smelly classes and "No" to non-smelly classes
df_merged["Code Smell"] = df_merged["_merge"].apply(lambda x: "Yes" if x != "left_only" else "No")

# Drop the "_merge" column as it is no longer needed
df_merged.drop(columns=["_merge"], inplace=True)

#  Save the final dataset
df_merged.to_csv(output_csv, index=False)

print(f"✅ Merged dataset saved as {output_csv}")

# Display count of smelly and non-smelly classes
smelly_count = df_merged["Code Smell"].value_counts().get("Yes", 0)
non_smelly_count = df_merged["Code Smell"].value_counts().get("No", 0)

print(f"🔹 Smelly Classes (Code Smell = Yes): {smelly_count}")
print(f"🔹 Non-Smelly Classes (Code Smell = No): {non_smelly_count}")

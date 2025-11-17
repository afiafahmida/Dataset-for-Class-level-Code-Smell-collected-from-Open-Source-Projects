import os
import sys
import csv
import pandas as pd  # For efficient CSV handling

# Add Understand API path
sys.path.insert(0, r"E:/Thesis/SciTools/bin/pc-win64/Python")

# Required for Python 3.8+ to locate DLLs
os.add_dll_directory(r"E:/Thesis/SciTools/bin/pc-win64/")


import understand  # SciTools Understand API

def get_class_metrics(und_file, csv_filename):
    """Extracts all class metrics from an Understand database and writes them to a CSV file."""
    try:
        if not os.path.exists(und_file):
            print(f"❌ Error: .und file not found at {und_file}")
            return

        db = understand.open(und_file)

        # Define the required metrics
        required_metrics = {
            "All Methods": "CountDeclMethodAll",
            "Average Blank Lines": "AvgCountLineBlank",
            "Average Code Lines": "AvgCountLineCode",
            "Average Comment Lines": "AvgCountLineComment",
            "Average Cyclomatic Complexity": "AvgCyclomatic",
            "Average Lines": "AvgCountLine",
            "Base Classes": "CountClassBase",
            "Blank Lines": "CountLineBlank",
            "Class Methods": "CountDeclClassMethod",
            "Class Variables": "CountDeclClassVariable",
            "Code Lines": "CountLineCode",
            "Comment Lines": "CountLineComment",
            "Comment to Code Ratio": "RatioCommentToCode",
            "Coupled Classes": "CountClassCoupled",
            "Coupled Classes Modified": "CountClassCoupledModified",
            "Declarative Code Lines": "CountLineCodeDecl",
            "Declarative Statements": "CountStmtDecl",
            "Default Methods": "CountDeclMethodDefault",
            "Derived Classes": "CountClassDerived",
            "Executable Code Lines": "CountLineCodeExe",
            "Executable Statements": "CountStmtExe",
            "Instance Methods": "CountDeclInstanceMethod",
            "Instance Variables": "CountDeclInstanceVariable",
            "Lines": "CountLine",
            "Max Cyclomatic Complexity": "MaxCyclomatic",
            "Max Inheritance Tree": "MaxInheritanceTree",
            "Max Nesting": "MaxNesting",
            "Methods": "CountDeclMethod",
            "Percent Lack of Cohesion": "PercentLackOfCohesion",
            "Percent Lack of Cohesion Modified": "PercentLackOfCohesionModified",
            "Private Methods": "CountDeclMethodPrivate",
            "Protected Methods": "CountDeclMethodProtected",
            "Public Methods": "CountDeclMethodPublic",
            "Semicolons": "CountSemicolon",
            "Statements": "CountStmt",
            "Sum Cyclomatic Complexity": "SumCyclomatic"
        }

        #  Extract all class entities from Understand database
        class_entities = db.ents("Class")
        total_classes = len(class_entities)

        if total_classes == 0:
            print("⚠️ No classes found in the .und file! Ensure the project is analyzed properly.")
            return

        print(f"🔍 Extracting metrics for {total_classes} classes...")

        #  Store data before writing to CSV
        data_rows = []

        for class_entity in class_entities:
            class_name = class_entity.name()
            class_kind = class_entity.kind().name()
            full_class_path = class_entity.longname()

            #  Drop classes whose paths do not start with "org"
            if not full_class_path.startswith("org"):
                continue  # Skip this class

            #  Retrieve metric values safely (Handle missing metrics as None)
            metric_values = []
            for metric_name, understand_metric in required_metrics.items():
                metric_value = class_entity.metric([understand_metric]).get(understand_metric, None)
                metric_values.append(metric_value)

            #  Append to data storage
            data_rows.append([full_class_path, class_name, class_kind] + metric_values)

        db.close()

        #  Convert to Pandas DataFrame for cleanup
        columns = ["Full Path", "Class Name", "Kind"] + list(required_metrics.keys())
        df = pd.DataFrame(data_rows, columns=columns)

        #  Remove duplicate rows based on "Full Path"
        df.drop_duplicates(subset=["Full Path"], keep="first", inplace=True)

        #  Drop rows where **all** metric columns are missing (to ensure valid data)ls
        metric_columns = list(required_metrics.keys())  # Select metric columns
        df.dropna(subset=metric_columns, how="all", inplace=True)

    
        df.to_csv(csv_filename, index=False)
        print(f"✅ Extracted {df.shape[0]} valid classes and exported to {csv_filename}")

    except Exception as e:
        print(f"❌ Error processing .und file: {e}")


und_file_path = r"E:/Thesis/Understand python/LazyClass.und"
csv_output_file = r"LazyClass-mahout_v_14.1.csv"

get_class_metrics(und_file_path, csv_output_file)


#AntiSingleton
#BaseClassShouldBeAbstract
#ClassDataShouldBePrivate
#Blob
#ComplexClass
#LargeClass
#LazyClass

## Example Input and output

SAS Program: 
```
libname sales "/data/sales";

data customers;
    set sales.customer;
    where state="TX";
    full_name = catx(" ", first_name, last_name);
run;
```

Prompt to Gemini: 

this is a migration document from SAS to pyspark. write a pyspark script based on this document.

```
MigrationDocument(
    inputs=[
        DataSource(
            name='sales.customer', type='dataset'
        )],
        targets=[
            DataTarget(name='customers', type='dataset')
        ],
        data_flows=[
            DataFlow(
                source=DataSource(
                    name='sales.customer',
                    type='dataset'),
                    target=DataTarget(name='customers',
                    type='dataset'))
                ],
                filters=[
                    Filter(expression='state="TX"')
                ],
                assignments=[],
                libraries={
                    'sales': {
                        'engine': 'BASE',
                        'path': '/data/sales";'
                    }
                }
)
```                                     
                         
Gemini Response:

Here is the PySpark script based on your migration document.

Since the SAS data is stored using the BASE engine at /data/sales, the script reads the customer dataset directly from that path (assuming it is available in a format Spark can read, like Parquet or a mounted directory), applies your filter for Texas customers, and saves it.

```
from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("SAS_to_PySpark_Migration_Customer") \
    .getOrCreate()

# Define the source path based on the SAS library definition
# SAS library 'sales' maps to '/data/sales'
source_path = "/data/sales/customer"

# 1. Read the source dataset
# Note: Adjust the format (e.g., "parquet", "csv") depending on how the 
# SAS datasets were exported/stored in your cloud or file system.
df_customer = spark.read.format("parquet").load(source_path)

# 2. Apply the filter: state="TX"
df_filtered = df_customer.filter(df_customer["state"] == "TX")

# 3. Write to the target destination
# Update the target path to your preferred lakehouse or file location
target_path = "/data/output/customers"

df_filtered.write \
    .mode("overwrite") \
    .format("parquet") \
    .save(target_path)

print("Migration task completed successfully.")
```

Key Mapping Highlights

    Source: sales.customer maps to loading the file from /data/sales/customer.

    Filter: The SAS state="TX" expression is converted to a native PySpark .filter() condition.

    Target: customers is saved out to your destination repository.

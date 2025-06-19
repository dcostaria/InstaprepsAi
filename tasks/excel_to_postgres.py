import pandas as pd
from sqlalchemy import create_engine
import os
from urllib.parse import quote_plus  # Add this import

# 1. Create Excel file in Documents folder
documents_path = os.path.join(os.path.expanduser("~"), "Documents")
excel_path = os.path.join(documents_path, "sample_data.xlsx")

data = {
    "product_id": [101, 102, 103, 104],
    "product_name": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "price": [999.99, 19.99, 49.99, 199.99],
    "stock_quantity": [45, 120, 85, 32]
}
pd.DataFrame(data).to_excel(excel_path, index=False)

# 2. Read Excel
df = pd.read_excel(excel_path)

# 3. PostgreSQL connection (UPDATE THESE VALUES!)
db_config = {
    'database': 'excel_import_db',
    'user': 'postgres',
    'password': 'Lucy@1234',  # Password with special character
    'host': 'localhost',
    'port': '5432'
}

# 4. Create connection string with URL-encoded password
password_encoded = quote_plus(db_config['password'])
conn_string = f"postgresql://{db_config['user']}:{password_encoded}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

# 5. Import to PostgreSQL
try:
    engine = create_engine(conn_string)
    df.to_sql('products', engine, if_exists='replace', index=False)
    print("✅ Data imported successfully!")
except Exception as e:
    print(f"❌ Error: {e}")
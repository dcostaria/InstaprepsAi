import pandas as pd
import os

def change_excel_column_names(file_path, column_mapping):
    """
    Changes column names in an Excel file.
    
    Parameters:
        file_path (str): Path to the Excel file
        column_mapping (dict): Dictionary mapping old column names to new ones
    """
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        # Rename the columns
        df.rename(columns=column_mapping, inplace=True)
        
        # Save back to the same file
        df.to_excel(file_path, index=False)
        print(f"✅ Column names changed successfully in {file_path}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# Example usage
if __name__ == "__main__":
    # Create a sample Excel file in Documents folder
    documents_path = os.path.join(os.path.expanduser("~"), "instaprepstasks")
    excel_path = os.path.join(documents_path, "products.xlsx")
    
    # Sample data
    data = {
        "product_id": [101, 102, 103, 104],
        "product_name": ["Laptop", "Mouse", "Keyboard", "Monitor"],
        "price": [999.99, 19.99, 49.99, 199.99],
        "stock_quantity": [45, 120, 85, 32]
    }
    
    # Create the Excel file if it doesn't exist
    if not os.path.exists(excel_path):
        pd.DataFrame(data).to_excel(excel_path, index=False)
        print(f"📄 Created sample Excel file at {excel_path}")
    
    # Define how we want to rename columns
    column_changes = {
        "product_id": "ID",
        "product_name": "Product",
        "price": "Price (USD)",
        "stock_quantity": "Inventory"
    }
    
    # Call our function to rename columns
    change_excel_column_names(excel_path, column_changes)
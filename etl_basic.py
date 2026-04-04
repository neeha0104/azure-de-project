"""
Simple ETL Script - Week 1
"""
import csv
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('etl.log'),
        logging.StreamHandler()
    ]
)

def clean_csv(input_file, output_file):
    """Read CSV, clean data, save as CSV"""
    logging.info(f"Starting ETL: {input_file}")
    
    cleaned_data = []
    
    with open(input_file, 'r') as infile:
        reader = csv.DictReader(infile)
        
        for row in reader:
            # Clean data - remove rows with missing values
            if all(row.values()):
                cleaned_data.append(row)
    
    # Write cleaned data
    if cleaned_data:
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=cleaned_data[0].keys())
            writer.writeheader()
            writer.writerows(cleaned_data)
        
        logging.info(f"Success! Cleaned {len(cleaned_data)} records")
    else:
        logging.warning("No valid records found")

if __name__ == "__main__":
    # Create sample data first
    sample_data = """id,name,age,city
1,Alice,30,New York
2,Bob,,Chicago
3,Charlie,25,Boston"""
    
    with open('sample_data.csv', 'w') as f:
        f.write(sample_data)
    
    # Run ETL
    clean_csv('sample_data.csv', 'cleaned_data.csv')

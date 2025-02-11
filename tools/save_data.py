import os
import csv
from datetime import datetime

def save_candidate_data(candidate_name: str, email: str, phone_number: str, matching_keywords: str, screening_result: str) -> str:
    """Save candidate information and screening results to a CSV file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    filename = "assets/candidates_database.csv"
    file_exists = os.path.isfile(filename)
    
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Timestamp', 'Name', 'Email', 'Phone number', 'Matching Keywords', 'Screening Decision'])
        writer.writerow([timestamp, candidate_name, email, phone_number, matching_keywords, screening_result])
    
    return f"Data saved to {filename}"
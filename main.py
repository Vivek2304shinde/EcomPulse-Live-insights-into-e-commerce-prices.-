import os

# Define the project folder structure
folders = [
    "Laptop_Price_Comparison_Project",
    "Laptop_Price_Comparison_Project/data",
    "Laptop_Price_Comparison_Project/scrapers",
    "Laptop_Price_Comparison_Project/dashboard",
    "Laptop_Price_Comparison_Project/api",
    "Laptop_Price_Comparison_Project/automation",
    "Laptop_Price_Comparison_Project/logs"
]

# Create the directories
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create empty files within the directories
open("Laptop_Price_Comparison_Project/data/laptops_data.csv", 'w').close()
open("Laptop_Price_Comparison_Project/scrapers/amazon_scraper.py", 'w').close()
open("Laptop_Price_Comparison_Project/scrapers/flipkart_scraper.py", 'w').close()
open("Laptop_Price_Comparison_Project/dashboard/update_dashboard.py", 'w').close()
open("Laptop_Price_Comparison_Project/api/powerbi_api.py", 'w').close()
open("Laptop_Price_Comparison_Project/automation/pipeline.py", 'w').close()
open("Laptop_Price_Comparison_Project/automation/scheduler.sh", 'w').close()
open("Laptop_Price_Comparison_Project/logs/automation_log.txt", 'w').close()
open("Laptop_Price_Comparison_Project/README.md", 'w').close()

print("Project structure created successfully!")

#!/usr/local/bin/python3

# display_columns.py
# This script displays a matrix of task counts by list name from a normalized TickTick CSV file.
# It allows the user to select lists and statuses interactively or uses defaults if no menu is used.
# Input: normalized CSV file from TickTick backup
# 2025-06-24 using amazon q, this is the latest version of the script
    # It mostly gives satisfactory results.
    # Next steps:
    # 1. Add an ASCII tree of tasks associated by taskID/parentID
    # 2. Output the results to a file
    # 3. Review Claude's desired information to process tasks to determine which are high impact/leverage.
    # 4. Assess the five dimensions scores of each task. Rank them. Request confidence scores from Claude on the assessment.
    # 5. 

import csv
import re
import os
import sys
from collections import defaultdict

# Check for --menu flag
use_menu = '--menu' in sys.argv

# Get current directory and find CSV files
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_files = [f for f in os.listdir(current_dir) if f.endswith('.csv')]
csv_files.sort(key=lambda f: os.path.getmtime(os.path.join(current_dir, f)), reverse=True)

if not csv_files:
    print("No CSV files found in the current directory.")
    exit(1)

if use_menu:
    # Display CSV files with numbers
    print("Available CSV files (sorted by most recently modified):")
    for i, filename in enumerate(csv_files, 1):
        print(f"{i}. {filename}")
    
    # Get user choice
    while True:
        try:
            choice = int(input(f"\nSelect a CSV file (1-{len(csv_files)}): "))
            if 1 <= choice <= len(csv_files):
                csv_file = os.path.join(current_dir, csv_files[choice - 1])
                print(f"Selected: {csv_files[choice - 1]}\n")
                break
            else:
                print(f"Please enter a number between 1 and {len(csv_files)}.")
        except ValueError:
            print("Please enter a valid number.")
else:
    # Auto-select most recent CSV file
    csv_file = os.path.join(current_dir, csv_files[0])
    print(f"Using most recent CSV: {csv_files[0]}\n")

# # # Debugging: Uncomment the following lines to display column titles and first 5 rows
# # Open and read the CSV file to display column titles and first 5 rows
# with open(csv_file, mode="r", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     headers = next(reader)  # Get the column titles
# 
#     # Display column titles for columns 1 through 24
#     print("Column Titles:")
#     print(headers[:24])
# 
#     # Display the first 5 rows of data for columns 1 through 24
#     print("\nFirst 5 Rows:")
#     for i, row in enumerate(reader):
#         print(row[:24])  # Display values for columns 1 through 24
#         if i == 4:  # Stop after the first 5 rows
#             break




# Reopen the file to process task counts
with open(csv_file, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the headers

    # Initialize a dictionary to store task counts by list name
    task_counts = defaultdict(lambda: {"uncompleted": 0, "completed": 0, "cancelled": 0, "total": 0})

    # Process each row to count tasks by status and list name
    for row in reader:
        list_name = row[1]  # Column 2: List Name
        status = row[12]    # Column 13: Status
        task_counts[list_name]["total"] += 1
        if status == "0":
            task_counts[list_name]["uncompleted"] += 1
        elif status == "2":
            task_counts[list_name]["completed"] += 1
        elif status == "-1":
            task_counts[list_name]["cancelled"] += 1

    # Print the matrix
    print("\nTask Matrix by List Name:")
    print(f"{'List Name':<45} {'Uncompleted':<12} {'Completed':<10} {'Cancelled':<10} {'Total':<6}")
    list_names = list(task_counts.keys())
    for list_name, counts in task_counts.items():
        print(f"{list_name:<45} {counts['uncompleted']:<12} {counts['completed']:<10} {counts['cancelled']:<10} {counts['total']:<6}")

    if use_menu:
        # List selection menu
        print("\nSelect List(s):")
        for i, list_name in enumerate(list_names, 1):
            print(f"{i}. {list_name}")
        
        selected_lists = []
        while True:
            try:
                choices = input(f"\nEnter list numbers (1-{len(list_names)}, comma-separated, or 'all'): ").strip()
                if choices.lower() == 'all':
                    selected_lists = list_names[:]
                    break
                else:
                    nums = [int(x.strip()) for x in choices.split(',')]
                    if all(1 <= num <= len(list_names) for num in nums):
                        selected_lists = [list_names[num-1] for num in nums]
                        break
                    else:
                        print(f"Please enter numbers between 1 and {len(list_names)}.")
            except ValueError:
                print("Please enter valid numbers separated by commas.")
        
        # Status selection menu
        statuses = {'1': ('uncompleted', '0'), '2': ('completed', '2'), '3': ('cancelled', '-1')}
        print("\nSelect Status(es):")
        print("1. Uncompleted")
        print("2. Completed")
        print("3. Cancelled")
        
        selected_statuses = []
        while True:
            try:
                choices = input("\nEnter status numbers (1-3, comma-separated, or 'all'): ").strip()
                if choices.lower() == 'all':
                    selected_statuses = [v[1] for v in statuses.values()]
                    break
                else:
                    nums = [x.strip() for x in choices.split(',')]
                    if all(num in statuses for num in nums):
                        selected_statuses = [statuses[num][1] for num in nums]
                        break
                    else:
                        print("Please enter numbers 1, 2, or 3.")
            except ValueError:
                print("Please enter valid numbers separated by commas.")
        
        print(f"\nSelected Lists: {', '.join(selected_lists)}")
        status_names = [statuses[k][0] for k, v in statuses.items() if v[1] in selected_statuses]
        print(f"Selected Statuses: {', '.join(status_names)}")
    else:
        # Default: lists where folder name contains 'projects' or list name contains 'oneoff', uncompleted only
        selected_lists = []
        for list_name in list_names:
            with open(csv_file, mode="r", encoding="utf-8") as temp_file:
                temp_reader = csv.reader(temp_file)
                next(temp_reader)  # Skip headers
                for temp_row in temp_reader:
                    if (temp_row[1] == list_name and 
                        (re.search(r'projects', temp_row[0], re.IGNORECASE) or 
                         re.search(r'oneoff', temp_row[1], re.IGNORECASE))):
                        selected_lists.append(list_name)
                        break
        
        selected_statuses = ['0']  # uncompleted only
        print(f"\nUsing defaults - Lists with folder containing 'projects' or list containing 'oneoff': {', '.join(selected_lists)}")
        print(f"Status: Uncompleted only")

# Display filtered tasks
with open(csv_file, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the headers

    print(f"\nFiltered Tasks:")
    print(f"{'Task Title':<50} {'Folder':<20} {'List':<20} {'Tags':<20} {'Priority':<10} {'Content':<100}")
    for row in reader:
        list_name = row[1]   # Column 2: List Name
        status = row[12]     # Column 13: Status
        if list_name in selected_lists and status in selected_statuses:
            task_title = row[2]  # Column 3: Task Title
            folder_name = row[0] # Column 1: Folder Name
            tags = row[4] if len(row) > 4 else ""           # Column 5: Tags
            priority = row[11] if len(row) > 11 else ""     # Column 12: Priority
            content = row[5][:200] if len(row) > 5 else ""  # Column 6: Content (first 100 characters)
            priority_label = "High" if priority == "5" else "Medium" if priority == "3" else "Low" if priority == "1" else "None"

            print(f"{task_title:<50} {folder_name:<20} {list_name:<20} {tags:<20} {priority_label:<10} {content:<100}")
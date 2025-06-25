#!/usr/bin/env python3
"""
TickTick CSV Normalizer

This script normalizes a non-standard TickTick CSV export file into a standard CSV format.
It handles:
1. Removes metadata header (lines 1-6)
2. Preserves column headers
3. Properly preserves multiline fields that are quoted
4. Creates a new normalized CSV file

Usage:
    python ticktick_normalizer.py input.csv

2025-06-24 
Solid version that works with TickTick CSV exports.
It normalizes the CSV file by removing unnecessary metadata and ensuring that multiline fields are handled correctly.
Next steps (if bored):
1. Add functionality to count uncompleted tasks.
2. Generate a matrix of tasks categorized by list names.
3. Print the task matrix in a readable format.
"""

import csv
import sys
import os
import re

def normalize_ticktick_csv(input_path, output_path):
    """
    Normalize a TickTick CSV export file.
    
    Args:
        input_path: Path to the input TickTick CSV file
        output_path: Path where the normalized CSV will be saved
    """
    try:
        # Read the entire file as text first
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Find the header line (7th line)
        lines = content.split('\n')
        if len(lines) < 7:
            print(f"Error: Input file does not have enough lines. Found {len(lines)} lines.")
            return False
        
        # Extract headers from the 7th line
        header_line = lines[6]
        
        # Create a new content starting with the header line
        new_content = header_line + '\n'
        
        # Add all content from line 8 onwards
        new_content += '\n'.join(lines[7:])
        
        # Now parse this content properly with the csv module
        # which will handle the quoted fields correctly
        reader = csv.reader(new_content.splitlines(), quotechar='"', 
                           delimiter=',', quoting=csv.QUOTE_ALL, 
                           skipinitialspace=True)
        
        # Write to the output file
        with open(output_path, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
            
            # Skip the header row as we've already read it
            headers = next(reader)
            writer.writerow(headers)
            
            # Write all remaining rows
            for row in reader:
                writer.writerow(row)
        
        print(f"Successfully normalized CSV file. Output saved to {output_path}")
        return True
    
    except Exception as e:
        print(f"Error normalizing CSV: {str(e)}")
        return False

# def count_uncompleted_tasks(input_path):
#     """
#     Count the total number of uncompleted tasks in the CSV file.
#     
#     Args:
#         input_path: Path to the input TickTick CSV file
#     Returns:
#         int: Number of uncompleted tasks
#     """
#     try:
#         with open(input_path, 'r', encoding='utf-8') as file:
#             reader = csv.DictReader(file)
#             uncompleted_count = sum(1 for row in reader if row.get("Status", "").lower() == "incomplete")
#         return uncompleted_count
#     except Exception as e:
#         print(f"Error counting uncompleted tasks: {str(e)}")
#         return 0

def generate_task_matrix(input_path):
    """
    Generate a matrix count of tasks by list names.

    Args:
        input_path: Path to the input TickTick CSV file
    Returns:
        dict: A dictionary with list names as keys and counts of tasks categorized
              into uncompleted, completed, cancelled, and total as values.
    """
    try:
        task_matrix = {}
        with open(input_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                list_name = row.get("List Name", "Unknown")
                status = row.get("Status", "")

                if list_name not in task_matrix:
                    task_matrix[list_name] = {"uncompleted": 0, "completed": 0, "cancelled": 0, "total": 0}

                if status == "0":
                    task_matrix[list_name]["uncompleted"] += 1
                elif status == "2":
                    task_matrix[list_name]["completed"] += 1
                elif status == "-1":
                    task_matrix[list_name]["cancelled"] += 1

                task_matrix[list_name]["total"] += 1

        return task_matrix
    except Exception as e:
        print(f"Error generating task matrix: {str(e)}")
        return {}

def print_task_matrix(task_matrix):
    """
    Print the task matrix in a readable format.

    Args:
        task_matrix: Dictionary containing task counts by list names.
    """
    print("\nTask Matrix by List Names:")
    print(f"{'List Name':<45} {'Uncompleted':<12} {'Completed':<10} {'Cancelled':<10} {'Total':<6}")
    print("-" * 75)
    for list_name, counts in task_matrix.items():
        print(f"{list_name:<45} {counts['uncompleted']:<12} {counts['completed']:<10} {counts['cancelled']:<10} {counts['total']:<6}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python ticktick_normalizer.py input.csv")
        sys.exit(1)
    
    input_path = sys.argv[1]
        
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist.")
        sys.exit(1)
    
    # Generate the output file path in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_filename = os.path.basename(input_path)
    output_filename = os.path.splitext(input_filename)[0] + "-normalized.csv"
    output_path = os.path.join(script_dir, output_filename)
    
    success = normalize_ticktick_csv(input_path, output_path)

    if success:
        # uncompleted_count = count_uncompleted_tasks(output_path)
        # print(f"Total number of uncompleted tasks: {uncompleted_count}")
        
        task_matrix = generate_task_matrix(output_path)
        print_task_matrix(task_matrix)
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()

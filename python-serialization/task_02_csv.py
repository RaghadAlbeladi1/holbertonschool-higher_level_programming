#!/usr/bin/python3
"""Module converts CSV to JSON"""
import csv
import json

def convert_csv_to_json(csv_file):
   """Convert CSV to JSON"""
   try:
       # Deserialize CSV (load to python)
       with open(csv_file, newline='', encoding='utf-8') as csvfile:
           reader = csv.DictReader(csvfile)
           rows = list(reader)
       
       # Serialize CSV into Json
       with open('data.json', "w", encoding='utf-8') as jsonfile:
           json.dump(rows, jsonfile, ensure_ascii=False, indent=2)
       
       return True
   except (FileNotFoundError, csv.Error, json.JSONDecodeError, Exception):
       return False

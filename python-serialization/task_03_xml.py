#!/usr/bin/python3
"""Module for XML serialization and deserialization"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
   """Serialize a Python dictionary to XML and save to file"""
   # Create root element
   root = ET.Element("data")
   
   # Iterate through dictionary items and add as child elements
   for key, value in dictionary.items():
       child = ET.SubElement(root, key)
       child.text = str(value)
   
   # Create ElementTree and write to file
   tree = ET.ElementTree(root)
   tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
   """Deserialize XML file back to Python dictionary"""
   # Parse the XML file
   tree = ET.parse(filename)
   root = tree.getroot()
   
   # Reconstruct dictionary from XML elements
   dictionary = {}
   for child in root:
       dictionary[child.tag] = child.text
   
   return dictionary

#!/usr/bin/python3
"""Client-Server Application with Serialization"""
import socket
import json
import threading


def start_server():
   """Start a server that receives and deserializes data"""
   # Create server socket
   server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   
   try:
       # Bind to localhost on port 12345
       server_socket.bind(('localhost', 12345))
       server_socket.listen(1)
       print("Server listening on port 12345...")
       
       # Accept incoming connection
       client_socket, address = server_socket.accept()
       print(f"Connection from {address}")
       
       # Receive serialized data
       data = client_socket.recv(1024).decode('utf-8')
       
       # Deserialize the data
       received_dict = json.loads(data)
       
       # Print the received dictionary
       print("Received Dictionary from Client:")
       print(received_dict)
       
       # Close connections
       client_socket.close()
       
   except Exception as e:
       print(f"Server error: {e}")
   finally:
       server_socket.close()


def send_data(dictionary):
   """Send serialized dictionary to server"""
   try:
       # Create client socket
       client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       
       # Connect to server
       client_socket.connect(('localhost', 12345))
       
       # Serialize the dictionary
       serialized_data = json.dumps(dictionary)
       
       # Send serialized data to server
       client_socket.send(serialized_data.encode('utf-8'))
       
       # Close connection
       client_socket.close()
       
   except Exception as e:
       print(f"Client error: {e}")

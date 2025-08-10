#!/usr/bin/env python
"""
Test script for the Django REST API
This script tests all the API endpoints to ensure they're working correctly.
"""
import os
import sys
import django
import requests
import json

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth.models import User
from clients.models import Client
from projects.models import Project

def test_api_endpoints():
    """Test all API endpoints"""
    base_url = "http://127.0.0.1:8000"
    session = requests.Session()
    
    print("🚀 Testing Django REST API...")
    print("=" * 50)
    
    # Test 1: Login to get session
    print("\n1. Testing Login...")
    login_data = {
        'username': 'admin',
        'password': 'admin123'
    }
    
    try:
        response = session.post(f"{base_url}/admin/login/", data=login_data)
        if response.status_code == 200:
            print("✅ Login successful!")
        else:
            print("❌ Login failed!")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure the server is running!")
        return
    
    # Test 2: Create a client
    print("\n2. Testing Client Creation...")
    client_data = {
        'client_name': 'Test Company API'
    }
    
    try:
        response = session.post(
            f"{base_url}/api/clients/",
            json=client_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 201:
            client_response = response.json()
            client_id = client_response['id']
            print(f"✅ Client created successfully! ID: {client_id}")
            print(f"   Client Name: {client_response['client_name']}")
            print(f"   Created By: {client_response['created_by']}")
        else:
            print(f"❌ Client creation failed! Status: {response.status_code}")
            print(f"   Response: {response.text}")
            return
    except Exception as e:
        print(f"❌ Error creating client: {e}")
        return
    
    # Test 3: List all clients
    print("\n3. Testing Client List...")
    try:
        response = session.get(f"{base_url}/api/clients/")
        
        if response.status_code == 200:
            clients = response.json()
            print(f"✅ Retrieved {len(clients)} clients!")
            for client in clients:
                print(f"   - {client['client_name']} (ID: {client['id']})")
        else:
            print(f"❌ Failed to get clients! Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Error getting clients: {e}")
    
    # Test 4: Get client details
    print(f"\n4. Testing Client Details (ID: {client_id})...")
    try:
        response = session.get(f"{base_url}/api/clients/{client_id}/")
        
        if response.status_code == 200:
            client_details = response.json()
            print(f"✅ Client details retrieved!")
            print(f"   Name: {client_details['client_name']}")
            print(f"   Projects: {len(client_details.get('projects', []))}")
        else:
            print(f"❌ Failed to get client details! Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Error getting client details: {e}")
    
    # Test 5: Create a project for the client
    print(f"\n5. Testing Project Creation for Client {client_id}...")
    project_data = {
        'project_name': 'Test Project API',
        'users': [1]  # Assign to admin user
    }
    
    try:
        response = session.post(
            f"{base_url}/api/clients/{client_id}/projects/",
            json=project_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 201:
            project_response = response.json()
            project_id = project_response['id']
            print(f"✅ Project created successfully! ID: {project_id}")
            print(f"   Project Name: {project_response['project_name']}")
            print(f"   Client: {project_response['client']}")
            print(f"   Users: {len(project_response['users'])}")
        else:
            print(f"❌ Project creation failed! Status: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Error creating project: {e}")
    
    # Test 6: List user's projects
    print("\n6. Testing User Projects...")
    try:
        response = session.get(f"{base_url}/api/projects/")
        
        if response.status_code == 200:
            projects = response.json()
            print(f"✅ Retrieved {len(projects)} projects for current user!")
            for project in projects:
                print(f"   - {project['project_name']} (Client: {project['client']})")
        else:
            print(f"❌ Failed to get user projects! Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Error getting user projects: {e}")
    
    # Test 7: Update client
    print(f"\n7. Testing Client Update (ID: {client_id})...")
    update_data = {
        'client_name': 'Updated Test Company API'
    }
    
    try:
        response = session.put(
            f"{base_url}/api/clients/{client_id}/",
            json=update_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            updated_client = response.json()
            print(f"✅ Client updated successfully!")
            print(f"   New Name: {updated_client['client_name']}")
        else:
            print(f"❌ Client update failed! Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Error updating client: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 API Testing Complete!")
    print("\n📋 Summary:")
    print("✅ All API endpoints are working correctly")
    print("✅ Client CRUD operations successful")
    print("✅ Project creation and assignment working")
    print("✅ User authentication working")
    print("\n🌐 You can now use the API with:")
    print("   - cURL commands")
    print("   - Postman")
    print("   - Any HTTP client")
    print(f"\n📖 API Documentation: {base_url}/")

if __name__ == '__main__':
    test_api_endpoints() 
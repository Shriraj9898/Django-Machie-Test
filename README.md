# Django REST API Project

A complete Django REST API system for managing Users, Clients, and Projects with full CRUD operations.

## 🚀 Features

- **User Management**: Django's built-in User model with admin panel
- **Client Management**: Full CRUD operations via REST API
- **Project Management**: Create projects and assign users
- **Authentication**: Session-based authentication
- **Admin Interface**: Django admin panel for user management

## 📋 Requirements

- Python 3.8+
- Django 5.1.5
- Django REST Framework 3.14.0

## 🛠️ Installation & Setup

1. **Clone/Download the project**
2. **Install dependencies:**
   ```bash
   pip install django djangorestframework
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the server:**
   ```bash
   python manage.py runserver
   ```

## 🌐 Access Points

- **Home Page**: `http://127.0.0.1:8000/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`
- **API Base URL**: `http://127.0.0.1:8000/api/`

## 👥 Default Users

- **Admin**: `admin` / `admin123`
- **Test Users**: `rohit` / `test123`

## 📚 API Documentation

### Client Management

#### List All Clients
```http
GET /api/clients/
```

**Response:**
```json
[
    {
        "id": 1,
        "client_name": "Nimap",
        "created_at": "2025-08-08T21:30:00.000000+05:30",
        "created_by": "Rohit Sharma",
        "updated_at": "2025-08-08T21:30:00.000000+05:30"
    }
]
```

#### Create New Client
```http
POST /api/clients/
Content-Type: application/json

{
    "client_name": "Company A"
}
```

#### Get Client Details
```http
GET /api/clients/{id}/
```

**Response:**
```json
{
    "id": 2,
    "client_name": "Infotech",
    "projects": [
        {
            "id": 1,
            "project_name": "Project A"
        }
    ],
    "created_at": "2025-08-08T21:30:00.000000+05:30",
    "created_by": "Rohit Sharma",
    "updated_at": "2025-08-08T21:30:00.000000+05:30"
}
```

#### Update Client
```http
PUT /api/clients/{id}/
Content-Type: application/json

{
    "client_name": "Updated Company Name"
}
```

#### Delete Client
```http
DELETE /api/clients/{id}/
```

**Response:** `204 No Content`

### Project Management

#### List User's Projects
```http
GET /api/projects/
```

**Response:**
```json
[
    {
        "id": 1,
        "project_name": "Project A",
        "client": "Nimap",
        "users": [
            {
                "id": 1,
                "name": "Rohit Sharma"
            }
        ],
        "created_at": "2025-08-08T21:30:00.000000+05:30",
        "created_by": "Ganesh Patil"
    }
]
```

#### Create Project for Client
```http
POST /api/clients/{client_id}/projects/
Content-Type: application/json

{
    "project_name": "Project A",
    "users": [1, 2]
}
```

**Response:**
```json
{
    "id": 3,
    "project_name": "Project A",
    "client": "Nimap",
    "users": [
        {
            "id": 1,
            "name": "Rohit Sharma"
        }
    ],
    "created_at": "2025-08-08T21:30:00.000000+05:30",
    "created_by": "Ganesh Patil"
}
```

## 🔧 Testing the API

### Using cURL

1. **Login (get session cookie):**
   ```bash
   curl -c cookies.txt -X POST http://127.0.0.1:8000/admin/login/ \
     -d "username=admin&password=admin123"
   ```

2. **List clients:**
   ```bash
   curl -b cookies.txt http://127.0.0.1:8000/api/clients/
   ```

3. **Create client:**
   ```bash
   curl -b cookies.txt -X POST http://127.0.0.1:8000/api/clients/ \
     -H "Content-Type: application/json" \
     -d '{"client_name": "Test Company"}'
   ```

### Using Postman

1. **Set up authentication:**
   - Go to Settings → Cookies
   - Add domain: `127.0.0.1`
   - Add cookie: `sessionid` (get from browser after login)

2. **Test endpoints:**
   - GET `http://127.0.0.1:8000/api/clients/`
   - POST `http://127.0.0.1:8000/api/clients/`
   - GET `http://127.0.0.1:8000/api/projects/`

## 📁 Project Structure

```
myproject/
├── manage.py              # Django management script
├── myproject/            # Project configuration
│   ├── settings.py       # Project settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI application
├── home/                 # Home app
│   ├── views.py         # Home page views
│   └── templates/       # Templates
├── clients/             # Clients app
│   ├── models.py        # Client model
│   ├── views.py         # Client API views
│   ├── serializers.py   # Client serializers
│   ├── urls.py          # Client URLs
│   └── admin.py         # Admin configuration
├── projects/            # Projects app
│   ├── models.py        # Project model
│   ├── views.py         # Project API views
│   ├── serializers.py   # Project serializers
│   ├── urls.py          # Project URLs
│   └── admin.py         # Admin configuration
└── db.sqlite3           # Database file
```

## 🔐 Authentication

The API uses Django's session authentication. To access protected endpoints:

1. **Login via admin panel** or **API endpoint**
2. **Use session cookies** in subsequent requests
3. **All endpoints require authentication**

## 🎯 Key Features Implemented

✅ **User Management**: Django's built-in User model  
✅ **Client CRUD**: Create, Read, Update, Delete clients  
✅ **Project Management**: Create projects and assign users  
✅ **User Assignment**: Assign multiple users to projects  
✅ **REST API**: Complete RESTful API implementation  
✅ **Admin Interface**: Django admin for user management  
✅ **Authentication**: Session-based authentication  
✅ **Documentation**: Comprehensive API documentation  

## 🚀 Next Steps

1. **Add more features:**
   - Project status tracking
   - Time tracking
   - File uploads
   - Email notifications

2. **Enhance security:**
   - JWT authentication
   - API rate limiting
   - CORS configuration

3. **Add testing:**
   - Unit tests
   - Integration tests
   - API tests

## 📞 Support

For any questions or issues, please refer to the Django documentation or create an issue in the project repository. 
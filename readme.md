
# 💰 Django Expense Tracker 

A RESTful API built with Django and Django REST Framework to track income and expenses, with secure JWT authentication and tax calculation logic.

## 🚀 Project Overview

This project allows users to:

- Register and log in with JWT authentication.
- Track income and expenses with optional tax (flat or percentage).
- Only access their own records (except superusers).
- Get paginated API responses for efficient data retrieval.

## 🔧 Tech Stack

- **Backend:** Django 5.x, Django REST Framework
- **Authentication:** JWT via `djangorestframework-simplejwt`
- **Database:** SQLite (for development)
- **Python Version:** 3.8+

## 🛠️ Features

✅ User registration & login  
✅ JWT-based authentication  
✅ Personal income/expense tracking  
✅ Flat & percentage tax logic  
✅ Complete CRUD functionality  
✅ Secure permissions (regular user vs superuser)  
✅ Paginated list view

## 🧱 Database Models

### User
- Uses Django's built-in `User` model.


## 🔗 API Endpoints

### 🔐 Authentication

| Endpoint                   | Description            |
|----------------------------|------------------------|
| POST `/api/auth/register/` | Register new user      |
| POST `/api/auth/login/`    | Login & get tokens     |
| POST `/api/auth/refresh/`  | Refresh token          |

### 💸 Expense/Income

| Endpoint                     | Method | Description                         |
|------------------------------|--------|-------------------------------------|
| `/api/expenses/`             | GET    | List current user's records         |
| `/api/expenses/`             | POST   | Create new record                   |
| `/api/expenses/{id}/`        | GET    | Get single record                   |
| `/api/expenses/{id}/`        | PUT    | Update record                       |
| `/api/expenses/{id}/`        | DELETE | Delete record                       |

## 🧪 Example API Responses

### ✅ Single Record
```json
{
  "id": 1,
  "title": "Grocery",
  "description": "Weekly grocery shopping",
  "amount": 100.00,
  "transaction_type": "debit",
  "tax": 10.00,
  "tax_type": "flat",
  "total": 110.00,
  "created_at": "2025-01-01T10:00:00Z",
  "updated_at": "2025-01-01T10:00:00Z"
}
```

### 📄 Paginated List
```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Grocery",
      "amount": 100.00,
      "transaction_type": "debit",
      "total": 110.00,
      "created_at": "2025-01-01T10:00:00Z"
    }
  ]
}
```

## ⚙️ Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/regmiaashish/Expense-Tracker.git
cd expense-tracker
```

2. **Create & activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
env\Scripts\activate     # For Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Apply migrations**
```bash
python manage.py migrate
```

5. **Create superuser (optional)**
```bash
python manage.py createsuperuser
```

6. **Run the server**
```bash
python manage.py runserver
```

## 🧪 Testing Checklist

✅ User registration/login  
✅ JWT token auth  
✅ Access control (self vs superuser)  
✅ Create, Read, Update, Delete entries  
✅ Correct tax total calculation  
✅ Paginated response  


## 📂 Folder Structure

```
├── expenses/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── expense_tracker/
│   └── settings.py
├── manage.py
└── requirements.txt
```

## 📝 Author

**Aashish Regmi**  
Intern Applicant at Vrit Technologies  
Email: [regmiaashish660@gmail.com]  


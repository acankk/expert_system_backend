# 🩺 STAYCARE Backend

Backend API untuk aplikasi **STAYCARE**, sebuah sistem pakar diagnosis penyakit berbasis Android menggunakan metode **Forward Chaining** dan **Certainty Factor (CF)**.

---

## 🚀 Tech Stack

- Python 3
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- drf-spectacular (Swagger/OpenAPI)

---

## ✨ Features

### Authentication

- Login
- JWT Authentication
- Role-based Authorization
- Admin & User

### Knowledge Management

- Disease Management
- Symptom Management
- Rule Management
- Recommendation Management

### Expert System

- Forward Chaining Inference
- Certainty Factor Calculation
- Disease Diagnosis
- Diagnosis History
- Recommendation based on Confidence Level

### Dashboard

- Total Diseases
- Total Symptoms
- Total Rules
- Total Recommendations

---

## 📂 Project Structure

```
apps/
│
├── users/
├── knowledge/
│   ├── disease/
│   ├── symptom/
│   ├── rule/
│   └── recommendation/
│
├── diagnosis/
└── dashboard/
```

---

## ⚙️ Installation

Clone repository

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
```

Masuk ke project

```bash
cd project-name
```

Buat virtual environment

```bash
python -m venv venv
```

Aktifkan virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependency

```bash
pip install -r requirements.txt
```

---

## 🛠 Configure Environment

Buat file `.env`

```env
SECRET_KEY=your-secret-key

DEBUG=True

DATABASE_URL=your-postgresql-url

ALLOWED_HOSTS=127.0.0.1,localhost
```

---

## 🔄 Migration

```bash
python manage.py migrate
```

---

## 👤 Create Superuser

```bash
python manage.py createsuperuser
```

---

## ▶️ Run Server

```bash
python manage.py runserver
```

Server berjalan di

```
http://127.0.0.1:8000/
```

---

## 📖 API Documentation

Swagger

```
/api/schema/swagger-ui/
```

OpenAPI Schema

```
/api/schema/
```

---

## 🧠 Diagnosis Process

1. User memilih gejala.
2. Sistem melakukan proses **Forward Chaining**.
3. Setiap rule dihitung menggunakan metode **Certainty Factor**.
4. Nilai CF digabungkan menggunakan rumus kombinasi CF.
5. Sistem menentukan penyakit dengan nilai CF tertinggi.
6. Sistem memberikan rekomendasi berdasarkan rentang nilai CF.

---

## 🔐 Authentication

Menggunakan JWT Authentication.

Login akan menghasilkan:

- Access Token
- Refresh Token

Access Token digunakan pada setiap request:

```
Authorization: Bearer <access_token>
```

---

## 📦 Main API

### Authentication

- POST `/api/users/login/`

### Dashboard

- GET `/api/dashboard/`

### Disease

- GET `/api/knowledge/disease/`
- POST `/api/knowledge/disease/`
- PUT `/api/knowledge/disease/{id}/`
- DELETE `/api/knowledge/disease/{id}/`

### Symptom

- GET `/api/knowledge/symptom/`
- POST `/api/knowledge/symptom/`
- PUT `/api/knowledge/symptom/{id}/`
- DELETE `/api/knowledge/symptom/{id}/`

### Rule

- GET `/api/knowledge/rule/`
- POST `/api/knowledge/rule/`
- PUT `/api/knowledge/rule/{id}/`
- DELETE `/api/knowledge/rule/{id}/`

### Recommendation

- GET `/api/knowledge/recommendation/`
- POST `/api/knowledge/recommendation/`
- PUT `/api/knowledge/recommendation/{id}/`
- DELETE `/api/knowledge/recommendation/{id}/`

### Diagnosis

- POST `/api/diagnosis/`
- GET `/api/diagnosis/history/`

---

## 📄 License

This project was developed for educational purposes.

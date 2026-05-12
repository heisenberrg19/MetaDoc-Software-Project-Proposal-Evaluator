# 🛠️ MetaDoc - Development & Deployment Guide

This document provides technical details about the MetaDoc technology stack, deployment procedures, and testing credentials.

---

## 🏗️ Technology Stack

MetaDoc is built using a modern, scalable stack split into a Flask backend and a React frontend.

### 🔹 Backend (Python 3.10+)
| Component | Technology | Version |
|-----------|------------|---------|
| **Core Framework** | Flask | 3.0.0 |
| **Database ORM** | Flask-SQLAlchemy | 3.1.1 |
| **Migrations** | Flask-Migrate | 4.0.5 |
| **Authentication** | Google OAuth 2.0 | - |
| **AI Engine** | Google Gemini (Generative AI) | >= 0.8.0 |
| **NLP Utilities** | SpaCy, NLTK, Textstat | 3.7.2+, 3.8.1, 0.7.3 |
| **Task Queue** | Celery + Redis | 5.3.6, 5.0.1 |
| **Data Handling** | Pandas | >= 2.2.0 |
| **Document Parsing** | python-docx, pypdf | 1.1.0, >= 4.0.0 |
| **PDF Generation** | ReportLab | 4.0.8 |
| **Security** | PyJWT, Cryptography | 2.8.0, 41.0.7 |

### 🔹 Frontend (React 19)
| Component | Technology | Version |
|-----------|------------|---------|
| **Framework** | React | 19.2.4 |
| **Build Tool** | Vite | 7.2.4 |
| **Routing** | React Router Dom | 7.1.1 |
| **API Client** | Axios | 1.7.9 |
| **Charts** | Recharts | 3.7.0 |
| **Excel Export** | XLSX (SheetJS) | 0.18.5 |
| **Linting** | ESLint | 9.39.1 |

---

## 🚀 Deployment Instructions

### 🌐 Frontend Deployment (Vercel)
The frontend is optimized for Vercel deployment.

1. **Install Vercel CLI**: `npm i -g vercel`
2. **Configure Environment**: Ensure `VITE_API_BASE_URL` is set to your deployed backend URL.
3. **Build**: `npm run build`
4. **Deploy**:
   ```bash
   cd frontend/metadoc
   vercel --prod
   ```

### ⚙️ Backend Deployment (Production)
The backend is designed to run with a WSGI server (Gunicorn) and a PostgreSQL database.

1. **Database Setup**:
   - Provision a PostgreSQL instance (e.g., Supabase, Neon, or AWS RDS).
   - Set `DATABASE_URL` in your environment variables.
2. **Environment Variables**:
   - `FLASK_ENV=production`
   - `SECRET_KEY`: Random 32-byte hex string
   - `JWT_SECRET_KEY`: Random 32-byte hex string
   - `GOOGLE_CLIENT_ID` & `GOOGLE_CLIENT_SECRET` (from Google Cloud Console)
   - `GEMINI_API_KEY` (from Google AI Studio)
3. **Initialization**:
   ```bash
   cd backend
   pip install -r requirements.txt
   flask db upgrade  # If using migrations
   # OR
   python scripts/reset_database.py # To start with fresh tables (CAUTION: Deletes data)
   ```
4. **Execution**:
   ```bash
   gunicorn wsgi:app --bind 0.0.0.0:$PORT
   ```

---

## 👤 Sample/Dummy Credentials

MetaDoc primarily uses **Google OAuth 2.0** for secure authentication. For testing purposes, the following dummy student accounts are pre-registered in the system's class records (whitelist).

### 🎓 Student Accounts (Google OAuth)
Students must log in using a personal Gmail account. The following dummy student accounts are pre-registered in the system. Since authentication is handled via Google OAuth, passwords for these accounts are left as `null`:

| Username (Email) | Password | Role |
|------------------|----------|------|
| `mahinay.franciskyle@gmail.com` | `null` | Student |
| `ashleeeskye@gmail.com` | `null` | Student |
| `josefcajes777@gmail.com` | `null` | Student |
| `gemgemps@gmail.com` | `null` | Student |
| `rcampilanan.reenahc@gmail.com` | `null` | Student |
| `mikeljoshnicer@gmail.com` | `null` | Student |
| `rubyxmanalo@gmail.com` | `null` | Student |
| `kikikyleed@gmail.com` | `null` | Student |
| `rafiki.abella@gmail.com` | `null` | Student |
| `nicolaaiirabe@gmail.com` | `null` | Student |
| `aquinojulianne.r@gmail.com` | `null` | Student |
| `bramwellicer@gmail.com` | `null` | Student |
| `jorgemartinn11@gmail.com` | `null` | Student |
| `geraldezjunjie@gmail.com` | `null` | Student |
| `michaelgrantlibato7@gmail.com` | `null` | Student |
| `paulbibit05@gmail.com` | `null` | Student |
| `ninaisabelletupas@gmail.com` | `null` | Student |
| `rosalinakremer02@gmail.com` | `null` | Student |
| `rodgabriellecanete2002@gmail.com` | `null` | Student |
| `johannelumauag11@gmail.com` | `null` | Student |

### 👨‍🏫 Professor Accounts
Professors log in via Google OAuth. To grant professor access:
1. Sign in once with Google.
2. Manually update the `role` in the `users` table to `professor` (or use the default registration if `ALLOWED_EMAIL_DOMAINS` includes your domain).

### 🔑 Local Testing (Basic Login)
If basic authentication is enabled (via `/api/v1/auth/register` and `/api/v1/auth/login-basic`), you can create a test user:

**Example Test Credentials:**
- **Email**: `test.professor@cit.edu`
- **Password**: `password123`
- **Role**: Professor

---

## 📂 Key Directories
- `backend/uploads`: Temporary storage for uploaded files.
- `backend/reports`: Generated analysis reports (CSV/PDF).
- `backend/migrations`: Database schema version control.
- `frontend/metadoc/src/pages`: UI screen implementations.

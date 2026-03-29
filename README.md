# MetaDoc: Software Project Proposal Evaluator

> **⚡ Quick Start?** See [QUICK_START.md](QUICK_START.md) for a 10-minute setup guide!

MetaDoc is a comprehensive **document analysis and evaluation platform** designed for academic institutions. It streamlines student proposal submissions, performs intelligent metadata extraction, executes deep NLP analysis, and leverages Google Gemini AI for qualitative insights.

---

## ✨ Key Features

### 📤 **Unified Submission System**
- Google OAuth 2.0 authentication for students and professors
- Whitelist gatekeeping integrated with Class Records
- Google Drive link submission with permission handling
- Flexible deadline management (hard/soft deadlines)
- Multi-folder organization by deadline

### 🔬 **Intelligent Document Analysis**
- Automatic metadata extraction (authors, dates, revision counts)
- Identity deduplication with smart name/email normalization
- Real-time NLP analysis (readability, sentiment, named entities)
- Google Gemini AI-powered qualitative evaluation
- Custom rubric-based assessment

### 👨‍🏫 **Professor Dashboard**
- Real-time system overview and statistics
- Submission management and organization
- Comprehensive report generation (PDF/CSV)
- Rubric creation and customization
- Batch operations for submissions

---

## 🏗️ System Architecture

### Backend (3-Layer Design)
```
API Layer (Flask Routes) 
    ↓
Service Layer (Business Logic) 
    ↓
Persistence Layer (SQLAlchemy ORM)
```

**Key Components:**
- **Flask REST API** - 8+ blueprints for different features
- **Service Layer** - 12 specialized service classes
- **SQLAlchemy ORM** - Database abstraction for SQLite/PostgreSQL
- **Google APIs** - Drive, OAuth, and Gemini integration

### Frontend (React + Vite)
```
Pages & Components (React)
    ↓
State Management (AuthContext)
    ↓
API Services (Axios)
```

**Key Features:**
- Component-based architecture with reusable UI
- React Context for state management
- Responsive design (works on desktop & mobile)
- Real-time loading states and error handling
- Role-based access control

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+** (Tested on 3.13)
- **Node.js 18+** and npm
- **Git** for version control
- **Google Cloud Account** (for OAuth and Gemini API)

### Installation (3 Steps)

**1. Clone Repository**
```bash
git clone <repository-url>
cd MetaDoc-Software-Project-Proposal-Evaluator
```

**2. Setup Backend**
```bash
cd backend
python -m venv venv

# Activate virtual environment
# Windows PowerShell:
.\venv\Scripts\Activate.ps1

# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure
copy .env.example .env  # Windows
# cp .env.example .env  # Linux/Mac

# Initialize database
python scripts/reset_database.py

# Start server
python run.py
```

✅ Backend running at: `http://localhost:5000`

**3. Setup Frontend** (in new terminal)
```bash
cd frontend/metadoc
npm install
npm run dev
```

✅ Frontend running at: `http://localhost:5173`

---

## ⚙️ Configuration

### Required: Google OAuth & Gemini API

Create `backend/.env` file with:

```env
# Authentication (REQUIRED)
GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-client-secret
GOOGLE_REDIRECT_URI=http://localhost:5000/api/v1/auth/callback

# Gemini AI (Optional - for qualitative analysis)
GEMINI_API_KEY=your-api-key-from-aistudio.google.com

# Database (Default: SQLite - no setup needed)
DATABASE_URL=sqlite:///metadoc.db

# File Storage
UPLOAD_FOLDER=uploads
MAX_FILE_SIZE=52428800  # 50MB
```

See [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md) for detailed configuration.

---

## 📂 Project Structure

### Backend
```
backend/
├── app/
│   ├── api/              # Route handlers (auth, submission, analysis, etc.)
│   ├── services/         # Business logic (12 service classes)
│   ├── models/           # Database models (User, Submission, Rubric, etc.)
│   ├── schemas/          # Request/response DTOs
│   └── core/             # Config, extensions, utilities
├── scripts/              # Admin tools (reset DB, migrations)
├── requirements.txt      # Python dependencies (21 packages)
└── run.py               # Entry point
```

### Frontend
```
frontend/metadoc/src/
├── pages/                # Main screens (Dashboard, Submission, etc.)
├── components/           # Reusable React components
├── services/             # API client (Axios)
├── contexts/             # Global state (AuthContext)
└── styles/              # CSS stylesheets
```

---

## 🛠️ Technology Stack

| Layer | Technology |
|-------|-----------|
| **Backend Framework** | Flask 3.0.0 |
| **Database** | SQLite / PostgreSQL (SQLAlchemy ORM) |
| **Authentication** | Google OAuth 2.0 |
| **AI/NLP** | Google Gemini, SpaCy, NLTK, TextStat |
| **Reports** | ReportLab (PDF), Pandas (CSV) |
| **Frontend** | React 18, Vite, Axios |
| **Styling** | CSS3, Responsive Design |

---

## 📊 API Endpoints Overview

| Feature | Endpoint | Method |
|---------|----------|--------|
| **Authentication** | `POST /api/v1/auth/login` | POST |
| **Dashboard** | `GET /api/v1/dashboard/overview` | GET |
| **Submissions** | `POST /api/v1/submission/drive-link` | POST |
| **Analysis** | `POST /api/v1/insights/analyze/:id` | POST |
| **Metadata** | `GET /api/v1/metadata/result/:id` | GET |
| **Reports** | `GET /api/v1/reports/generate/:id` | GET |
| **Rubrics** | `POST /api/v1/rubrics/` | POST |

See [backend/README.md](backend/README.md) for complete API documentation.

---

## 🎯 Main Features Explained

### 1. **Authentication & Authorization**
- Secure Google OAuth 2.0 login
- Session-based authentication
- Role-based access control (Professor/Student)
- Whitelist integration with Class Records

### 2. **Document Submission**
- Accept Google Drive document links
- Validate file permissions
- Organize by deadline and category
- Track submission timeline

### 3. **Analysis Engine**
- Extract metadata (authors, dates, revision info)
- Perform NLP analysis (readability, sentiment)
- Generate AI insights using Gemini
- Deduplicate identity data

### 4. **Reporting & Export**
- Generate comprehensive PDF reports
- Export data to CSV format
- Include analysis results and metrics
- Support batch operations

### 5. **Rubric-Based Evaluation**
- Create custom evaluation criteria
- Define evaluation levels
- Apply to submissions
- Track scoring and feedback

---

## 🚨 Troubleshooting

### Backend Issues

**"pip install" fails**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**"ModuleNotFoundError" when running app**
```bash
# Ensure virtual environment is activated
# Windows: .\venv\Scripts\Activate.ps1
# Linux/Mac: source venv/bin/activate
```

**Database errors**
```bash
# Reset database
python scripts/reset_database.py
```

### Frontend Issues

**"npm install" fails**
```bash
npm cache clean --force
npm install
```

**Cannot connect to backend**
- Verify backend is running: http://localhost:5000
- Check CORS settings in .env
- Verify frontend proxy in vite.config.js

---

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| [QUICK_START.md](QUICK_START.md) | 10-minute setup guide ⚡ |
| [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md) | Detailed configuration guide |
| [METADOC_FINAL_SUMMARY.md](METADOC_FINAL_SUMMARY.md) | Complete system overview |
| [backend/README.md](backend/README.md) | API documentation |
| [frontend/metadoc/README.md](frontend/metadoc/README.md) | Frontend guide |

---

## 👥 Development Team

**Developers:**
- Edgar B. Quiandao Jr.
- Paul G. Abellana
- Miguel Ray A. Veloso
- Mark Christian Q. Garing

**Advisers:**
- Mr. Ralph Laviste
- Dr. Cheryl Pantaleon

---

## 📝 Project Status

✅ **Production Ready**
- Fully functional and tested
- All core features implemented
- Performance optimized
- Security best practices applied

**Last Updated:** March 2026

---

## 🤝 Contributing

When developing:

1. Create virtual environment: `python -m venv venv`
2. Activate it before coding
3. Install dependencies: `pip install -r requirements.txt`
4. Create `.env` file with API keys
5. Run backend and frontend simultaneously
6. Test changes thoroughly before committing

---

## 📞 Support

For issues or questions:
1. Check [QUICK_START.md](QUICK_START.md) or [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md)
2. Review the troubleshooting sections
3. Check the detailed documentation
4. Contact development team

---

## 📄 License

See LICENSE file for details.

---

**Ready to get started?** → 👉 [QUICK_START.md](QUICK_START.md)
- **Submission details** - View complete analysis results
- **Individual file management** - Delete specific submissions
- **Bulk operations** - Delete entire folders with all submissions

### 🔐 Authentication & Security
- **Session-based authentication** - Secure login system
- **User registration** - Email and password registration
- **Protected routes** - Role-based access control
- **Token validation** - Secure submission links with expiration

### 🎨 Modern UI/UX
- **Responsive design** - Works on desktop, tablet, and mobile
- **Clean interface** - Simple black icons, no clutter
- **Visual feedback** - Success messages and loading states
- **Smooth redirects** - Automatic navigation after actions

## 🔧 Development

### Project Structure

```
MetaDoc-Software-Project-Proposal-Evaluator/
├── backend/
│   ├── app/
│   │   ├── api/                    # API route handlers
│   │   │   ├── auth.py            # Authentication endpoints
│   │   │   ├── dashboard.py       # Dashboard endpoints
│   │   │   ├── submission.py      # Submission endpoints
│   │   │   └── metadata.py        # Metadata endpoints
│   │   ├── services/              # Business logic layer
│   │   │   ├── auth_service.py
│   │   │   ├── dashboard_service.py
│   │   │   ├── submission_service.py
│   │   │   └── metadata_service.py
│   │   ├── models/                # Database models
│   │   │   ├── user.py
│   │   │   ├── submission.py
│   │   │   ├── deadline.py
│   │   │   └── analysis.py
│   │   ├── schemas/               # Data transfer objects
│   │   │   └── dto/
│   │   ├── core/                  # Core configurations
│   │   │   ├── extensions.py     # Flask extensions
│   │   │   └── config.py         # App configuration
│   │   └── utils/                 # Utility functions
│   ├── scripts/                   # Database and utility scripts
│   │   ├── reset_database.py
│   │   └── create_test_user.py
│   ├── uploads/                   # Uploaded files storage
│   ├── temp/                      # Temporary file storage
│   ├── requirements.txt           # Python dependencies
│   ├── run.py                     # Application entry point
│   └── metadoc.db                 # SQLite database (auto-created)
├── frontend/
│   └── metadoc/
│       ├── src/
│       │   ├── pages/             # Page components
│       │   │   ├── TokenBasedSubmission.jsx    # Token-based submission form
│       │   │   ├── SubmissionDetailView.jsx    # Submission details
│       │   │   ├── Dashboard.jsx               # Professor dashboard
│       │   │   ├── Folder.jsx                  # Folder view
│       │   │   ├── Deadlines.jsx               # Deadline management
│       │   │   ├── Login.jsx                   # Login page
│       │   │   └── Register.jsx                # Registration page
│       │   ├── components/        # Reusable components
│       │   ├── services/          # API service layer
│       │   │   └── api.js
│       │   ├── contexts/          # React contexts
│       │   │   └── AuthContext.jsx
│       │   ├── styles/            # CSS stylesheets
│       │   └── App.jsx            # Main app component
│       ├── vite.config.js         # Vite configuration
│       └── package.json           # Node dependencies
└── README.md                      # This file
```

### Development Workflow

**Starting the Application:**

```bash
# Terminal 1 - Backend
cd backend
.\venv\Scripts\Activate.ps1  # Windows
python run.py

# Terminal 2 - Frontend
cd frontend/metadoc
npm run dev
```

**Resetting the Database:**

```bash
cd backend
python scripts/reset_database.py
```

**Creating Test Users:**

```bash
cd backend
python scripts/create_test_user.py
```

## 🐛 Troubleshooting

### Backend Won't Start

**Issue**: `ModuleNotFoundError` or import errors

**Solution**: 
```bash
# Ensure virtual environment is activated
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate      # Linux/Mac

# Reinstall dependencies
pip install -r requirements.txt
```

### Frontend CORS Errors

**Issue**: `Failed to fetch` or CORS errors in browser console

**Solution**: 
1. Ensure backend is running on `http://localhost:5000`
2. Check `vite.config.js` proxy configuration
3. Clear browser cache and restart frontend

### Database Locked Error

**Issue**: `database is locked` error

**Solution**: 
```bash
# Close all Python processes
# On Windows Task Manager, end all python.exe processes
# Then restart the backend
```

### Port Already in Use

**Issue**: `Address already in use` error

**Solution**:
```bash
# Windows - Kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:5000 | xargs kill -9
```

### Login Not Working

**Issue**: Login fails or session not persisting

**Solution**:
1. Clear browser cookies and localStorage
2. Check backend logs for errors
3. Verify user exists in database
4. Reset database and create new test user

## 📱 User Guide

### For Professors

1. **Register/Login**
   - Navigate to `http://localhost:5173`
   - Register with email and password
   - Login to access dashboard

2. **Create Deadline**
   - Go to "Deadline Management"
   - Click "Create New Deadline"
   - Fill in title, description, and deadline date
   - Click "Create Deadline"

3. **Generate Submission Link**
   - In deadline card, click "Generate Link"
   - Copy the submission link
   - Share with students

4. **View Submissions**
   - Go to "Folders"
   - Click on a deadline folder
   - View all submitted files
   - Click on a file to see detailed analysis

5. **Delete Submissions**
   - Click trash icon next to a file to delete it
   - Click folder delete to remove entire deadline (deletes all files inside)

### For Students

1. **Access Submission Link**
   - Click the unique link provided by your professor.
   - Login with your **Gmail** account to verify your authorization.

2. **Verify Whitelist Status**
   - If your email is in the Class Record for this deadline, the form will unlock.
   - If not, you will see an "Account Not Authorized" message.

3. **Submit via Google Drive**
   - Paste your Google Drive link into the submission box.
   - **Important**: Ensure the document is shared with the MetaDoc Service Account if prompted.
   - Click "Validate & Submit".

4. **Review Status**
   - Once submitted, the system will immediately begin metadata extraction and NLP analysis.
   - You will see a "Submission Successful" message once the job is enqueued.

3. **Submission Requirements**
   - File must be in DOCX format
   - File size must be under 50MB
   - File must contain actual content (not empty)

## 🔌 API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login-basic` - Login with email/password
- `POST /api/v1/auth/logout` - Logout current session
- `GET /api/v1/auth/validate` - Validate session
- `POST /api/v1/auth/generate-submission-token` - Generate submission link

### Dashboard
- `GET /api/v1/dashboard/overview` - Get dashboard statistics
- `GET /api/v1/dashboard/submissions` - List all submissions
- `GET /api/v1/dashboard/submissions/:id` - Get submission details
- `DELETE /api/v1/dashboard/submissions/:id` - Delete submission
- `GET /api/v1/dashboard/deadlines` - List deadlines
- `POST /api/v1/dashboard/deadlines` - Create deadline
- `PUT /api/v1/dashboard/deadlines/:id` - Update deadline
- `DELETE /api/v1/dashboard/deadlines/:id` - Delete deadline (and all submissions)

### Submission
- `GET /api/v1/submission/token-info` - Get deadline info from token
- `POST /api/v1/submission/upload` - Upload document
- `GET /api/v1/submission/status/:id` - Check submission status

### Metadata
- `GET /api/v1/metadata/result/:id` - Get analysis results

## 🤝 Contributing

### For Team Members

1. **Before starting work**:
   - Pull latest changes: `git pull`
   - Activate virtual environment
   - Install any new dependencies

2. **Before committing**:
   - Test your changes locally
   - Update documentation if needed
   - Don't commit `.env` files
   - Update `requirements.txt` if you added packages

3. **Code style**:
   - Follow PEP 8 for Python
   - Use ESLint for JavaScript/React
   - Add comments for complex logic
   - Write descriptive commit messages

## 📄 License

This project is developed for Cebu Institute of Technology – University as part of the capstone project requirements.

## 👥 Development Team

- **Edgar B. Quiandao Jr.** - Backend Developer
- **Paul G. Abellana** - Backend Developer
- **Miguel Ray A. Veloso** - Frontend Developer
- **Mark Christian Q. Garing** - Full Stack Developer

**Advisers**: Mr. Ralph Laviste & Dr. Cheryl Pantaleon

---

## 🆘 Need Help?

- **Setup Issues**: See [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md)
- **API Questions**: See [backend/README.md](backend/README.md)
- **Bug Reports**: Contact the development team
- **Feature Requests**: Discuss with advisers

---

**Version**: 1.0.0  
**Last Updated**: December 2025  
**Institution**: Cebu Institute of Technology - University

# 🚀 AI Resume Analyzer & Job Matching Platform

An AI-powered backend system that analyzes resumes, matches them with job descriptions, and provides ATS scores along with actionable improvement suggestions.

---

## 🌐 Live Demo

🔗 Frontend : https://skill-fit-resume.netlify.app
🔗 Backend API: https://resume-analyzer-0tc9.onrender.com

---

## 🧠 Features

* 🔐 **JWT Authentication**

  * Secure user registration & login
* 📄 **Resume Upload**

  * Upload PDF resumes
* 📊 **PDF Parsing**

  * Extract text from resumes using pdfplumber
* 🧠 **Skill Extraction (NLP)**

  * Identify technical skills from resume content
* 🎯 **Job Matching Engine**

  * Compare resume with job description
* 📈 **ATS Score Calculation**

  * Generate match score + ATS score
* 💡 **AI Suggestions**

  * Recommend missing skills and improvements
* 🌍 **Deployed Backend**

  * Hosted on Render for real-world access
* 💻 **Frontend UI**

  * Simple interface built with HTML, CSS, JavaScript

---

## 🏗️ Tech Stack

### Backend

* Django
* Django REST Framework
* JWT Authentication (SimpleJWT)

### AI / Processing

* pdfplumber
* Rule-based NLP for skill extraction

### Database

* SQLite (development)
* PostgreSQL-ready (production)

### Frontend

* HTML
* CSS
* JavaScript (Fetch API)

### Deployment

* Render
* Gunicorn
* Whitenoise

---

## 📁 Project Structure

```
resume-analyzer/
│
├── backend/
│   ├── config/
│   ├── apps/
│   │   ├── accounts/
│   │   ├── resumes/
│   │   ├── analysis/
│   │   ├── jobs/
│   │   └── common/
│
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── style.css
│   └── script.js
│
├── requirements.txt
├── build.sh
├── Procfile
└── README.md
```

---

## 🔌 API Endpoints

### Authentication

* `POST /api/auth/register/`
* `POST /api/auth/login/`

### Resume

* `POST /api/resumes/upload/`

### Analysis

* `POST /api/analysis/analyze/`

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone https://github.com/Slayezs/resume-analyzer.git
cd resume-analyzer
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file:

```
SECRET_KEY=your-secret-key
DEBUG=True
```

---

### 5️⃣ Run Migrations

```
cd backend
python manage.py migrate
```

---

### 6️⃣ Start Server

```
python manage.py runserver
```

---

## 🧪 Usage Flow

1. Register a new user
2. Login to get JWT token
3. Upload resume
4. Enter job description
5. Get:

   * Match score
   * ATS score
   * Missing skills
   * Suggestions

---

## 💡 Future Improvements

* 🔥 React-based frontend
* 🤖 LLM-based suggestions (OpenAI / Gemini)
* 📊 Dashboard with history tracking
* 📄 Support for DOCX parsing
* ☁️ Full PostgreSQL production setup

---

## 🧠 Key Highlights

* Modular backend architecture using Django apps
* Service-layer design for scalability
* Real-world deployment on cloud
* Integration of AI/NLP with backend systems

---

## 📬 Contact

**Chirag Singh**
📧 [chirag00200300@gmail.com]
🔗 GitHub: https://github.com/Slayezs/resume-analyzer.git

---

⭐ If you found this project useful, consider giving it a star!

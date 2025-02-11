# 🏗️ System Architecture Overview

## **📌 Overview**
The **AI-Powered Smart Task Manager** is a full-stack web application that allows users to manage tasks efficiently with AI-powered prioritization and smart reminders.

---

## **🔹 Technology Stack**
### **Backend (Flask API)**
- **Flask** - Web framework
- **Flask-JWT-Extended** - Authentication
- **Flask-SQLAlchemy** - Database ORM
- **Flask-CORS** - Handles cross-origin requests
- **PostgreSQL/SQLite** - Database

### **Frontend (React.js)**
- **React.js** - Frontend framework
- **Axios** - API requests
- **Bootstrap / Tailwind CSS** - Styling

### **AI & Services**
- **Task Prioritization AI** - Uses ML/AI models
- **Email/SMS Notifications** - Flask Mail / Twilio

---

## **🔹 System Architecture Diagram**
```
+----------------+          +----------------+
|  React Frontend |  <--->  |  Flask Backend |
+----------------+          +----------------+
       |                        |
       v                        v
+----------------+          +----------------+
|  PostgreSQL DB |  <--->  |  AI Prioritization |
+----------------+          +----------------+
```

---

## **🔹 Component Breakdown**
### **1️⃣ Backend (Flask API)**
- `app.py` - Main application entry point
- `auth.py` - User authentication (Signup/Login)
- `tasks.py` - Task management API
- `database.py` - Defines models (User, Task)
- `config.py` - Configuration settings

### **2️⃣ Frontend (React.js UI)**
- `src/components/TaskList.js` - Displays tasks
- `src/pages/Login.js` - User authentication page
- `src/services/api.js` - Handles API calls

### **3️⃣ AI Task Prioritization**
- Uses **machine learning models** to sort tasks
- Adjusts **task urgency** based on past behavior

### **4️⃣ Notification System**
- **Flask-Mail** - Sends email reminders
- **Twilio API** - Sends SMS notifications

---

## **🔹 Deployment Strategy**
- **Backend** → Deployed on **Render** (or AWS/GCP)
- **Frontend** → Deployed on **Vercel/Netlify**
- **Database** → Hosted on **PostgreSQL (Supabase/AWS RDS)**

---

## **📌 Summary**
- **Modular & scalable** architecture
- **AI-driven task prioritization**
- **Secure authentication with JWT**
- **Automated reminders & notifications**

This architecture ensures that the application is **scalable, efficient, and AI-powered** for optimal task management.


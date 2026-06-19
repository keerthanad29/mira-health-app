<div align="center">

# 🏥 MIRA - Medical Intelligence Robotic Automation

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)

> **AI-powered health prediction app that analyzes patient blood test results and predicts possible health conditions.**

</div>

---

## 📌 Objective
Build a health prediction application that collects patient blood test data, stores it securely, and uses AI to generate intelligent health risk assessments automatically.

---

## 🎯 Project Highlights

| What | Detail |
|------|--------|
| 🖥️ Frontend | Streamlit (Python) |
| 🗄️ Database | SQLite |
| 🤖 AI Model | LLaMA 3.3 70B via Groq API |
| 📋 Operations | Full CRUD |
| 🔒 Security | API keys via .env file |

---

## 🗂️ Project Structure

```
mira-health-app/
│
├── app.py              # Main Streamlit UI
├── database.py         # SQLite CRUD operations
├── ai_service.py       # Groq AI API integration
├── requirements.txt    # Dependencies
├── .gitignore          # Excludes .env and mira.db
└── README.md
```

---

## 🛠️ Tech Stack
- **Streamlit** — Frontend & Backend
- **SQLite** — Persistent storage
- **Groq API (LLaMA 3.3 70B)** — AI health prediction
- **python-dotenv** — Secure API key management

---

## 📋 Patient Fields

| Field | Type | Validation |
|-------|------|-----------|
| Full Name | Text | Required |
| Date of Birth | Date | Cannot be future date |
| Email Address | Email | Valid format required |
| Glucose | Number | Must be greater than 0 |
| Haemoglobin | Number | Must be greater than 0 |
| Cholesterol | Number | Must be greater than 0 |
| Remarks | Text | AI Generated |

---

## ⚙️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/keerthanad29/mira-health-app.git
cd mira-health-app
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your API key
Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the app
```bash
streamlit run app.py
```

---

## 💡 What I Learned
- Building **full-stack Python apps** with Streamlit
- Integrating **AI APIs** for real-world predictions
- Implementing **CRUD operations** with SQLite
- Securing credentials using **environment variables**
- Applying **input validation** for data integrity

---

## 🔮 Future Improvements
- [ ] Add patient login & authentication
- [ ] Export patient records as PDF
- [ ] Add more blood test parameters
- [ ] Deploy to cloud (Streamlit Cloud)
- [ ] Add graphs for blood value trends
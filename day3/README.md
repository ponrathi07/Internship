# ChatMate – Interactive Chatbot & Student Analytics

**Day 3 | Python Internship | 2026**

## Project Overview

ChatMate is a Python-based application that combines an interactive chatbot with a student performance reporting system.

The chatbot communicates with users, remembers previous conversations, and generates keyword-based responses. The student analytics module reads academic records from a CSV file and generates individual performance summaries and an overall class average.

The project demonstrates how Python can be used to build applications using Object-Oriented Programming, file handling, data storage, and modular programming.

## Key Features

### 1. Interactive Chatbot
- Personalized chatbot name using environment variables.
- Keyword-based automatic responses.
- Stores user and bot conversations.
- Saves conversation history in JSON format.
- Loads previous conversations when restarted.
- Handles missing or invalid JSON files.

### 2. Student Performance Analytics
- Reads student records from a CSV file.
- Calculates individual student averages.
- Displays academic performance.
- Calculates the overall class average.
- Handles missing files and invalid student records.

## Project Architecture

```text
ChatMate
│
├── Chatbot Module
│   ├── ChatBot Class
│   ├── Message Management
│   ├── Reply Generation
│   └── JSON History Storage
│
└── Student Analytics Module
    ├── CSV Data Reading
    ├── Individual Average
    └── Class Performance Summary
```

## Technologies & Concepts

| Technology | Application |
|---|---|
| Python 3 | Core programming |
| OOP | Classes, objects and inheritance |
| JSON | Conversation storage |
| CSV | Student data management |
| Exception Handling | Error management |
| python-dotenv | Environment configuration |
| Type Hints | Code readability |
| Git & GitHub | Version control |

## Project Structure

```text
day3/
│
├── main.py
├── chatbot.py
├── student_report.py
├── students.csv
├── chat_history.json
├── .env
├── .env.example
├── requirements.txt
└── README.md
```

*Note: chat_history.json is generated automatically when the chatbot saves its first conversation.*

## Installation & Execution

**1. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**2. Configure environment variables**

Create a `.env` file:

```env
BOT_NAME=ChatMate
```

**3. Run the chatbot**

```bash
python main.py
```

**4. Generate the student report**

```bash
python student_report.py
```

## Sample Student Report

```text
STUDENT REPORT

Anu - Average: 87.67
Bala - Average: 75.00
Kavi - Average: 65.67
Ravi - Average: 92.33

Class Average: 80.17
Student report process completed.
```

## Learning Outcomes

Through this project, I gained practical experience in:

- Designing reusable Python classes and methods.
- Implementing inheritance and object-oriented programming.
- Handling errors using try-except-finally.
- Reading and writing JSON and CSV files.
- Creating modular Python applications.
- Managing application settings using environment variables.
- Organizing and maintaining projects using GitHub.

---

**Developed as part of the Python Internship – Day 3.**
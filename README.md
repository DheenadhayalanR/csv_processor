# Django CSV Processing with Celery

## 📌 Overview
This is a Django web application that allows users to:
- Upload CSV files 📂
- Process them asynchronously using Celery 🏗️
- Perform calculations (sum, average, count) 📊
- Display processed results dynamically on the frontend 🚀
- Search data by product name 🔍

## 🚀 Features
- **Asynchronous processing** with Celery (No waiting!)
- **Redis as a message broker**
- **Django models for file storage**
- **Dynamic search feature**
- **Results processed in-memory (no DB storage for CSV data)**

---

## 📦 Installation

### **1️⃣ Clone the Repository**
```bash
git clone <your-github-repo-url>
cd csv_processor


- Create and Activate Virtual Environment
- Install Dependencies
- Start Redis ( sudo service redis-server start )
- Apply Migrations
- Start Django Server ( python manage.py runserver )
- Start Celery ( celery -A csv_processor worker --loglevel=info )
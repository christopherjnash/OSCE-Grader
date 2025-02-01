# OSCE Grader Setup 🚀  
An AI-powered grading system for medical student OSCE post-encounter notes, using GPT models to automate grading and provide structured feedback.  

## ✨ Features  
✅ Supports **Excel, CSV, and text-based** student notes  
✅ Works with **structured rubrics** (Excel, CSV)  
✅ Uses **ChatGPT (or other LLMs)** to generate **detailed, section-by-section grading**  
✅ Customizable **grading prompts** tailored to your institution  
✅ **Automatic logging** for debugging and analysis  
✅ **Easy setup** with Python & OpenAI API  

---

## 📌 Getting Started  
### **1️⃣ Install Dependencies**  
You'll need **Python 3.8+** and an OpenAI API key.  

#### **Windows/Mac/Linux**  
```sh
git clone https://github.com/YOUR_GITHUB/osce-grader.git
cd osce-grader
pip install -r requirements.txt

---

Set Up Your OpenAI API Key
Sign up at OpenAI
Go to API Keys → Generate a new key
Save your key in a .env file or api_key.txt
sh
Copy
Edit
echo "YOUR_API_KEY" > api_key.txt

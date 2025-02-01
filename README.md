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

#### **Mac/Linux**  
```sh  
git clone https://github.com/christopherjnash/OSCE-Grader.git  
cd OSCE-Grader  
pip install -r requirements.txt  
```

#### **Windows (PowerShell)**  
```powershell  
git clone https://github.com/christopherjnash/OSCE-Grader.git  
cd OSCE-Grader  
pip install -r requirements.txt  
```

---

### **2️⃣ Set Up Your OpenAI API Key**  
1. Sign up at **[OpenAI](https://platform.openai.com/signup/)**  
2. Go to **API Keys** → Generate a new key  
3. Save your key in a `.env` file or `api_key.txt`  
   ```sh  
   echo "YOUR_API_KEY" > api_key.txt  
   ```

---

### **3️⃣ Run the OSCE Grader**  
#### **Basic Usage**  
```sh  
python grader.py --rubric standardrubric.xlsx --notes student_notes.xlsx --output results.xlsx  
```

#### **Optional Parameters**  
| Flag | Description |  
|------|------------|  
| `--rubric` | Path to the grading rubric (Excel/CSV) |  
| `--notes` | Path to student notes (Excel/CSV) |  
| `--output` | Name of the output file (Excel) |  

---

## ⚙️ **Customizing the Grading Prompt**  
- The script **grades section-by-section** for higher accuracy.  
- You can modify the **grading prompt** in `config.py` without editing JSON.  

Example:  
```plaintext  
SYSTEM MESSAGE:  
"I am a medical educator, and I need your help grading an assignment.  
My students recently completed an OSCE post-encounter note based on a standardized patient interview.  
I have provided a structured scoring rubric with expected responses.  
The rubric is broken into individual sections. To ensure accuracy, please score each section separately.  
For each section, provide a detailed explanation of your reasoning before giving a final score.  
At the end of your evaluation, place the final score as an integer on a new line with no markup."
```
- **Modify this text** in `config.py` if your institution requires a different approach.

---

## 📚 Troubleshooting  
### **💡 Common Issues & Fixes**  
🔹 **API Key Not Found**  
👉 Make sure `api_key.txt` exists or export your key:  
```sh  
export OPENAI_API_KEY="your-key-here"  
```

🔹 **Unexpected Scores or Formatting Issues**  
👉 Enable debugging mode:  
```sh  
python grader.py --debug  
```

🔹 **Invalid File Format**  
👉 Convert Word/PDF rubrics to Excel/CSV using the `convert_rubric.py` script.  

---

## 📠 Resources  
📌 **GitHub Repository:** [OSCE-Grader](https://github.com/christopherjnash/OSCE-Grader)  
📌 **OpenAI API Docs:** [OpenAI](https://platform.openai.com/docs/)  
📌 **Troubleshooting Guide:** See `docs/troubleshooting.md`  

---

## 💜 License  
**MIT License** – Free to use and modify.  
See [`LICENSE`](LICENSE) for details.  

---

## 🎤 Contributions  
Contributions are welcome! If you improve the script or add new features, submit a **pull request** or open an **issue**.  

🚀 **Happy Grading!**


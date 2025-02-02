# OSCE Grader Setup Guide 🚀  
An AI-powered grading system for medical student OSCE post-encounter notes, using GPT models to automate grading and provide structured feedback.  

## ✨ Features  
✅ Supports **Excel, CSV, and text-based** student notes  
✅ Works with **structured rubrics** (Excel, CSV)  
✅ Uses **ChatGPT (or other LLMs)** to generate **detailed, section-by-section grading**  
✅ Customizable **grading prompts** via `config.py`  
✅ **Automatic logging** for debugging and analysis  
✅ **Easy setup** with Python & OpenAI API  
✅ Includes **convert_rubric.py** to assist in converting rubric files (PDF/DOCX to structured formats)  

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

### **2️⃣ Configure the Grader**  
The **grading prompt, model selection, API key location, and default file paths** are managed in `config.py`.  
Modify `config.py` as needed to customize the grading behavior for your institution.  

Example of `config.py` settings:  
```python  
MODEL = "gpt-4o-mini"
DEFAULT_RUBRIC_PATH = "examples/sample_rubric.xlsx"
DEFAULT_NOTES_PATH = "examples/sample_notes.xlsx"
DEFAULT_OUTPUT_PATH = "results.xlsx"
```

---

### **3️⃣ Set Up Your OpenAI API Key**  
1. Sign up at **[OpenAI](https://platform.openai.com/signup/)**  
2. Go to **API Keys** → Generate a new key  
3. Save your key in a file named `api_key.txt` in the root folder.  

---

### **4️⃣ Run the OSCE Grader**  
#### **Basic Usage**  
```sh  
python scripts/grader.py --rubric examples/sample_rubric.xlsx --notes examples/sample_notes.xlsx --output results.xlsx  
```

#### **Optional Parameters**  
| Flag | Description |  
|------|------------|  
| `--rubric` | Path to the grading rubric (Excel/CSV) |  
| `--notes` | Path to student notes (Excel/CSV) |  
| `--output` | Name of the output file (Excel) |  

---

## 🔄 Converting a Rubric File  
If your rubric is in **PDF or DOCX**, you can convert it to a structured format (Excel or CSV) using `convert_rubric.py`.  

**Example Usage:**  
```sh  
python scripts/convert_rubric.py examples/FlankPainRubric.pdf examples/sample_rubric.xlsx  
```

⚠️ **Note:** `convert_rubric.py` is a **starting point** for rubric conversion and may require manual adjustments based on formatting inconsistencies.  

---

## ⚙️ **Customizing the Grading Prompt**  
- The script **grades section-by-section** for higher accuracy.  
- You can modify the **grading prompt** in `config.py` without editing JSON.  

Example:  
```python  
GRADING_PROMPT = "I am a medical educator, and I need your help grading an assignment... (your modified prompt)"
```

---

## 🛠 Troubleshooting  
### **💡 Common Issues & Fixes**  
🔹 **API Key Not Found**  
👉 Ensure `api_key.txt` exists in the root folder.  

🔹 **Unexpected Scores or Formatting Issues**  
👉 Modify the grading prompt in `config.py` to better fit your rubric.  

🔹 **Invalid File Format**  
👉 Convert Word/PDF rubrics to Excel/CSV using `convert_rubric.py`.  

---

## 🔗 Resources  
📌 **GitHub Repository:** [OSCE-Grader](https://github.com/christopherjnash/OSCE-Grader)  
📌 **OpenAI API Docs:** [OpenAI](https://platform.openai.com/docs/)  
📌 **Troubleshooting Guide:** See `docs/troubleshooting.md`  

---

## 📜 License  
**MIT License** – Free to use and modify.  
See [`LICENSE`](LICENSE) for details.  

---

## 🎤 Contributions  
Contributions are welcome! If you improve the script or add new features, submit a **pull request** or open an **issue**.  

🚀 **Happy Grading!**

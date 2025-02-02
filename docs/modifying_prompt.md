# Modifying the Grading Prompt

## 🎯 Why Modify the Prompt?
The grading prompt determines how ChatGPT evaluates and scores student responses. Customizing it ensures that the model aligns with **your institution's rubric and grading style.**

---
## 📌 Default Grading Prompt
The default prompt used in `grader.py` follows this structure:

```plaintext
SYSTEM MESSAGE:
"I am a medical educator, and I need your help grading an assignment.
My students recently completed an OSCE post-encounter note based on a standardized patient interview.
I have provided a structured scoring rubric with expected responses.
The rubric is broken into individual sections. To ensure accuracy, please score each section separately.
For each section, provide a detailed explanation of your reasoning before giving a final score.
At the end of your evaluation, place the final score as an integer on a new line with no markup."
```

---
## 🛠 How to Modify the Prompt
### **Option 1: Modify `config.py` (Recommended)**
You can edit `config.py` to update the grading prompt without changing the script logic.

Example:
```python
SYSTEM_PROMPT = "I am a medical educator... (your modified prompt)"
```

### **Option 2: Edit `grader.py` Directly**
Locate the section in `grader.py` that defines the **system message** and update it:

```python
messages = [
    {"role": "system", "content": "Your modified prompt text here."}
]
```

---
## 🎯 Best Practices for Prompt Customization
✅ **Be Clear & Specific** – Define exactly what you want ChatGPT to evaluate.  
✅ **Use Examples** – Provide sample student responses and expected answers in the rubric.  
✅ **Avoid Overloading** – Keep prompts concise to prevent AI confusion.  
✅ **Test & Iterate** – Run a few test cases to refine performance.  

---
## 🔍 Testing Your Changes
After modifying the prompt, test its effectiveness:
```sh
python scripts/grader.py --rubric examples/sample_rubric.xlsx --notes examples/sample_notes.xlsx --output results.xlsx
```

If the results aren't what you expect, tweak the prompt further and **re-run the script.**

🚀 **A well-tuned prompt ensures accurate and fair grading!**


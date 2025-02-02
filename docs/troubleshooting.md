# OSCE Grader Troubleshooting Guide

## 🔹 Common Issues & Fixes

### ❌ API Key Not Found
**Issue:**
- The script fails to run with an API key error.

**Fix:**
1. Ensure you have an **OpenAI API Key**.
2. Save your API key inside a file named `api_key.txt` in the root folder.
3. If using an environment variable, set it manually:
   ```sh
   export OPENAI_API_KEY="your-key-here"
   ```

### ❌ Dependencies Not Installed
**Issue:**
- The script throws an error about missing Python packages.

**Fix:**
- Install all required dependencies by running:
  ```sh
  pip install -r requirements.txt
  ```

### ❌ File Format Issues
**Issue:**
- The script crashes when loading student notes or rubric files.

**Fix:**
1. Ensure files are in **Excel (`.xlsx`) or CSV (`.csv`)** format.
2. Convert Word/PDF rubrics to Excel/CSV using `convert_rubric.py`.
3. Check that column headers in Excel match expected fields.

### ❌ Unexpected Scores or Formatting Issues
**Issue:**
- The grading output seems incorrect or inconsistent.

**Fix:**
1. Ensure that your **grading rubric is formatted correctly**.
2. If necessary, **modify the grading prompt** to match institutional needs (see [Modifying Prompt Guide](docs/modifying_prompt.md)).
3. Run the script in **debug mode** to inspect responses:
   ```sh
   python scripts/grader.py --debug
   ```

### ❌ API Rate Limits Exceeded
**Issue:**
- The script fails due to OpenAI API rate limits.

**Fix:**
1. Reduce the request rate (e.g., **batch process fewer notes** at a time).
2. Upgrade to a **higher-tier OpenAI plan** if applicable.

### ❌ Other Issues
- Check the [GitHub Issues](https://github.com/christopherjnash/OSCE-Grader/issues) for ongoing bug reports.
- If you encounter a unique issue, **submit a GitHub issue** with error details.

🚀 **Follow these steps, and your OSCE Grader should run smoothly!**


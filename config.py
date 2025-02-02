# OSCE Grader Configuration File

# OpenAI API Key (loaded from external file for security)
API_KEY_FILE = "api_key.txt"

# Model Selection
MODEL = "gpt-4o-mini"

# Default Grading Prompt
GRADING_PROMPT = """I am a medical educator, and I need your help grading an assignment.
My students recently completed an OSCE post-encounter note based on a standardized patient interview.
I have provided a structured scoring rubric with expected responses.
The rubric is broken into individual sections. To ensure accuracy, please score each section separately.
For each section, provide a detailed explanation of your reasoning before giving a final score.
At the end of your evaluation, place the final score as an integer on a new line with no markup."""

# Default Temperature & Top-P (Not emphasized but configurable)
TEMPERATURE = 0.5
TOP_P = 1.0

# File Paths (Users can set defaults here)
DEFAULT_RUBRIC_PATH = "examples/sample_rubric.xlsx"
DEFAULT_NOTES_PATH = "examples/sample_notes.xlsx"
DEFAULT_OUTPUT_PATH = "results.xlsx"

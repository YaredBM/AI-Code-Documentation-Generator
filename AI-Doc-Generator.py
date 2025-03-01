import os
import openai
import ast
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_docstring(code_snippet):
    """Sends code snippet to OpenAI API for docstring generation."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI that generates clear and concise docstrings for Python functions."},
            {"role": "user", "content": f"Generate a Python docstring for the following function:
```python
{code_snippet}
```"}
        ]
    )
    return response["choices"][0]["message"]["content"]

def extract_functions_from_code(code):
    """Parses Python code and extracts functions."""
    tree = ast.parse(code)
    functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
    return functions

def process_code(code):
    """Generates docstrings for all functions in the given Python code."""
    functions = extract_functions_from_code(code)
    updated_code = code
    
    for func in functions:
        func_source = ast.unparse(func)
        docstring = generate_docstring(func_source)
        updated_code = updated_code.replace(func_source, f"""{func_source}\n    \"\"\"{docstring}\"\"\"""
        )
    
    return updated_code

@app.route("/generate", methods=["POST"])
def generate_documentation():
    """API endpoint to generate documentation."""
    data = request.json
    if "code" not in data:
        return jsonify({"error": "Code is required"}), 400
    
    processed_code = process_code(data["code"])
    return jsonify({"updated_code": processed_code})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

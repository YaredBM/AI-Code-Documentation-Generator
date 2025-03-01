# AI-Code-Documentation-Generator
An AI-powered tool that automatically generates docstrings, class/module summaries, and README documentation based on source code analysis. This tool integrates with GitHub Actions and can be used locally or as an API service to keep your documentation up to date.

🚀 Features

✅ Docstring Generation – AI generates function and class docstrings based on logic.

✅ Module & Class Summarization – Creates structured documentation for entire modules.

✅ Auto README Generator – Parses project files and generates a structured README.md.

✅ Code Commenting – AI suggests inline comments for better clarity.

✅ GitHub CI/CD Integration – Automatically runs on new commits to ensure up-to-date documentation.

✅ Multi-Language Support – Python, JavaScript, and Java (extendable).

✅ Custom Prompt Templates – Users can define AI behavior for documentation style.

📌 Prerequisites

-Before using this tool, ensure you have the following:
-Python 3.8+ installed
-pip (Python package manager)
-OpenAI API Key (for AI-based documentation)
-GitHub Repository (for CI/CD integration)
-Docker (optional for deployment)

🛠 Installation & Setup

1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/ai-doc-generator.git
cd ai-doc-generator
```
2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
3️⃣ Set Environment Variables
```sh
Create a .env file and add the following credentials:
OPENAI_API_KEY=your_openai_api_key
```
4️⃣ Run the AI Documentation Generator Locally
```sh
python app.py
This starts the API server on http://localhost:5000.
```

🔗 API Usage

Generate AI-Powered Documentation

Send a POST request with the code snippet to get AI-generated docstrings.

Request:
```sh
curl -X POST "http://localhost:5000/generate" -H "Content-Type: application/json" -d '{"code": "def add(a, b): return a + b"}'
```
Response:
```sh
{
"updated_code": "def add(a, b):\n    """Adds two numbers and returns the sum."""\n    return a + b"
}
```
🚀 Deployment

🐳 Docker Deployment

Build Docker Image
```sh
docker build -t ai-doc-generator .
```
Run the Container
```sh
docker run -p 5000:5000 --env-file .env ai-doc-generator
```
☁️ Deploy on Azure

1. Create an Azure App Service or Azure Functions.
2. Set environment variables in Azure.
3. Deploy the Flask app using GitHub Actions.
🛠 GitHub Actions Integration

Automatically generate documentation for new pull requests using GitHub Actions.

1️⃣ Create a .github/workflows/docs.yml file:

name: Generate Documentation

on:
pull_request:
branches:
- main

jobs:
generate-docs:
runs-on: ubuntu-latest
steps:
- name: Checkout code
uses: actions/checkout@v3

- name: Set up Python
    uses: actions/setup-python@v3
    with:
      python-version: '3.8'

  - name: Install dependencies
    run: pip install -r requirements.txt

  - name: Generate Documentation
    run: |
      python app.py

2️⃣ Commit & Push to GitHub
```sh
git add .
git commit -m "Added GitHub Actions for AI documentation"
git push origin main
```
Now, every time a pull request is made, the AI bot will automatically generate documentation and update code files.

🤖 Example AI-Generated Docstring
```sh
def multiply(x, y):
"""Multiplies two numbers and returns the product."""
return x * y
```

🎯 Roadmap

-Extend support to JavaScript, TypeScript, and Java.
-Add integration with Azure OpenAI Service.
-Improve AI suggestions with fine-tuned models.
-Implement README.md ato-generation for full projects.
-Deploy as a SaaS GitHub App.

📝 Contributing

Contributions are welcome! To contribute:
1. Fork the repository
2. Create a feature branch (git checkout -b feature-xyz)
3. Commit changes (git commit -m "Added new feature")
4. Push to the branch (git push origin feature-xyz)
5. Open a Pull Request

**📌 Overview**

ASK AITELA BOT is an AI-powered chatbot built using Streamlit that allows users to upload PDF documents and interact with them through a conversational interface. Users can ask questions about the content, summarize sections, extract key insights, and more.

**🚀 Features**

📂 Upload multiple PDF files

💬 Chat with your documents using natural language

🔍 Extract key information and insights

📑 Summarize long sections efficiently

🔒 Secure and private document handling using FAISS vector storage

**🛠️ Tech Stack**

Framework: Streamlit

Backend: Python

AI Model: OpenAI GPT via ChatOpenAI

Text Processing: PyPDF2, LangChain

Vector Storage: FAISS

Memory Management: ConversationBufferMemory

Environment Management: Python dotenv

**📌 Installation & Setup**

Prerequisites

Ensure you have the following installed:

Python 3.x

Virtual environment (optional but recommended)

Setup Steps

Clone the repository:

git clone https://github.com/your-repo/ask-aitela-bot.git
cd ask-aitela-bot

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app.py

**🎯 Usage**

Open the app in a browser.

Upload one or multiple PDF documents via the sidebar.

Click on “Process” to extract and analyze the text.

Ask questions about the document using the chat input field.

**🔐 Security & Privacy**

All uploaded PDFs are processed locally.

No user data is stored permanently unless configured.

HTTPS is recommended for secure communication.

**🤝 Contributing**

Fork the repository

Create a feature branch (git checkout -b feature-name)

Commit changes (git commit -m 'Add feature')

Push to branch (git push origin feature-name)

Create a pull request

**📧 Contact**

For questions or suggestions, feel free to open an issue or reach out via email: your-email@example.com

**📜 License**

This project is licensed under the MIT License - see the LICENSE file for details.

# 🔠 Name Matching System (Flask + LangChain + FAISS)

This project is a simple **name matching system** built with **Flask**, **LangChain**, **FAISS**, and **HuggingFace sentence-transformer embeddings**.  

The system allows users to input a name and find the **closest matches** from a dataset of names. It returns the **best match** along with a ranked list of other similar names.

---

## 🚀 Features
- Embedding-based **name similarity search** (not just string matching).
- Uses **FAISS vector database** for fast similarity lookup.
- Frontend built with **HTML, CSS, and JavaScript**.
- Backend powered by **Flask** with CORS enabled.
- Works offline using **HuggingFace embeddings**.

---

## 📂 Project Structure
  project/
  │── index.py # Flask backend
  │── templates/
  │ └── index.html # Frontend (HTML + JS)
  │── requirements.txt # Python dependencies
  │── README.md # Project documentation

  
---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/name-matcher.git
cd name-matcher


2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Virtual Environment

On Windows:

venv\Scripts\activate


On Mac/Linux:

source venv/bin/activate

4️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the App

Start the Flask server:

python index.py


By default, the server runs at:

http://127.0.0.1:5000

🌐 Frontend

Open http://127.0.0.1:5000 in your browser to access the frontend UI.
Enter a name, click Find Matches, and you’ll see:

Best Match (closest name + similarity score)

Other Matches (ranked list with scores)

🛠️ Technologies Used

Python 3.8+

Flask (backend framework)

Flask-CORS (cross-origin requests)

LangChain + FAISS (vector database search)

HuggingFace Sentence Transformers (all-MiniLM-L6-v2)

HTML, CSS, JS (frontend)

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

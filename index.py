from flask import Flask, request, jsonify,render_template
from flask_cors import CORS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


app = Flask(__name__)
CORS(app)



embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

from flask import Flask, request, jsonify
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


app = Flask(__name__)


embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


names = [
    "Geetha", "Gita", "Gitu", "Geeta", "Gitika", "Githu", "Geetanjali",
    "Sunita", "Suneetha", "Sunitha", "Soniya", "Sonia", "Sonali", "Sona",
    "Anita", "Anitha", "Anjali", "Anjana", "Anju", "Ananya",
    "Lakshmi", "Laxmi", "Laxmita", "Lekha", "Leela",
    "Kavitha", "Kavita", "Kavitha Rani", "Kavitha Devi",
    "Meena", "Meenakshi", "Mina", "Minal",
    "Priya", "Preethi", "Pritha", "Priti", "Pranjali",
    "Rani", "Renu", "Renuka", "Ritika", "Ritu",

    "Arjun", "Arjith", "Arjit", "Arjunan",
    "Vijay", "Vijaya", "Vijayan",
    "Rahul", "Ragul", "Rahil",
    "Ramesh", "Rajesh", "Raj", "Raja", "Raju",
    "Kiran", "Karthik", "Karthikeyan",
    "Suresh", "Sumanth", "Suhas",
    "Manoj", "Manu", "Manjunath",
    "Naveen", "Navin", "Naveendra",
    "Rohit", "Rohan", "Rohini",
    "Amit", "Amaan", "Amarnath"
]


db = FAISS.from_texts(names, embeddings)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/match_name', methods=['POST'])
def match_name():
    try:
       
        data = request.get_json()
        user_input = data.get("name", "")

        if not user_input:
            return jsonify({"error": "Please provide a name"}), 400

        
        results = db.similarity_search_with_score(user_input, k=5)

       
        response = {
            "input_name": user_input,
            "best_match": {
                "name": results[0][0].page_content,
                "score": round(float(results[0][1]), 4)
            },
            "other_matches": [
                {"name": doc.page_content, "score": round(float(score), 4)}
                for doc, score in results[1:]
            ]
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

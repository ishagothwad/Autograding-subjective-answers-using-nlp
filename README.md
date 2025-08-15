# Auto-Grading Q&A App 📚✏️

This is a Streamlit-based application that evaluates student answers by comparing them to model answers using NLP techniques (NLTK, cosine similarity, etc.).

## 🚀 Features

* Load a dataset of questions and model answers from CSV.
* Display random questions automatically.
* Accept user answers and calculate similarity scores.
* Grade responses instantly.


### 📂 Project Structure

```
.
├── app.py                # Main Streamlit app
├── data/
│   └── sample_answers.csv # Dataset with questions & model answers
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```


### 📦 Installation
 Clone the repo
```
git clone https://github.com/your-username/auto-grading-app.git

cd auto-grading-app

 ```
Create a virtual evnironment
 ```
python -m venv venv

source venv/bin/activate # for windows
source venv/bin/activate # for mac
 ```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Download NLTK resources (run once)

```bash
python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('stopwords')
>>> exit()
```

---

## ▶️ Running the App

```bash
.\venv\Scripts\activate  
streamlit run app.py
```

Then open the URL shown in your terminal (usually `http://localhost:8501`).

---

## 📝 Usage

1. The app will display a **random question** from the dataset.
2. Type your answer in the text area.
3. Click **Submit** to see your score.
4. Click **Next Question** to get another one.

---


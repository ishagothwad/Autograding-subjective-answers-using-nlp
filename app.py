# app.py
import nltk
import streamlit as st
from src.preprocess import preprocess
from src.scoring import compute_score
from src.feedback import generate_feedback


st.title("AutoGrade-NLP — Subjective Answer Grader")

method = st.selectbox("Method", ['bert','tfidf'])
question = st.text_area("Question","What is Photosynthesis?")
model_answer = st.text_area("Model Answer","Photosynthesis is the process....")
student_answer = st.text_area("Student Answer", "")

if st.button("Grade"):
   
    res = compute_score(model_answer, student_answer, method=method)
    st.metric("Score (0-10)", res['final_score'])
    st.write("Details:")
    st.write(f"Semantic similarity: {res['semantic']}")
    st.write(f"Keyword score: {res['keyword_score']} (keywords: {res['keywords']})")
    st.write(f"Grammar score: {res['grammar_score']} (errors: {res['grammar_errors']})")
    st.subheader("Feedback")
    st.write(generate_feedback(res))

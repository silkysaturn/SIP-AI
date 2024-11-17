import streamlit as st
import openai
from openai import OpenAI
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import json

# Firebase Setup
with open("serviceAccountKey.json") as f:
    service_account_info = json.load(f)

cred = credentials.Certificate(service_account_info)
db = firestore.client()

# OpenAI Setup
openai.api_key = st.secrets["openai_api_key"]  # Get OpenAI API key from Streamlit secrets

# Streamlit UI
st.title("SIP AI Smart Interview Prep")

# Dropdown for selecting the job role
job_role = st.selectbox("Select the job role you are preparing for:", ["Software Engineer"])

# Inputs from the user
user_name = st.text_input("Enter your name:")

if st.button("Start Interview"):
    if not user_name or not job_role:
        st.error("Please provide your name and select your job role.")
    else:
        st.subheader(f"Mock Interview for {job_role}")
        
        # Generate response from OpenAI API for Software Engineer role
        try:
            # Ask technical interview questions for a Software Engineer (e.g., LeetCode-style questions)
            prompt = "Please ask a technical interview question for a Software Engineer. The question should be similar to a LeetCode coding question."
            
            # Make the API call to OpenAI's ChatCompletion endpoint
            response = openai.chat.completions.create(
                model="gpt-4",  # Ensure to use the correct model (gpt-4 is often used for chat models)
                messages=[{"role": "system", "content": "You are a helpful assistant."},
                          {"role": "user", "content": prompt}]
            )
            
            # Get the interviewer's question from the response
            interviewer_question = response['choices'][0]['message']['content'].strip()
            st.write("**Interviewer:**", interviewer_question)

            # User Response
            user_response = st.text_area("Your Answer:", placeholder="Type your response here...")

            if st.button("Submit Answer"):
                if user_response:
                    # Save to Firestore
                    interview_data = {
                        "user_name": user_name,
                        "job_role": job_role,
                        "question": interviewer_question,
                        "user_response": user_response,
                        "timestamp": datetime.now(),
                    }
                    db.collection("mock_interviews").add(interview_data)
                    st.success("Your response has been saved successfully!")
                else:
                    st.error("Please type your answer before submitting.")
        except Exception as e:
            st.error(f"Error communicating with OpenAI API: {e}")

# View Interview History
st.subheader("View Your Previous Mock Interviews")
if st.button("Show History"):
    try:
        docs = db.collection("mock_interviews").where("user_name", "==", user_name).stream()
        for doc in docs:
            data = doc.to_dict()
            st.write("**Job Role:**", data["job_role"])
            st.write("**Question:**", data["question"])
            st.write("**Your Response:**", data["user_response"])
            st.write("**Timestamp:**", data["timestamp"])
            st.write("---")
    except Exception as e:
        st.error(f"Error fetching data: {e}")

import google.generativeai as genai
import sqlite3
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load google gemini model and sql query


def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text


# Function to retrieve from sql database

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

# Defining prompt


prompt = [
    """
    You are an expert in converting English qustions to SQL query!
    The SQL database has the name STUDENT and the following columns -NAME,CLASS,SECTION
    and MARKS \n\nFor example, \nExample 1 - How many entries of records are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
    \nExample 2 - Tell me all the students studying in Data Science class?,
    the SQL command will be something like this SELECT * FROM STUDENT where CLASS="Data Science";
    also the sql code should not have ``` in the begining or end and sql word in output
"""
]


# Strealit app

st.set_page_config(page_title="I can Retrieve any SQL Query")
st.header("Gemini App to retrieve SQL Data")
question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")


if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, "student.db")
    st.subheader("The response is ")
    for row in data:
        st.header(row)

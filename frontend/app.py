import streamlit as st
import requests

st.title("Smart Attendance System")

student_name = st.text_input("Enter Student Name")

if st.button("Mark Attendance"):

    response = requests.post(
        "http://127.0.0.1:8000/mark_attendance",
        json={"name": student_name}
    )

    result = response.json()

    st.success(
        f"Student: {result['student']} | Status: {result['status']}"
    )
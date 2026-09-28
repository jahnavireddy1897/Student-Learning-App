import streamlit as st



st.title("🎓 Student Learning App")

topic = st.selectbox(
    "Choose a topic",
    ["Python Basics", "Variables", "Loops", "Functions"]
)

if topic == "Python Basics":
    st.write("Python is a simple and powerful programming language.")

elif topic == "Variables":
    st.write("Variables are used to store data in Python.")

elif topic == "Loops":
    st.write("Loops are used to repeat a block of code.")

elif topic == "Functions":
    st.write("Functions are reusable blocks of code.")

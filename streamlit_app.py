import streamlit as st

goose = open("test.txt","r").readlines()
st.write(f"""

# hello world
{goose[0]}
# """)

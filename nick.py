import streamlit as st
import pandas as pd
 

name = st.text_input("What is your name?")

def main():
    st.title("Welcome " + name)
    st.write("This is gay")


if __name__ == "__main__":
    main()
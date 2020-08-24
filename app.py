import streamlit as st
import page1
import page2
import home

PAGES = {
    'home': home,
    'page1': page1,
    'page2': page2
}

st.sidebar.title("Navigation")
selection = st.sidebar.selectbox('pages', list(PAGES.keys()))

PAGES[selection].write()

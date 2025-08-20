import streamlit as st

#Sidebar
st.sidebar.markdown("Clicked Page 1")
st.sidebar.markdown("Side Menu")
st.sidebar.button("Click")
st.sidebar.radio("성별", ["여자","남자"])

#Page
st.title("Page 1")
st.markdown("Mark Down")
st.header("Header")
st.subheader("sub header")
st.caption("caption")
st.code(""" 
def func():
    print("ok")
def func2():
    print("ok2")
""", language="python")
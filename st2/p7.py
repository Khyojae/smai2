import streamlit as st
#side bar
st.sidebar.markdown("Clicked Page 7")

#page
st.title("Page 7")
picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
import streamlit as st

home = st.Page(page="pages/1.0_Home.py", title="Home", icon=":material/home:")
copilot = st.Page(
    page="pages/2.0_Copilot.py", title="Copilot", icon=":material/assistant:"
)


pages_list = [home, copilot]

nav = st.navigation(pages_list)

nav.run()

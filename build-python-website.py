import streamlit as st


st.set_page_config(
    page_title="My First Website",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="expanded"
)


st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
        }
        .stButton>button {
            background-color: #4CAF50;
            color:white;
        }
        .stTextInput>div>div>input {
            background-color: #e6f7ff;
        }
        .stTextArea>div>textarea {
            background-color: #e6f7ff;
        }
    </style>
""", unsafe_allow_html=True)


st.sidebar.title("🔎 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "ℹ️ About", "📩 Contact"])


theme = st.sidebar.selectbox("Theme", ["Light", "Dark"])

if theme == "Dark":
    st.markdown("""
        <style>
            body {
                background-color: #0e1117;
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)


if page == "🏠 Home":
    st.title("🏠 Home Page")
    st.write("This is the home page built with Python and Streamlit.")
    name = st.text_input("What's your name?", placeholder="Enter your name")

    if name:
        st.balloons()  # 🎈 
        st.success(f"Hello {name}! 🎉 Thank you for visiting.")


elif page == "ℹ️ About":
    st.title("ℹ️ About Page")
    st.info("""
        This website is built entirely using **Python** and **Streamlit**.
        
        🕑 Development time: Under 15 minutes  
        💻 Language: Python 3  
        🎨 UI Library: Streamlit  
        
        Feel free to explore and learn! 🚀
    """)


elif page == "📩 Contact":
    st.title("📩 Contact Us")

    with st.form("contact_form"):
        email = st.text_input("Your Email", placeholder="example@email.com")
        message = st.text_area("Your Message", placeholder="Type your message here...")
        submitted = st.form_submit_button("Submit")

    if submitted:
        if email and message:
            st.snow()  # ❄️ 
            st.success("Thank you! We have received your message. ✅")
        else:
            st.warning("⚠️ Please fill in both fields before submitting.")


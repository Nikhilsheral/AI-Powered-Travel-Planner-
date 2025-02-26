import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage

# 🔑 Directly set Google API Key (Replace with your actual key)
GOOGLE_API_KEY = "your-google-api-key-here"

# 🧠 Initialize Google GenAI Model
chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=GOOGLE_API_KEY)

def get_travel_recommendations(source, destination):
    """Fetch travel options using Google GenAI via LangChain."""
    messages = [
        SystemMessage(content="You are an AI-powered travel planner that provides the best travel options including cab, train, bus, and flights along with estimated costs."),
        HumanMessage(content=f"🚀 Suggest the best travel options from {source} to {destination}, including estimated prices.")
    ]

    try:
        response = chat_model.invoke(messages)
        return response.content if response else "⚠️ No recommendations available."
    except Exception as e:
        return f"❌ Error fetching recommendations: {str(e)}"

# 🌍 Streamlit UI Setup
st.title("🛫 AI-Powered Travel Planner 🌍")
st.markdown("✨ Find the **best** travel options between your source and destination! ✈️🚆🚖🚌")

# 📍 User Input for Travel Planning
source = st.text_input("📍 Enter Source Location:")
destination = st.text_input("🎯 Enter Destination Location:")

if st.button("🔎 Get Travel Options"):
    if source and destination:
        st.write("⏳ Fetching travel recommendations... 🔍")
        recommendations = get_travel_recommendations(source, destination)
        st.write("### ✅ Recommended Travel Options:")
        st.write(recommendations)
    else:
        st.warning("⚠️ Please enter both **source** and **destination**.")

import streamlit as st
from supabase import create_client, Client

# Initialize connection to Supabase
def init_connection():
    url = st.secrets["https://jlvgoobmqiadyskzikiy.supabase.co"]
    key = st.secrets["eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impsdmdvb2JtcWlhZHlza3ppa2l5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDY1MTY1NzUsImV4cCI6MjA2MjA5MjU3NX0.WG1VdaWCb3tsuFqaFadll9TGpODvdTjsxsBS6RYcQQA"]
    return create_client(url, key)

supabase = init_connection()

# Function to fetch Tournaments from Supabase
def fetch_Tournaments():
    return supabase.table("Tournaments").select("*").execute()

# Function to add a new Tournament
def add_project(name):
    supabase.table("Tournaments").insert({"name": name}).execute()

# Streamlit app
st.title("Project Management App")

# Add new project
project_name = st.text_input("Project Name")
if st.button("Add Project"):
    add_project(project_name)
    st.success(f"Project '{project_name}' added!")

# Display Tournaments
st.header("Tournaments")
Tournaments = fetch_Tournaments()
for project in Tournaments.data:
    st.write(f"Project ID: {project['id']}, Name: {project['name']}")

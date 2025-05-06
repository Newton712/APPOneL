
import streamlit as st
from supabase import create_client, Client

# Initialize connection to Supabase
def init_connection():
    url = st.secrets["supabase_url"]
    key = st.secrets["supabase_key"]
    return create_client(url, key)

supabase = init_connection()

# Function to fetch projects from Supabase
def fetch_projects():
    return supabase.table("projects").select("*").execute()

# Function to add a new project
def add_project(name):
    supabase.table("projects").insert({"name": name}).execute()

# Streamlit app
st.title("Project Management App")

# Add new project
project_name = st.text_input("Project Name")
if st.button("Add Project"):
    add_project(project_name)
    st.success(f"Project '{project_name}' added!")

# Display projects
st.header("Projects")
projects = fetch_projects()
for project in projects.data:
    st.write(f"Project ID: {project['id']}, Name: {project['name']}")

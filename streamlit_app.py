import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from datetime import datetime, timedelta

# Define some sample entities 
entities = [ {"name": "Entity 1", "description": "Description of Entity 1"},
            {"name": "Entity 2", "description": "Description of Entity 2"},
            {"name": "Entity 3", "description": "Description of Entity 3"},
            {"name": "Entity 4", "description": "Description of Entity 4"}, ] 

# Function to render the main page with the grid of entities 
def render_main_page(): 
    st.title("Entities Grid") 
    cols = st.columns(2) 
# Adjust the number of columns as needed 
    for i, entity in enumerate(entities): 
        with cols[i % 2]: 
            if st.button(entity["name"]): 
                st.session_state.selected_entity = entity["name"] 
                st.experimental_rerun() 


        
# Function to render the profile details page 
def render_profile_page(entity_name): 
    entity = next(e for e in entities if e["name"] == entity_name) 
    st.title(f"{entity['name']} Profile") 
    st.write(f"Name: {entity['name']}") 
    st.write(f"Description: {entity['description']}") 
    if st.button("Back to Entities Grid"): 
        st.session_state.selected_entity = None 
        st.experimental_rerun() 
        
# Main application logic 
if "selected_entity" not in st.session_state: 
    st.session_state.selected_entity = None 
        
if st.session_state.selected_entity: 
    render_profile_page(st.session_state.selected_entity) 
else: 
    render_main_page()

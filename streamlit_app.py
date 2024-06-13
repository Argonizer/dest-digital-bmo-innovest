import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from datetime import datetime, timedelta
from st_clickable_images import clickable_images

# Define some sample entities 
entities = [ {"name": "Entity 1", "description": "Description of Entity 1", "image":"https://d1csarkz8obe9u.cloudfront.net/posterpreviews/company-logo-design-template-e089327a5c476ce5c70c74f7359c5898_screen.jpg?ts=1672291305"},
            {"name": "Entity 2", "description": "Description of Entity 2", "image":"https://d1csarkz8obe9u.cloudfront.net/posterpreviews/company-logo-design-template-e089327a5c476ce5c70c74f7359c5898_screen.jpg?ts=1672291305"},
            {"name": "Entity 3", "description": "Description of Entity 3", "image":"https://d1csarkz8obe9u.cloudfront.net/posterpreviews/company-logo-design-template-e089327a5c476ce5c70c74f7359c5898_screen.jpg?ts=1672291305"},
            {"name": "Entity 4", "description": "Description of Entity 4", "image":"https://d1csarkz8obe9u.cloudfront.net/posterpreviews/company-logo-design-template-e089327a5c476ce5c70c74f7359c5898_screen.jpg?ts=1672291305"} ]



# Function to render the main page with the grid of entities 
def render_main_page(): 
    st.title("Small Businesses Profiles") 
    clicked = clickable_images(
    [
        "https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=700",
        "https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=700",
        "https://images.unsplash.com/photo-1582550945154-66ea8fff25e1?w=700",
        "https://images.unsplash.com/photo-1591797442444-039f23ddcc14?w=700",
        "https://images.unsplash.com/photo-1518727818782-ed5341dbd476?w=700",
    ],
    titles=[f"Image #{str(i)}" for i in range(5)],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "200px"},
    )
    st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")
    cols = st.columns(2) 
            
# Adjust the number of columns as needed 
    for i, entity in enumerate(entities): 
        with cols[i % 2]: 
            st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")
            if st.image(entity["image"], "Alt"): 
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

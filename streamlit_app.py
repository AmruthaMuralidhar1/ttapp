import streamlit as st

# Define historical places
historical_places = {
    "Central Park": {
        "description": "A large public park in New York City.",
        "location": "New York, USA"
    },
    "Eiffel Tower": {
        "description": "A wrought-iron lattice tower in Paris, France.",
        "location": "Paris, France"
    },
    "Great Wall of China": {
        "description": "A series of fortifications made of stone, brick, tamped earth, wood, and other materials.",
        "location": "China"
    },
    "Taj Mahal": {
        "description": "An ivory-white marble mausoleum on the south bank of the Yamuna river in the Indian city of Agra.",
        "location": "Agra, India"
    },
    "Sydney Opera House": {
        "description": "A multi-venue performing arts centre in Sydney, Australia.",
        "location": "Sydney, Australia"
    }
}

# Streamlit UI components
st.title("Time Traveler's Guide 🎈")

# Add a sidebar for navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("Use this app to explore historical places around the world.")

# User input for location
location = st.text_input("Enter the location you want to explore:")

if st.button("Explore"):
    if location in historical_places:
        
        # Fetch historical data from the dictionary
        historical_data = historical_places[location]
        
        # Display historical information using Streamlit
        st.subheader(f"Exploring the history of {location}...")
        st.write(f"**Name:** {location}")
        st.write(f"**Description:** {historical_data['description']}")
        st.write(f"**Location:** {historical_data['location']}")
    else:
        st.write("Sorry, no historical data available for this location.")

if st.button("About Us"):
    st.write("This app is designed to help you explore the history of various historical places around the world.")

if st.button("Help"):
    st.write("If you need assistance or have any questions, please feel free to contact us.")

# Adding a footer
st.sidebar.markdown("---")
st.sidebar.write("Developed by Amrutha Muralidhar")
st.sidebar.write("Find more about this project on [GitHub](https://github.com/AmruthaMuralidhar1/ttapp)")

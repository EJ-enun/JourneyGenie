import streamlit as st
from transformers import pipeline

# Initialize the HuggingFace model
model = pipeline('text-generation', model='your-huggingface-model')

def generate_itinerary(location, destination, interests):
    # Generate the itinerary using the HuggingFace model
    input_text = f"Location: {location}, Destination: {destination}, Interests: {interests}"
    generated_text = model(input_text)[0]['generated_text']
    return generated_text

def main():
    st.title("Travel Itinerary Generator")

    # Get the inputs from the user
    location = st.text_input("Enter your location")
    destination = st.text_input("Enter your destination")
    interests = st.text_input("Enter your interests")

    if st.button("Generate Itinerary"):
        if location and destination and interests:
            # Generate the itinerary
            itinerary = generate_itinerary(location, destination, interests)
            st.write(itinerary)
        else:
            st.write("Please enter all the details")

if __name__ == "__main__":
    main()

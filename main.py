import streamlit as st
from transformers import pipeline

# Initialize the HuggingFace model
model = pipeline('text-generation', model='your-huggingface-model')

def generate_itinerary(location, destination, interests):
    # Generate the itinerary using the HuggingFace model
    input_text = f"Location: {location}, Destination: {destination}, Interests: {interests}"
    generated_text = model(input_text)[0]['generated_text']
    return generated_text
    
# Function to set background color
def set_background_color(color):
    background_color = f'''
    <style>
    .stApp {{
        background-color: {color};
    }}
    </style>
    '''
    st.markdown(background_color, unsafe_allow_html=True)


def add_image():
    col_spacer, col_copy, col_push = st.columns([0.5, 0.3, 0.2])
        with col_copy:
            copy_to_clipboard = st.image(image, caption="Uploaded Image") #, use_column_width=True

def main():
    set_background_color('#40E0D0')
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

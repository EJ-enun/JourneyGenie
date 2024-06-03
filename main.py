import streamlit as st
from transformers import pipeline
from google.cloud import vertexai as vertexai
from vertexai.generative_models import GenerativeModel, ChatSession

# Replace with your project ID and location
PROJECT_ID = "your-project-id"
LOCATION = "your-location"


# Initialize the HuggingFace model
model = pipeline('text-generation', model='your-huggingface-model')

def generate_itinerary(location, destination, interests):
    #Import vertex ai
    vertexai.init(project=project_id, location="us-central1")
    
    #Instantiate Model
    model = GenerativeModel(model_name="gemini-1.0-pro-002")
    
    #Start Chatting with the model
    chat = model.start_chat()
    
    # Generate the itinerary using the HuggingFace model
    #input_text = f"Location: {location}, Destination: {destination}, Interests: {interests}"
    #generated_text = model(input_text)[0]['generated_text']

    prompt = "Hello."
    generated_text = get_chat_response(chat, prompt)
    return generated_text


#Function to get chat response
def get_chat_response(chat: ChatSession, prompt: str) -> str:
    response = chat.send_message(prompt)
    return response.text

    
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

#Function to add Image
#def add_image():
#    image = ""
#    col_spacer, col_copy, col_push = st.columns([0.5, 0.3, 0.2])
#        with col_copy:
#            image = st.image(image, caption="Uploaded Image") #, use_column_width=True
#            return image

def main():
    set_background_color('#40E0D0')
    st.title("Visa Voyager")

    

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

import streamlit as st
from transformers import pipeline
from google.cloud import aiplatform 
import vertexai
from vertexai.generative_models import GenerativeModel, ChatSession
import pyperclip
# Replace with your project ID and location
PROJECT_ID = "your-project-id"
LOCATION = "your-location"

def copy(text):
    col_spacer, col_copy, col_push = st.columns([0.5, 0.3, 0.2])
    with col_copy:
            copy_to_clipboard = st.button(label="Copy to clipboard :clipboard:")
            if copy_to_clipboard:
                try:
                    pyperclip.copy(text)
                except pyperclip.PyperclipException:
                    st.warning("Error: Copying currently not working")

  

# Initialize the HuggingFace model
#model = pipeline('text-generation', model='your-huggingface-model')

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

def page_logo():
    # Streamlit page configuration is set
    st.set_page_config(
        page_title="VisaVoyager",
        page_icon= "https://raw.githubusercontent.com/EJ-enun/journeygenie/main/logo.png",)

    
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

# Function to set logo
def set_logo():
    image = "https://raw.githubusercontent.com/EJ-enun/visavoyager/main/logo.png"
    col1, col2, col3 = st.columns([1,4,1])
    with col2:
        return st.image(image, caption = 'Navigate the visa application process and chart your travel journey with ease.')


#def show_loading_gif():
    # URL of the GIF in the GitHub repo
    #gif_url = 'https://github.com/EJ-enun/visavoyager/main/loading.gif'

    # Send a GET request to the GitHub server to fetch the GIF
    #response = requests.get(gif_url)

    # Read the content of the response
    #gif_data = response.content

    # Encode the GIF data in base64
    #encoded_gif = base64.b64encode(gif_data).decode('utf-8-sig')

    # Display the GIF in the Streamlit app
    #st.markdown(f'<img src="data:image/gif;base64,{encoded_gif}" alt="gif">', unsafe_allow_html=True)

def app():
    # Get the inputs from the user
    location = st.text_input("Which city are you applying from:")
    destination = st.text_input("Which city/cities are you going to:")
    dates = st.text_input("How many days will you be staying:")
    interests = st.text_input("What would you like to see and do:")

    if st.button("Create Itinerary"):
        if location and destination and dates and interests:
            days = int(dates)
            # Generate the itinerary
            #show_loading_gif()
            st.write(f"Country of Interest: {destination.capitalize()}")
            st.write(f"Country of Applicant: {location.capitalize()}")
            st.title(f"List of all {destination.capitalize()} Embassies within {location.capitalize()}")
            st.title(f"Travel Itinerary for my Journey to {destination.capitalize()}")
            #itinerary = generate_itinerary(location, destination, interests)
            #st.write(itinerary)
            st.title(f"About Visa applications for {destination.capitalize()}")
            text = st.text_input(f"Do you have any other questions about visa applications to {destination.capitalize()} ?")
            copy(text)
            st.write("This is what we live for.")
        else:
            #show_loading_gif()
            st.write("Please enter all the details")


def main():
    page_logo()
    set_background_color('#008080')
    st.title("Visa Voyager")
    set_logo()
    app()

    

    

if __name__ == "__main__":
    main()

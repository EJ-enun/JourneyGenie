import streamlit as st
from transformers import pipeline
from google.cloud import aiplatform 
import vertexai
from vertexai.generative_models import GenerativeModel, ChatSession

# Replace with your project ID and location
PROJECT_ID = "your-project-id"
LOCATION = "your-location"


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
    image = "https://raw.githubusercontent.com/EJ-enun/journeygenie/main/logo.png"
    col1, col2, col3 = st.columns([1,4,1])
    with col2:
        return st.image(image, caption = 'Navigate the visa application process and chart your travel journey with ease.')


def show_loading_gif():
    # URL of the GIF in the GitHub repo
    gif_url = 'https://github.com/EJ-enun/journeygenie/blob/main/loading.gif?raw=true'

    # Send a GET request to the GitHub server to fetch the GIF
    response = requests.get(gif_url)

    # Read the content of the response
    gif_data = response.content

    # Encode the GIF data in base64
    encoded_gif = base64.b64encode(gif_data).decode('utf-8-sig')

    # Display the GIF in the Streamlit app
    st.markdown(f'<img src="data:image/gif;base64,{encoded_gif}" alt="gif">', unsafe_allow_html=True)



def main():
    page_logo()
    set_background_color('#008080')
    st.title("Visa Voyager")
    set_logo()

    

    # Get the inputs from the user
    location = st.text_input("Enter your location")
    destination = st.text_input("Enter your destination")
    interests = st.text_input("Enter your interests")

    if st.button("Generate Itinerary"):
        if location and destination and interests:
            # Generate the itinerary
            show_loading_gif()
            #itinerary = generate_itinerary(location, destination, interests)
            #st.write(itinerary)
        else:
            show_loading_gif()
            st.write("Please enter all the details")

if __name__ == "__main__":
    main()

import streamlit as st
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import os
from dotenv import load_dotenv 

# loading variables from .env file
load_dotenv() 

# accessing vision key and endpoint
subscription_key = os.getenv("VISION_KEY")
endpoint = os.getenv("VISION_ENDPOINT")

# this is the main function in which we define our webpage  




def main():
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
    st.markdown("#  Showdown 🖼️")
    st.markdown("### Nems et frites à volonté sauce Dallas.")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOljNTwuxcG42R8OSb1p9Dq68eJmdW3bHBRw&s", caption="Pasteis de nata")
# Define the image to analyse
    remote_image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOljNTwuxcG42R8OSb1p9Dq68eJmdW3bHBRw&s"

# Call AI Vision API to analyse a remote image
    tags_result_remote = computervision_client.tag_image(remote_image_url)

# Show results with confidence score
    st.markdown("Tags in the remote image: ")
    if (len(tags_result_remote.tags) == 0):
        st.text("No tags detected.")
    else:
        for tag in tags_result_remote.tags:
            st.text("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))

# Init code
if __name__=='__main__': 
    main()


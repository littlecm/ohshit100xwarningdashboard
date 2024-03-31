import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="Embedded Retool App", layout="wide")

def main():
    # Title for your app
    st.title("Embedded Retool App")

    # Define the URL to be embedded
    url = "https://miai.retool.com/p/os100warnings"

    # Create an iframe with the specified URL, width, and height
    components.iframe(url, width=1000, height=800, scrolling=True)

if __name__ == "__main__":
    main()

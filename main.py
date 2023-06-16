# This is a sample Python script.
import nltk as nltk


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Load nltk chatbot corpus
nltk.download('nps_chat')

# Define global chatbot variable
chatbot_pairs = []


# Load chatbot algorithm
def load_chatbot():
    global chatbot_pairs
    chat_corpus = nltk.corpus.nps_chat.posts()
    pairs = []
    for post in chat_corpus:
        for i in range(len(post) - 1):
            pairs.append((post[i], post[i + 1]))
    chatbot_pairs = pairs


# Define speech recognition function
def transcribe_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Transcribing...")
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Error: {str(e)}")


# Define chatbot function
def chatbot_response(input_text):
    global chatbot_pairs
    if input_text.startswith('/speech'):
        input_text = transcribe_speech()
        if not input_text:
            return "Sorry, I couldn't transcribe your speech. Please try again."

    for pair in chatbot_pairs:
        pattern, response = pair
        if pattern in input_text:
            return response

    return "I'm sorry, I don't have a response for that."


# Create Streamlit app
def main():
    st.title("Chatbot App")

    # Load chatbot
    load_chatbot()

    # Get user input
    user_input = st.text_input("User Input:")

    # Get user input type
    input_type = st.radio("Input Type:", ('Text', 'Speech'))

    if st.button("Submit"):
        if input_type == 'Speech':
            response = chatbot_response('/speech')
        else:
            response = chatbot_response(user_input)

        st.text_area("Chatbot Response:", value=response, height=200)


if __name__ == "__main__":
    import nltk
    import streamlit as st
    import speech_recognition as sr
    main()

# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

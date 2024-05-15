
import os
from groq import Groq
import streamlit as st

client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)
def predict(input_phrase):
    completion = client.chat.completions.create(
         model="llama3-70b-8192",
        messages=[
            {
                "role": "user",
                "content": "Reformulate this phrase:" + input_phrase
            },
            {
                "role": "assistant",
                "content": "Here's a reformulated version:"
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    
    return completion



def main():
    st.title('LLAMA Test')
    st.write('Enter the phrase to reformulate:')
    phrase = st.text_input("Phrase")
    if st.button("Reformulate"):
        completion = predict(phrase)
        
        st.write(completion.choices[0].message.content)

if __name__ == '__main__':

    main()
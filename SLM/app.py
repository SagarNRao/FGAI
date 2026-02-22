import streamlit as st
# Paste all code from above (imports → tools → llm → prompt → agent_executor)
# ...

st.title('Free Trip Planning Agent')
st.caption('Uses Groq Llama 3, OpenWeather, Geoapify (free tiers)')

prompt = st.text_input('Your trip request', 'Plan a 3-day trip to Tokyo in May')

if st.button('Plan My Trip') and prompt:
    with st.spinner('Planning your adventure...'):
        try:
            result = agent_executor.invoke({'input': prompt})
            st.markdown(result['output'])
        except Exception as e:
            st.error(f'Something went wrong: {str(e)}')

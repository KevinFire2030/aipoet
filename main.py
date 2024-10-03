

import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
# from langchain_openai import OpenAI, ChatOpenAI
# from langchain_community.llms import OpenAI
#from langchain_community.chat_models import ChatOpenAI

from langchain_openai import ChatOpenAI

# 환경 변수에서 API 키 가져오기
#api_key = os.getenv("OPENAI_API_KEY")



# ChatOpenAI 테스트
#chat_model = ChatOpenAI(api_key=api_key)
chat_model = ChatOpenAI()

st.title("인공지능 시인")

content = st.text_input("시의 주재를 재시해주세요")

if st.button("시 작성 요청하기"):

    with st.spinner('시 작성 중...'):
        result = chat_model.invoke(content + "에 대한 시를 써줘")
        st.write(result.content)


    













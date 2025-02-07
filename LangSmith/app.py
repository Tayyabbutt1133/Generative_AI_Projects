# Using openai model through langchain 
from langchain_openai import ChatOpenAI
# usin template for interaction chats
from langchain_core.prompts import ChatPromptTemplate
# using output parser to parse output in a formatted way
from langchain_core.output_parsers import StrOutputParser


import os
from dotenv import load_dotenv

load_dotenv()

# loading key's from .env
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please Respond to the user based on the given context"),
        ("user", "Question:{question}\nContext:{context}")
    ]
)

model = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

# Creating a chain of actions that we need to 
chain = prompt | model | output_parser

question= "Can you summarize this speech ?"

context= """Ladies and Gentlemen, I cordially thank you, with the utmost sincerity, for the honour you have conferred upon me — the greatest honour that it is possible for this Sovereign Assembly to confer — by electing me as your first President. I also thank those leaders who have spoken in appreciation of my services and their personal references to me. I sincerely hope that with your support and your co-operation we shall make this Constituent Assembly an example to the world. The Constituent Assembly has got two main functions to perform. The first is the very onerous and responsible task of framing our future constitution of Pakistan and the second of functioning as a full and complete Sovereign body as the Federal Legislature of Pakistan. We have to do the best we can in adopting a provisional constitution for the Federal Legislature of Pakistan. You know really that not only we ourselves are wondering but, I think, the whole world is wondering at this unprecedented cyclonic revolution which has brought about the plan of creating and establishing two independent Sovereign Dominions in this sub-continent. As it is, it has been unprecedented; there is no parallel in the history of the world. This mighty sub-continent with all kinds of inhabitants has been brought under a plan which is titanic, unknown, unparalleled. And what is very important with regards to it is that we have achieved it peacefully and by means of a revolution of the greatest possible character.

Dealing with our first function in this Assembly, I cannot make any well-considered pronouncement at this moment, but I shall say a few things as they occur to me. The first and the foremost thing that I would like to emphasise is this — remember that you are now a Sovereign legislative body and you have got all the powers. It, therefore, places on you the gravest responsibility as to how you should take your decisions. The first observation that I would like to make is this. You will no doubt agree with me that the first duty of a Government is to maintain law and order, so that the life, property and religious beliefs of its subjects are fully protected by the State."""

print(chain.invoke({"question": question, "context": context}))
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage, SystemMessage
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.document_loaders import PyPDFDirectoryLoader, DirectoryLoader, TextLoader

#load api key
load_dotenv()


llm = ChatGoogleGenerativeAI(model='gemini-3.5-flash')

# load documents
directory = Path("/home/matthew/Documents/my-notes/recipes")

text_loader = DirectoryLoader(directory, glob="**/*.md", loader_cls=TextLoader)
text_docs = text_loader.load()

docs = text_docs

# create embeddings and vector store
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = InMemoryVectorStore(embeddings)
vector_store.add_documents(docs)









user_query = input("Enter query: ")
retrieved_docs = vector_store.similarity_search(user_query, k=2)
context = "\n".join(doc.page_content for doc in retrieved_docs)

system_prompt = f"""
You are a helpful assistant that answers questions about these documents: {context}
"""
# set up message for llm
messages = [
    SystemMessage(content=system_prompt),
    HumanMessage(content=user_query)
]

response = llm.invoke(messages)

print(response.content)

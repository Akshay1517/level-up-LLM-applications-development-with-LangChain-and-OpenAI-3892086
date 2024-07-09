from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(model="gpt-4-turbo-preview")
ATLAS_CONNECTION_STRING = os.getenv("ATLAS_CONNECTION_STRING")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
ATLAS_VECTOR_SEARCH_INDEX_NAME = os.getenv("ATLAS_VECTOR_SEARCH_INDEX_NAME")

# Connect to your Atlas cluster
client = MongoClient(ATLAS_CONNECTION_STRING)

# Define collection and index name
collection = client[DB_NAME][COLLECTION_NAME]

if client:
    print("Connected to MongoDB Atlas")
    print(client.list_database_names())

# Load the sample data (PDF document)
loader = PyPDFLoader("https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4HkJP")
data = loader.load()

# Split PDF into smaller documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
docs = text_splitter.split_documents(data)

# Print the first document
print(docs[0])

# Instantiate the vector store
vector_store = MongoDBAtlasVectorSearch.from_documents(
    documents=docs,
    embedding=OpenAIEmbeddings(disallowed_special=()),
    collection=collection,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME
)



# Instantiate Atlas Vector Search as a retriever


# Define a prompt template
 

# Construct a chain to answer questions on your data


# Prompt the chain to answer a question


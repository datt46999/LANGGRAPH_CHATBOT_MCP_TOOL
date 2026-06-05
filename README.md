# LANGGRAPH_CHATBOT_MCP_TOOL


 Implement  AI chatbot platform built with FastAPI and LangGraph, featuring multi-agent orchestration, multi-tenant vector storage, cross-chat memory, and voice call capabilities through LiveKit integration.


## Feature

###  Wrokflow Orchestration with LangGraph
- **Multi-Agent System**: Specialized agents working together to solve complex tasks
  - **Supervisor Agent**: Coordinates workflow and delegates tasks to specialized agents
  - **Research Agent**: Retrieves information from the web and knowledge bases
  - **Scraper Agent**: Extracts and summarizes content from web pages
- **Complex Workflows**: Handle multistep reasoning and task decomposition
- **State Management**: Maintain conversation context across multiple turns


### Voice Assistant via LiveKit

- **Real-Time Voice Communication**: Natural voice interaction using LiveKit's WebRTC platform
- **High-Quality Speech Recognition**: Accurate transcription with Deepgram's advanced STT
- **Natural Text-to-Speech**: Lifelike voice responses with Cartesia TTS
- **Voice Activity Detection**: Intelligent turn-taking with Silero VAD
- **Multilingual Support**: Voice interaction in multiple languages

### MCP Tools Integration

- **Firecrawl**: Advanced web scraping and content extraction
  - Extract structured data from websites
  - Summarize long-form content
  - Process tables and lists
- **Tavily**: Intelligent web search capabilities
  - Semantic search across the web
  - Real-time information retrieval
  - Source attribution and citation


### Vector Storage with Qdrant

- **Multi-Tenant Vector Store**: Efficiently store and retrieve conversation history with tenant isolation
- **Semantic Search**: Find relevant past conversations using semantic similarity
- **Payload Filtering**: Efficient filtering by tenant_id for data security and performance
- **Metadata Storage**: Store and retrieve additional context alongside vector embeddings


### Persistent Memory with Mem0

- **Cross-Chat Memory**: Remember important information across different conversations
- **Long-Term Context**: Maintain context over extended interactions
- **Selective Memory**: Intelligently decide what information to remember
- **Memory Retrieval**: Retrieve relevant memories based on conversation context



### Backend Architecture

- **FastAPI Framework**: High-performance asynchronous API framework with automatic OpenAPI documentation
- **SQLAlchemy ORM**: Async database operations with SQLite (configurable for PostgreSQL/MySQL)
- **Pydantic Models**: Type-safe data validation and serialization
- **JWT Authentication**: Secure token-based authentication with OAuth2 password flow




##  Installation




1. Clone the repository

```bash
git clone <repository-url>
cd ruban_fastapi-langgraph-chatbot
```

2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Python dependencies

```bash
pip install -r requirements.txt
```

4. Set up environment variables

Create a `.env` file in the root directory with the following variables:

```env
# FastAPI settings
SECRET_KEY=YOUR_SECRET_KEY
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Database settings
SQLALCHEMY_DATABASE_URI=sqlite:///./app.db

# OpenAI settings

OPENAI_API_KEY=YOUR_OPENAI_API_KEY
# Qdrant settings
QDRANT_HOST=localhost
QDRANT_PORT=6333


TAVILY_API_KEY=YOUR_TAVILY_API_KEY

FIRECRAWL_API_KEY=YOUR_FIRECRAWL_API_KEY


# LiveKit settings
LIVEKIT_URL=YOUR_LIVEKIT_URL
LIVEKIT_API_KEY=YOUR_LIVEKIT_API_KEY
LIVEKIT_API_SECRET=YOUR_LIVEKIT_API_SECRET

# LangSmith (optional, for tracing)
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://eu.api.smith.langchain.com
LANGSMITH_API_KEY=YOUR_LANGSMITH_API_KEY
LANGSMITH_PROJECT=YOUR_LANGSMITH_PROJECT


```


## Running the Application

### Starting the Backend Services

1. Start the MCP servers (in separate terminals)

```bash
# Terminal 1: 
python -m app.mcp_server.search_server

# Terminal 2: 
python -m app.mcp_server.web_scrapping_server
```

2. Start the main FastAPI server

```bash
# Terminal 3: 
python app.py
```


3. Start with Backend:


Backend API documentation: http://localhost:8000/docs

### Demo:
[▶ Watch Demo](DEMO/DEMO_RESULT.webm)
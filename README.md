# 🦜🔗 Gen AI with LangChain

A hands-on learning repository covering core **LangChain** concepts — from basic LLM invocations to building full RAG pipelines. Each folder maps to a topic from the playlist and contains standalone, runnable Python scripts.

---

## 📂 Repository Structure

```
├── LLMs/                    # Legacy LLM interface (completion-style)
├── ChatModels/              # Chat model integrations (OpenAI, HuggingFace, Local)
├── Prompts/                 # Prompt templates, chat prompts & a simple chatbot
├── Chains/                  # LCEL chains — simple, sequential, parallel, conditional
├── Structured_Output/       # Structured output with Pydantic, TypedDict & output parsers
├── RAG/                     # Retrieval-Augmented Generation
│   ├── Document_Loaders/    #   Text, CSV, PDF & web loaders
│   ├── Text_Splitters/      #   Length-based, structured & code splitters
│   └── Vector_Stores/       #   Vector store concepts
└── requirements.txt
```

---

## 🧩 Module Breakdown

### 1. LLMs
| File | Description |
|------|-------------|
| `llm_demo.py` | Basic completion using `OpenAI` (GPT-3.5 Turbo Instruct) |

### 2. ChatModels
| File | Description |
|------|-------------|
| `chat_model_01.py` | Chat completion with `ChatOpenAI` (GPT-4) |
| `chat_model_hf.py` | Using HuggingFace Inference Endpoints (Qwen3-8B) |
| `chat_model_local.py` | Running a model locally via `HuggingFacePipeline` (TinyLlama) |

### 3. Prompts
| File | Description |
|------|-------------|
| `messages.py` | Working with `SystemMessage`, `HumanMessage`, `AIMessage` |
| `Chatprompt.py` | Using `ChatPromptTemplate` for structured prompts |
| `Chatbot.py` | Simple interactive chatbot with conversation history |

### 4. Chains (LCEL)
| File | Description |
|------|-------------|
| `simple_chain.py` | Basic `prompt \| model \| parser` chain |
| `sequential_chain.py` | Multi-step chain — generate report → summarize |
| `parallel_chain.py` | `RunnableParallel` — notes & quiz generated simultaneously, then merged |
| `conditional_chain.py` | `RunnableBranch` — sentiment-based routing with Pydantic classification |

### 5. Structured Output
| File | Description |
|------|-------------|
| `pydantic_demo.py` | Pydantic model basics |
| `json_schema_demo.py` | JSON schema-based structured output |
| `typedict.py` | TypedDict-based structured output |
| `with_structured_output_pydantic.py` | `model.with_structured_output()` using Pydantic |
| `with_structured_output_typedict.py` | `model.with_structured_output()` using TypedDict |
| `pydantic_output_parser.py` | `PydanticOutputParser` for structured parsing |
| **Output_Parsers/** | |
| `str_output_parser.py` | `StrOutputParser` usage |
| `json_output_parser.py` | `JsonOutputParser` usage |

### 6. RAG (Retrieval-Augmented Generation)

#### Document Loaders
| File | Description |
|------|-------------|
| `text_loader.py` | Loading `.txt` files with `TextLoader` (including `load` vs `lazy_load`) |
| `csvloader.py` | Loading CSV data with `CSVLoader` |
| `pypdf_loader.py` | Loading PDF files with `PyPDFLoader` |
| `webbaseloader.py` | Scraping web pages with `WebBaseLoader` |
| `directory_loader.py` | Batch loading from a directory with `DirectoryLoader` |

#### Text Splitters
| File | Description |
|------|-------------|
| `length_based.py` | `CharacterTextSplitter` with fixed chunk size |
| `text_structured_based.py` | `RecursiveCharacterTextSplitter` — structure-aware splitting |
| `python_code.py` | Splitting Python source code while preserving syntax |

#### Vector Stores
| File | Description |
|------|-------------|
| `image.png` | Conceptual diagram of vector store architecture |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- API keys for the providers you want to use (OpenAI, HuggingFace, etc.)

### Installation

```bash
# Clone the repository
git clone https://github.com/MuneebRbutt/Gen-AI-with-Langchain.git
cd Gen-AI-with-Langchain

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root (or in each module folder) with the required API keys:

```env
OPENAI_API_KEY=your_openai_api_key
HUGGINGFACEHUB_API_TOKEN=your_hf_token
```

### Running a Script

```bash
python Chains/simple_chain.py
```

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| **Framework** | LangChain, LangChain Core |
| **LLM Providers** | OpenAI, HuggingFace, Google Gemini, Anthropic |
| **Validation** | Pydantic |
| **Utilities** | python-dotenv, NumPy, scikit-learn |

---

## 📝 License

This project is for educational and personal learning purposes.

from smolagents import CodeAgent, LiteLLMModel
from smolagents import ToolCallingAgent


model = LiteLLMModel( 
    # "ollama_chat/MFDoom/deepseek-r1-tool-calling:1.5b"
    model_id="ollama_chat/qwen2.5:3b",
    api_base="http://127.0.0.1:11434",
    api_key="YOUR_API_KEY", # replace with API key if necessary
    num_ctx=8192 # ollama default is 2048 which will fail horribly. 8192 works for easy tasks, more is better. Check https://huggingface.co/spaces/NyxKrage/LLM-Model-VRAM-Calculator to calculate how much VRAM this will need for the selected model.
)
agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run(
   # "Could you give me the 118th number in the Fibonacci sequence?",
   "Could you give me the 118th number in the Fibonacci sequence?"
)
import gradio as gr
from llama_cpp import Llama
from huggingface_hub import hf_hub_download

# Modeli indir
model_path = hf_hub_download(
    repo_id="erdemyavuz/llama-3-8b-chat-doctor", 
    filename="llama-3-8b-chat-doctor-Q4_K_M.gguf"
)

# CPU optimizasyonlu yükleme
llm = Llama(
    model_path=model_path, 
    n_ctx=512,      # RAM dostu olması için context'i kısa tutuyoruz
    n_threads=2,    # Free tier 2 CPU çekirdeği verir
    n_gpu_layers=0  # Sadece CPU
)

def respond(message, history):
    prompt = f"Patient: {message}\nDoctor:"
    output = llm(prompt, max_tokens=256, stop=["Patient:"], echo=False)
    return output["choices"][0]["text"]

demo = gr.ChatInterface(respond, title="Llama-3 Medikal Chatbot (Docker/CPU) 🩺")

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
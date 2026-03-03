
# 🩺 Llama-3 Medical Chatbot

This project is an optimized web application of the **Llama-3-8B** model, which has been fine-tuned on a dataset containing over 250,000 patient-doctor dialogues. 

The model has been converted to the **GGUF** format (Q4_K_M) to minimize memory usage and run with high performance on standard CPUs. The application is packaged with Docker to provide a completely isolated and portable environment, and deployed with Gradio to offer a user-friendly chat interface.

## 🚀 Live Demo

You can try the application live on Hugging Face Spaces:
**[👉 Click Here for Live Demo](https://huggingface.co/spaces/erdemyavuz/doctor_chatbot)**

## 🚀 Features

* **Custom Fine-Tuned Model:** Optimized responses for medical conversations and patient questions.
* **Low Resource Consumption:** Fluent inference capability even on standard hardware (CPU only) thanks to GGUF quantization.
* **Container Architecture:** Guaranteed instant and seamless operation in any environment thanks to Docker.
* **Modern Interface:** A clean and fast chat interface developed with Gradio.

## 🛠️ Technologies Used

* **LLM & Inference:** Meta Llama-3-8B, `llama-cpp-python`
* **Interface:** Gradio
* **Infrastructure & Deployment:** Docker, Hugging Face Spaces
* **Language:** Python 3.10

## 🏃‍♂️ Running Locally (with Docker)

To get the project up and running on your own computer in seconds, simply run the following commands in your terminal:

```bash
# Clone the repository
git clone https://github.com/ErdemYavuz55/llama3-medical-chatbot.git
cd llama3-medical-chatbot

# Build the Docker image
docker build -t medical-chatbot .

# Run the container
docker run -p 7860:7860 medical-chatbot

```

*Then, you can go to `http://localhost:7860` in your browser and start chatting with the assistant right away.*

## ⚠️ Disclaimer

*This is an AI model and is strictly for educational/research purposes only. The answers it provides do not in any way substitute for professional medical advice, diagnosis, or treatment.*

---

**Developer:** Erdem Yavuz Hacısoftaoğlu

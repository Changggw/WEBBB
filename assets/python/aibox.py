import gradio as gr

def reply(message):
    return "Bạn hỏi: " + message + " — đây là câu trả lời mẫu."

gr.ChatInterface(reply, title="Măm Măm Bot").launch()

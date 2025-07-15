import gradio as gr

def reply(msg): return "Bạn hỏi: " + msg
demo = gr.ChatInterface(fn=reply, title="Măm Măm Bot")

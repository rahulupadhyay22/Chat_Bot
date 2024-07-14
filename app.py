# -*- coding: utf-8 -*-

import google.generativeai as palm
import gradio as gr

palm.configure(api_key='AIzaSyDuGhG5xtJC3L9DjfNBO-uALid2UhLD93E')

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

def get_text_response(user_message,history):
  completion = palm.generate_text(
    model=model,
    prompt=user_message,
    temperature=0.25,  # temperature=0 >> more deterministic results // temperature=1 >> more randomness
    max_output_tokens=100    # maximum length of response

)
  return completion.result

demo = gr.ChatInterface(get_text_response, examples=["How are you doing?","What are your interests?","Which places do you like to visit?"])

if __name__ == "__main__":
  demo.launch()
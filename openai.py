import openai
import tkinter as tk

# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Define function to get OpenAI response
def get_openai_response():
    # Get question from user
    question = question_entry.get()

    # Call OpenAI API to fetch response
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=question,
        max_tokens=100,
        temperature=0.5,
    )

    # Get response text from API response
    response_text = response.choices[0].text

    # Update answer label with response text
    answer_label.config(text=response_text)

# Set up GUI
root = tk.Tk()
root.title("OpenAI Question Answering")

# Add question entry field
question_entry = tk.Entry(root, width=50)
question_entry.pack()

# Add button to get OpenAI response
get_answer_button = tk.Button(root, text="Get Answer", command=get_openai_response)
get_answer_button.pack()

# Add label to display answer
answer_label = tk.Label(root, text="")
answer_label.pack()

# Start GUI main loop
root.mainloop()

#!/bin/bash

# Get OpenAI API key from environment variable
API_KEY="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"

# Ask user for a question
question=$(zenity --entry --title="Ask a Question" --text="What do you want to know?")

# Call OpenAI API to fetch response
response=$(curl -X POST https://api.openai.com/v1/engines/davinci-codex/completions \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer $API_KEY" \
     -d '{
           "prompt": "'"$question"'",
           "max_tokens": 100,
           "temperature": 0.5
         }' | jq -r '.choices[].text')

# Display response in a GUI window
zenity --info --title="Answer" --text="$response"


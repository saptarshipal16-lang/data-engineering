from openai import OpenAI
import pandas as pd
import os

# 1. Set API key (better way)
# In PowerShell first:
# setx OPENAI_API_KEY "your_real_api_key"

client = OpenAI()

# 2. Load data
df = pd.read_excel("clean.xlsx")

# 3. Convert data to text for context
schema = df.to_string(index=False)

# 4. User question
#question = "What is the class of senthil?"

question= input("Ask your question: ")

# 5. Prompt
prompt = f"""
You are a data assistant.
Answer ONLY using the table below.

Table:
{schema}

Question:
{question}

Answer with just the value.
"""

# 6. Correct API call (NEW)
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

# 7. Print result
print(response.output_text)

from openai import OpenAI
import os

llm_api_key = os.environ.get("LITELLM_API_KEY")
llm_api_base = "https://llmproxy.ai.orange"

def call_llm(prompt):    
    client = OpenAI(
        api_key=llm_api_key,
        base_url=llm_api_base
    )
    response = client.chat.completions.create(
        model="openai/gpt-4o-mini", # model to send to the proxy
        messages = [
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content

def call_repomix(prompt):    
    os.system('node ./node_modules/repomix/bin/repomix.cjs ' + '.')

def read_file(path):    
    f=open(path)
    s=f.read()
    f.close()
    return s

if __name__ == "__main__":
    print("## Testing call_llm")
    prompt = "In a few words, what is the meaning of life?"
    print(f"## Prompt: {prompt}")
    response = call_llm(prompt)
    print(f"## Response: {response}")

    print("## Testing call_repomix")
    call_repomix(prompt)

    print("## Testing read_file")
    print(read_file('custom-output.md'))
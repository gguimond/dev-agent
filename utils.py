from openai import OpenAI
import os

llm_api_key = os.environ.get("LITELLM_API_KEY")
llm_api_base = "https://llmproxy.ai.orange"

def call_llm(context):    
    client = OpenAI(
        api_key=llm_api_key,
        base_url=llm_api_base
    )
    prompt = f"""
You are a senior developer. Your job is to do a thorough code review of this code. 
You should write it up and output markdown. Include line numbers, and contextual info. 
Your code review will be passed to another teammate, so be thorough. Think deeply before writing the code review. 
Review every part, and don't hallucinate.
"""
    response = client.chat.completions.create(
        model="openai/gpt-o3-mini", # model to send to the proxy
        messages = [
            context,
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content

def call_repomix(path):    
    os.system('node ./node_modules/repomix/bin/repomix.cjs ' + path)

def read_file(path):    
    f=open(path)
    s=f.read()
    f.close()
    return s

def create_file(name, content):    
    f=open("./" + name, 'w+')
    s=f.write(content)
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
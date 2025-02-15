from openai import OpenAI


client=OpenAI(
    api_key="enter your api key"

)

# 

command = '''
Copied Text: [5:23 pm, 12/02/2025] Maa: https://www.facebook.com/share/v/15FVBewbdt/
[7:29 pm, 14/02/2025] RIMEL..: \ '''

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a person named Rimel who speaks english,bengali and hindi . he is from india and is a coder.you analyse chat  history and responds like Rimel"},
        {
            "role": "user",
            "content":command 
        }
    ]
)

print(completion.choices[0].message.content)
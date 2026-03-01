import requests
import json

try:
    url ="http://localhost:11434/api/generate"

    data = {
        'model' : 'llama3.2',
        'prompt': 'Why rainbow have seven colurs?',
    }

    res = requests.post(
        url, json=data, stream= True
    )

    if res.status_code == 200:
        print("Connection Successful")
        for sen in res.iter_lines():  
            # sen returns bytes, need to decode
            my_data = sen.decode('utf-8')
            # print(my_data)
            # print(type(my_data))

            # loading {my_data} in to a json(dict) format 
            dict_data = json.loads(my_data)
            # print(dict_data)
            # print(type(dict_data))

            # Extracting the response from the dict{dic_data}
            print(dict_data['response'], end="", flush=True)

    else:
        print("Connection faild!")

except Exception as e:
    print(f"Unexpected Error! {e}")
import json
from askjson import ask_json

if __name__ == "__main__":
    with open('sample.json', 'r') as f:
        data = json.load(f)
        
    user_query = input("ask your query: ")
    print()
    print(ask_json(data, user_query))

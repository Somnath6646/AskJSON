import json
from .utils import describe_json, generate_response, execute_api_code, colored, install_missing_libraries

def ask_json(data, user_query, model="gpt-4"):
    descr = describe_json(data)
    
    prompt = f'''
    So we have a json whose structure's can be described with the following struct:
    {descr}
    
    You are an AI developer who is trying to write a program that will generate code for the user based on their intent. only write valid code

        
    Our Goal is to find the proper answer to the user's query in the format the user wants (markdown and use tables where it will be better)
    Use json's description to write the python code to find the answer to the user query.
    Have proper print messages. 



    Only If there is String Matching required: never do absolute string matches, use fuzzywuzzy python lib  if no string matching required then ignore this rule
    the code is for: {user_query}


    Remember these rules that you have to obey:
    1) Only give code, no explainations or anything, Only Code
    2) the purpose for the code is to print the answer for {user_query}
    3) Write the code only in python
    4) Write the code assuming that you already have a `data` variable which has the json in string. DO NOT include the declaration for this variable.

    Begin generating the code now.
    '''
    

    code = f"data = \'\'\'{json.dumps(data)}\'\'\'\n"+generate_response(prompt=prompt, model=model)
    install_missing_libraries(code)
    output = execute_api_code(code=code)
    return { "output": output }

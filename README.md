
### AskJSON

As the name suggests, `AskJSON` helps you fetch answers or data from your json using natural language. It uses OpenAI API.

#### How to Use AskJSON:

1. Install the package using pip:

   ```
   pip install AskJSON
   ```
2. Set your OpenAI API key as an environment variable:

   ```
   export OPENAI_API_KEY='your_api_key_here'
   ```
3. In your Python script, import `ask_json` and call it with your JSON and query:

   ```python
   from askjson import ask_json

   my_json_data = {...}  # Your JSON data here
   my_query = "How many items are in the list?"

   result_code = ask_json(my_json_data, my_query)
   print(result_code)
   ```

#### Todo:

- have support for codellama

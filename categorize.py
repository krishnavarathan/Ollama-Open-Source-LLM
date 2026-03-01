import ollama
import os

input_file = 'data/grocery.txt'
output_file = 'data/order_grocery.txt'

if not os.path.exists(input_file):
    print("Not")
    exit(1)

with open(input_file, 'r') as f:
    items=f.read().strip()

# print(items)

prompt = f"""
You are an assistant that categorizes and sorts grocery items.

Here is a list of grocery items:

{items}

Please:

1. Categorize these items into appropriate categories such as Produce, Dairy, Meat, Bakery, Beverages, etc.
2. Sort the items alphabetically within each category.
3. Present the categorized list in a clear and organized manner, using bullet points or numbering.

"""
try:
    response = ollama.generate(
        model='llama3.2',
        prompt=prompt
    )
    # for i in response:
    #     print(i.response, end="", flush=True)
    gen_text = response.get('response', "")
    with open(output_file, 'w') as w:
        w.write(gen_text.strip())

    print(f"Sorted categorize: \n {output_file}")

except Exception as e:
    print(f"An error occured: {e}")

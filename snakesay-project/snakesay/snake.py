SNAKE = r""" \
   {oo}
    (_)\
     λ \\
       _\\__
      (______)_
    (__________)oo°
"""

def bubble(message):
    bubble_length = len(message) + 2
    return f"""
{'_' * bubble_length}
({message})
{'-' * bubble_length}"""

def say(message):
    print(bubble(message))
    print(SNAKE)
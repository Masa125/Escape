direction_prompt = '''
\nYou can only move left, right, forward, or backward.
Where do you want to go? '''
action_prompt = '''
\nThe only items are the sword, axe, bow, strength potion, poison potion,
invincibility potion, and health potion.
What item do you want to use? '''

directions = ['left', 'right', 'forward', 'backward']
actions = ['sword', 'strength potion', 'poison potion',
           'invinciblity potion', 'axe', 'bow', 'health potion']

while True:
    direction = input(direction_prompt)
    if direction == 'quit':
        break
    elif direction in directions:
        print(f"You will move {direction}.")
    else:
        print("\nYou can only move left, right, forward, or backward.")
        break
    action = input(action_prompt)
    if action == 'quit':
        break
    elif action in actions:
        print(f"You selected the {action}.")
        break
    else:
        print('''
\nThe only items are the sword, axe, bow, strength potion, poison potion,
invincibility potion, and health potion.
''')
        break

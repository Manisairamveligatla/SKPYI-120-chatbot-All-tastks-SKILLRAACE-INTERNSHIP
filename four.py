def remove_common_characters(name1, name2):
    name1_list = list(name1)
    name2_list = list(name2)

    for char in name1:
        if char in name2_list:
            name1_list.remove(char)
            name2_list.remove(char)

    return name1_list + name2_list

def calculate_flames_count(combined_names):
    return len(combined_names)

def get_flames_result(flames_count):
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    flames_meanings = {
        'F': "Friends",
        'L': "Love",
        'A': "Affection",
        'M': "Marriage",
        'E': "Enemies",
        'S': "Siblings"
    }
    
    while len(flames) > 1:
        split_index = (flames_count % len(flames)) - 1
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]
    
    return flames_meanings[flames[0]]

def flames_game(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    combined_names = remove_common_characters(name1, name2)
    flames_count = calculate_flames_count(combined_names)
    result = get_flames_result(flames_count)

    return result

# Example usage
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

result = flames_game(name1, name2)
print(f"The FLAMES result is: {result}")

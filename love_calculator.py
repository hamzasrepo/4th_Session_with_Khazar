



def calculate_love_score(name1, name2):
    combined_name = name1 + name2

    count_of_true = 0
    count_of_love = 0

    for letter in "true":
        count_of_true = count_of_true + combined_name.count(letter)

    for letter in "love":
        count_of_love = count_of_love + combined_name.count(letter)

    love_score = f"{count_of_true}{count_of_love}"
    return love_score




print(calculate_love_score(name1="Kanye West", name2= "Kim Kardashian"))
#calculate_love_score("Kanye West", "Kim Kardashian")
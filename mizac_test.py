import matplotlib.pyplot as plt

# Define the questions and choices
questions = [
    "Question 1: Mevsimlerdeki Sıcaklık Hissiniz Nedir?",
    "Question 2: Ses Tonunuz Nasıldır?",
    "Question 3: Cinsiyetiniz Nedir?",
    "Question 4: İyimsermisiniz Yoksa Karamsar Mı",
    # Add more questions here...
]

choices = [
    {
        "a) Sıcak mevsimlerde çok ısınırım": ["A"],
        "b) Tüm mevsimlerde ısınırım": ["B"],
        "c) Soğuk mevsimlerde üşürüm": ["C"],
        "d) Tüm mevsimlerde uşürüm": ["D"],
        "e) None": ["E"],
    },
    {
        "a) Dog": ["A"],
        "b) Cat": ["B"],
        "c) Bird": ["C"],
        "d) Elephant": ["C", "D"],
        "e) None": ["E"],
    },
    {
        "a) Spring": ["A"],
        "b) Summer": ["B"],
        "c) Autumn": ["C"],
        "d) Winter": ["D"],
        "e) None": ["E"],
    },
    {
        "a) Spring": ["A"],
        "b) Summer": ["B"],
        "c) Autumn": ["C"],
        "d) Winter": ["D"],
        "e) None": ["E"],
    },
    # Add more choices here...
]

# Define the personality types and their corresponding descriptions
personalities = {
    "A": "DEM",
    "B": "SAFRA",
    "C": "SOVDA",
    "D": "BALGAM",
    "E": "DENGE",
    # Add more personality types and descriptions here...
}

# Initialize personality type scores
personality_scores = {personality: 0 for personality in personalities}

# Display the questions and get the user's answers
for i in range(len(questions)):
    print(questions[i])
    for choice, associated_personalities in choices[i].items():
        print(choice)
    answer = input("Enter your choice (a, b, c, d,e): ")
    
    # Update personality scores based on selected choices
    for choice, associated_personalities in choices[i].items():
        #ignore the 'e' choice cause that is denge and has no wight.
        if answer.lower() == 'e':
            continue 
        elif answer.lower() == choice.split(')')[0].lower():
            for personality in associated_personalities:
                personality_scores[personality] += 1

# Display the result as a graph
personality_types = list(personality_scores.keys())
scores = list(personality_scores.values())

plt.bar(personality_types, scores)
plt.xlabel("Personality Type")
plt.ylabel("Score")
plt.title("Personality Test Results")
plt.show()

# Display the result with descriptions
for personality, score in personality_scores.items():
    print("Personality Type:", personality)
    print("Description:", personalities.get(personality, "No description available."))
    print("Score:", score)
    print()

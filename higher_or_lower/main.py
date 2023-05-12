import random
from game_data import data


def add_to_queue(self, elements_to_add):
    for i in range(elements_to_add):
        data = self.game_data.pop(self.generate_random_number())
        self.queue.append(data)

def generate_random_number(self):
    return random.randint(0, len(data) - 1)

def add_to_choice_mapping(self):
    if not self.choice_mapping:
        self.choice_mapping["a"] = self.game_data.pop()

    self.choice_mapping["b"] = self.game_data.pop()

def display_vs(self):
    print(
        f"Compare A: {self.choice_mapping['a']['name']} is a {self.choice_mapping['a']['description']} from {self.choice_mapping['a']['country']}"
    )
    print("vs")
    print(
        (
            f"Against B: {self.choice_mapping['b']['name']} is a {self.choice_mapping['b']['description']} from {self.choice_mapping['b']['country']}"
        )
    )

def player_choice(self):
    self.choice = ""
    while self.choice not in ("a", "b"):
        self.choice = "a"  # input("Who has more followers? A or B\n").lower()

def compare_player_choice(self):
    if self.choice == 'a' and self.choice_mapping['a']['follower_count'] > self.choice_mapping['b']['follower_count']:
        print("That is correct")
        self.play_on = True
    elif self.choice == 'b' and self.choice_mapping['a']['follower_count'] < self.choice_mapping['b']['follower_count']:
        print("That is correct")
        self.play_on = True
    elif self.choice == 'a' and self.choice_mapping['a']['follower_count'] < self.choice_mapping['b']['follower_count']:
        print("That is incorrect")
        self.play_on = False
    elif self.choice == 'b' and self.choice_mapping['a']['follower_count'] > self.choice_mapping['b']['follower_count']:
        print("That is incorrect")
        self.play_on = False
    else:
        print("They have the same number of followers") 


while play_on:
    add_to_choice_mapping()
    display_vs()
    player_choice()
    compare_player_choice()  

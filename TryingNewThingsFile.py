import random


def get_random_winners(participants, quantity):
    participant_keys = list(participants.keys())

    if quantity > len(participant_keys):
        return []
    random_winners = random.sample(participant_keys, quantity)
    return random_winners

participants = {
    "603d2cec9993c627f0982404": "test@test.com",
    "603f79022922882d30dd7bb6": "test11@test.com",
    "60577ce4b536f8259cc225d2": "test2@test.com",
    "605884760742316c07eae603": "vitanlhouse@gmail.com",
    "605b89080c318d66862db390": "elhe2013@gmail.com",
}

quantity_of_winners = 2
random_winner_ids = get_random_winners(participants, quantity=quantity_of_winners)
print(random_winner_ids)


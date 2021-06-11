"""
Final assignment Python HvA: Ali Sultan
Checked with Pylint,Black and PEP8.
Now the program keeps track of how long you rested and
whether you can train and if so how much you can train.
All inputs are checked using agechecker / is_int / is_float / anytime_exit
With this program we keep a sports schedule, and the program gives suggestions
per body group how much weight can be trained.
This according to the theory of hypertrophy.
"""


from dataclasses import dataclass
import sys
import pickle
import subprocess
import random
import time
from datetime import datetime
import os.path


@dataclass
class Bodybuilder:
    """ This class makes user as a object."""
    database_user_info: list = ()

    def __init__(self, first, last, age, gender):
        self.first: str = first
        self.last: str = last
        self.age: int = age
        self.gender: str = gender

        Bodybuilder.database_user_info.append(self)


class Statistic:
    """ This class keeps the statistics"""
    database_user_statistic: list = []

    def __init__(self, push, pull, legs, weight):
        self.push: int = push
        self.pull: int = pull
        self.legs: int = legs
        self.weight: int = weight
        Statistic.database_user_statistic.append(self)

    def update(
        self,
        push_list_input,
        pull_list_input,
        legs_list_input,
        weight_list_input,
    ):
        """This function adds object information to list."""
        trained_today = input("Heb je vandaag getraind?")

        if trained_today in yes_list:
            legs_list_input.append(self.legs)
            pull_list_input.append(self.pull)
            push_list_input.append(self.push)
            week_list.append(len(week_list))
            weight_list_input.append(self.weight)
            time_list.append(time.time())
        else:
            menu_user(user_data, time_now)


yes_list = ["Ja", "ja", "JA", "j", "Si", "jah"]
subprocess.call("cls", shell=True)

age_list = range(12, 120)
# Try to load files and if it does not exist create it.
if not os.path.isfile("time_list.pickle"):
    time_list = []
    pickle.dump(time_list, open("legs_list.pickle", "wb"))
else:
    pickle_in_time = open("time_list.pickle", "rb")
    time_list = pickle.load(pickle_in_time)

if not os.path.isfile("legs_list.pickle"):
    legs_list = []
    pickle.dump(legs_list, open("legs_list.pickle", "wb"))
else:
    pickle_in_legs = open("legs_list.pickle", "rb")
    legs_list = pickle.load(pickle_in_legs)

if not os.path.isfile("push_list.pickle"):
    push_list = []
    pickle.dump(push_list, open("push_list.pickle", "wb"))
else:
    pickle_in_push = open("push_list.pickle", "rb")
    push_list = pickle.load(pickle_in_push)

if not os.path.isfile("pull_list.pickle"):
    pull_list = []
    pickle.dump(pull_list, open("pull_list.pickle", "wb"))
else:
    pickle_in_pull = open("pull_list.pickle", "rb")
    pull_list = pickle.load(pickle_in_pull)
if not os.path.isfile("week_list.pickle"):
    week_list = []
    pickle.dump(week_list, open("week_list.pickle", "wb"))
else:
    pickle_in_week = open("week_list.pickle", "rb")
    week_list = pickle.load(pickle_in_week)
if not os.path.isfile("weight_list.pickle"):
    weight_list = []
    pickle.dump(weight_list, open("weight_list.pickle", "wb"))
else:
    pickle_in_weight = open("weight_list.pickle", "rb")
    weight_list = pickle.load(pickle_in_weight)

if not os.path.isfile("bodybuilder.pickle"):
    user_data = Bodybuilder("none", "none", 0, "m")
    pickle.dump(user_data, open("bodybuilder.pickle", "wb"))
else:
    pickle_in = open("bodybuilder.pickle", "rb")
    user_data = pickle.load(pickle_in)


LIST_AGE_RUNNING = bool(age_list)
LIST_LEGS_RUNNING = bool(legs_list)

print(
    f" system check:\n Lijst leeftijd werkzaam? {LIST_AGE_RUNNING}"
    f"\n Lijst benen ingevuld? "
    f"{LIST_LEGS_RUNNING}\n "
)
time_now = time.time()


def calculate_rest_hours(time_now_input):
    """ Calculates the hours rest between last training and current time. """

    if len(time_list) == 0:
        last_time = 0
    else:
        last_time = time_list[-1]
    hours_rest_output = (time_now_input - last_time) / 3600
    return hours_rest_output


def anytime_exit(humaninput):
    """ Let the user quit anytime. """

    list_stop = ["Q", "q", "quit", "Quit", "Stop", "stop"]
    if humaninput in list_stop:
        sys.exit(f"Ok {support_name_generator()} !")
    return humaninput


def is_int(stringinput):
    """ Checks the input for being numeric and casts it to integer. """

    while not stringinput.isnumeric() or stringinput == "":
        stringinput = anytime_exit(input("Geef alstublieft een getal."))
    stringinput = int(stringinput)
    return stringinput


def is_float(stringinput):
    """ Checks the input for being numeric and casts it to float. """

    while not stringinput.isnumeric() or stringinput == "":
        stringinput = input("Geef alstublieft een getal.")
    stringinput = float(int(stringinput))
    return stringinput


def age_checker(input_user):
    """ Validates the age of user."""

    if input_user not in age_list:
        print(
            "Je bent of te jong of te oud voor dit programma."
            " Blijf wel sporten!"
        )
    return input_user


def gender_user(input_user):
    """ Checks input gender according to list. """

    male_list = ["m", "man", "M", "Man", "Manno"]
    if input_user in male_list:
        input_user = "m"
    else:
        input_user = "v"
    return input_user


def support_name_generator():
    """This function is to generate supportive nicknames and return it
    wherever needed in a print statement"""

    support_list_names = [
        "kanjer",
        "baas",
        "tijger",
        "chef",
        "eindbaas",
        "schwarzenegger",
        "patron",
        "topper",
    ]
    chosen_word = random.choice(support_list_names)
    return chosen_word


def pickle_out_function(
    push_list_input,
    pull_list_input,
    legs_list_input,
    week_list_input,
    weight_list_input,
):
    """ Saves all lists and closes them. """

    pickle_out_push = open("push_list.pickle", "wb")
    pickle.dump(push_list_input, pickle_out_push)
    pickle_out_push.close()
    pickle_out_pull = open("pull_list.pickle", "wb")
    pickle.dump(pull_list_input, pickle_out_pull)
    pickle_out_pull.close()
    pickle_out_legs = open("legs_list.pickle", "wb")
    pickle.dump(legs_list_input, pickle_out_legs)
    pickle_out_legs.close()
    pickle_out_week = open("week_list.pickle", "wb")
    pickle.dump(week_list_input, pickle_out_week)
    pickle_out_week.close()
    pickle_out_weight = open("weight_list.pickle", "wb")
    pickle.dump(weight_list_input, pickle_out_weight)
    pickle_out_weight.close()
    pickle_out_time = open("time_list.pickle", "wb")
    pickle.dump(time_list, pickle_out_time)
    pickle_out_time.close()


def welcome_user():
    """ Welcomes the user. If user exists, greet by name. """

    subprocess.call("cls", shell=True)
    new_welcome = "Welkom, bij Automated Hypertrophy!"
    new_welcome_centre = new_welcome.center(30, "*")
    welcome = f"Welkom {user_data.first}, bij Automated Hypertrophy!"
    welcome_centre = welcome.center(30, "*")

    if user_data.first == "none":
        print(new_welcome_centre)
    else:
        print(welcome_centre)

    anytime_exit(
        input("Druk op enter om verder te gaan of Q+Enter om af te sluiten.")
    )
    menu_user(user_data, time_now)


def menu_user(user_1_input, time_now_input):
    """ Gives the user options to choose a function to perform. """

    user_1_input.first = user_1_input.first
    hours_rest = calculate_rest_hours(time_now_input)
    subprocess.call("cls", shell=True)
    print("Automated Hypertrophy keuzemenu")
    if hours_rest > 24:
        print("Je mag trainen!")
    # file_name_username = 'bodybuilder_name.txt'
    # open_txt_name = open(file_name_username, 'r')
    # read_txt_name = open_txt_name.read()
    if user_1_input.first == "none":
        print("0. Maak een nieuwe gebruiker aan.")
        print("Q. Druk Q en enter om het programma te verlaten.")
    else:
        print("1. Laad sportgeschiedenis.")
        print("2. Bereken hoeveel je mag trainen.")
        print("3. Verwijder alle gegevens en start opnieuw.")
        print("Q. Druk Q en enter om het programma te verlaten.")

    while True:
        choice_user = anytime_exit(input())
        if choice_user == "0":
            create_user()
        elif choice_user == "1":
            load_history()
        elif choice_user == "2":
            hypertrophy()
        elif choice_user == "3":
            reset_user(user_1_input)


def create_user():
    """ Makes an Bodybuilder object as a variable. """

    user_data_input = Bodybuilder(
        (anytime_exit(input("Geef je Voornaam."))),
        (anytime_exit(input("Geef je Achternaam."))),
        (anytime_exit(age_checker(is_int(input("Geef je leeftijd?"))))),
        (anytime_exit(gender_user(input("Man of Vrouw?")))))
    user_data_statistic = Statistic(
        (anytime_exit(is_int(input("Hoeveel kun je bankdrukken?")))),
        (anytime_exit(is_int(input("Hoeveel kun je pullen?")))),
        (anytime_exit(is_int(input("hoeveel kun je squaten?")))),
        (anytime_exit(is_float(input("Hoeveel weeg je?"))))
    )
    pickle_out = open("bodybuilder.pickle", "wb")
    pickle.dump(user_data_input, pickle_out)
    pickle_out2 = open("bodybuilder_statistic.pickle", "wb")
    pickle.dump(user_data_statistic, pickle_out2)
    pickle_out.close()
    pickle_out2.close()

    user_data_statistic.update(push_list, pull_list, legs_list, weight_list)
    pickle_out_function(
        push_list, pull_list, legs_list, week_list, weight_list
    )
    menu_user(user_data_input, time_now)


def reset_user(user_1):
    """ Erases user_1 and empties all lists."""

    last_check = anytime_exit(
        input("Weet je zeker dat je alle gegevens wilt verwijderen?")
    )

    if last_check in yes_list:
        user_1 = Bodybuilder("none", "none", 0, "m")
        pickle_out = open("bodybuilder.pickle", "wb")
        pickle.dump(user_1, pickle_out)
        pickle_out.close()
        legs_list.clear()
        push_list.clear()
        pull_list.clear()
        week_list.clear()
        weight_list.clear()
        time_list.clear()
        pickle_out_function(
            push_list, pull_list, legs_list, week_list, weight_list
        )

    menu_user(user_1, time_now)


def load_history():
    """ Loads the history of user_1. """

    subprocess.call("cls", shell=True)
    print("%10s" % "Training:", end=" ")
    for i in week_list:
        print("%10s" % f"{i}", end=" ")
    print("")
    print("%10s" % "Datum:", end=" ")
    for i in time_list:
        print(f"{datetime.fromtimestamp(i).strftime('%d-%m-%Y')}", end=" ")
    print("")
    print("%10s" % " Tijdstip:", end=" ")
    for i in time_list:
        print(
            "%10s" % f"{datetime.fromtimestamp(i).strftime('%H:%M:%S')}",
            end=" ",
        )
    print("")
    print("%10s" % "Squaten:", end=" ")
    for i in legs_list:
        print("%10s" % f"{i}KG", end=" ")
    print("")
    print("%10s" % "Pushen:", end=" ")
    for i in push_list:
        print("%10s" % f"{i}KG", end=" ")
    print("")
    print("%10s" % "Pullen:", end=" ")
    for i in pull_list:
        print("%10s" % f"{i}KG", end=" ")
    print("")
    print("%10s" % "Gewicht:", end=" ")
    for i in weight_list:
        print("%10s" % f"{i}KG", end=" ")
    print("")
    edit_history_button_e = anytime_exit(
        input("druk enter om door te gaan. "
              "Voer e in om dagen te " "bewerken.")
    )
    if edit_history_button_e == "e":
        edit_history()
    else:
        menu_user(user_data, time_now)


def edit_history():
    """ Edits the history of user_1. """

    for i in (week_list, legs_list, push_list, pull_list, weight_list):
        print(f"**{i}")
    while True:
        index_day = anytime_exit(is_int(input("Welke dag wil je wijzigen?")))
        if len(week_list) >= index_day:
            break
    delete_day = anytime_exit(
        input("Druk nogmaals enter om te wijzigen of V om te verwijderen.")
    )
    if delete_day == "V":
        week_list.pop(index_day)
        legs_list.pop(index_day)
        push_list.pop(index_day)
        pull_list.pop(index_day)
        weight_list.pop(index_day)
        time_list.pop(index_day)
        pickle_out_function(
            push_list, pull_list, legs_list, week_list, weight_list
        )
        menu_user(user_data, time_now)
    else:
        legs_list[index_day] = is_int(input("Wat heb je op die dag gesquat?"))
        push_list[index_day] = is_int(input("En wat heb je die dag gepusht?"))
        pull_list[index_day] = is_int(input("En gepulled?"))
        weight_list[index_day] = is_float(input("Wat woog je toen?"))
        pickle_out_function(
            push_list, pull_list, legs_list, week_list, weight_list
        )
        menu_user(user_data, time_now)


def hypertrophy():
    """ Calculate if the user can train and how much the user can train. """
    if not week_list:
        hours_rest = is_int(
            input("Hoeveel uur geleden heb jij voor het laatst getraind?")
        )
    else:
        hours_rest = calculate_rest_hours(time_now)
    if len(week_list) < 1:
        legs_today = user_data.legs
        push_today = user_data.push
        pull_today = user_data.pull
    else:
        legs_today = legs_list[-1]
        push_today = push_list[-1]
        pull_today = pull_list[-1]
    overview = (
        f"{legs_today} kg voor je benen.\n{push_today} kg voor je triceps en "
        f"borsten.\n {pull_today} kg voor je biceps en rug."
    )
    if week_list == 0:
        print("Je wilt dus in de eerste week nog een keer trainen!")
    else:
        print(
            "We gaan weer trainen. Jij wilt vast weten hoeveel je nog mag "
            "trainen."
        )
    if hours_rest < 24:
        print(
            f"Ho ho. Niet overtrainen, {support_name_generator()} . Wacht "
            f"minimaal 24 uur voor je gaat trainen.Je hebt {hours_rest:.2f}"
            f"uur rust genomen."
        )
        menu_user(user_data, time_now)
    elif 24 <= hours_rest <= 36:
        print(
            f"Je hebt een dag rust genomen, {support_name_generator()}. Je mag"
            f" hetzelfde gewicht weer gaan trainen."
        )
    elif 36 < hours_rest < 48:
        print(
            f"Je hebt net geen 2 dagen rust genomen, "
            f"{support_name_generator()}."
        )
        legs_today += 5
        push_today += 3
        pull_today += 3
    elif 48 <= hours_rest <= 96:
        print(f"Je hebt perfect rust genomen,{support_name_generator()}. ")
        legs_today += 10
        push_today += 5
        pull_today += 5
    elif 96 < hours_rest <= 168:
        print(
            f"Je hebt flink wat rust genomen, {support_name_generator()}."
            f" Je mag meer trainen!"
        )
        legs_today += 5
        push_today += 3
        pull_today += 3
    else:
        print(
            f"Je hebt teveel rust genomen, {support_name_generator()}."
            f" Train zelfde gewicht."
        )
    anytime_exit(input(f"{overview}\nDruk Enter als je klaar bent."))
    append_user(legs_today, push_today, pull_today)


def append_user(legs_input, push_input, pull_input):
    """ Appends the calculated training to the training lists. """

    user_result = anytime_exit(
        input(
            f"Heb je alles gedaan zoals geadviseerd, "
            f"{support_name_generator()}?"
        )
    )
    if user_result in yes_list:
        print("ok")
        legs_list.append(legs_input)
        push_list.append(push_input)
        pull_list.append(pull_input)
    else:
        legs_list.append(int(input("Hoeveel kg voor je benen?")))
        push_list.append(int(input("Hoeveel kg voor je triceps en borsten?")))
        pull_list.append(int(input("Hoeveel kg voor je biceps en rug.")))
    weight_list.append(float(input("Hoeveel weeg je nu?")))
    time_list.append(time.time())
    week_list.append(len(week_list))
    pickle_out_function(
        push_list, pull_list, legs_list, week_list, weight_list
    )
    menu_user(user_data, time_now)


welcome_user()

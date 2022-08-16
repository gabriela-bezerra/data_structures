"""Functions to parse a file containing villager data."""


from tkinter import N


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    # TODO: replace this with your code

    data_log = open(filename)

    for line in data_log:
        line = line.rstrip()
        words = line.split("|")

        species_file = words[1]
        species.add(species_file)

    return species

    data_log.close


# print(all_species("villagers.csv"))


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    # TODO: replace this with your code
    data_log = open(filename)

    search_species = search_string

    for line in data_log:
        line = line.rstrip()
        words = line.split("|")

        names_by_species = words[0], words[1]
        if search_species in names_by_species:
            villagers.append(names_by_species)

    return sorted(villagers)


# print(get_villagers_by_species("villagers.csv", "Horse"))


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code

    data_log = open(filename)

    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    for line in data_log:

        name, _, _, hobby, _ = line.rstrip().split("|")

        if hobby == "Fitness":
            fitness.append(name)
        elif hobby == "Nature":
            nature.append(name)
        elif hobby == "Education":
            education.append(name)
        elif hobby == "Music":
            music.append(name)
        elif hobby == "Fashion":
            fashion.append(name)
        elif hobby == "Play":
            play.append(name)

    return [
        sorted(fitness),
        sorted(nature),
        sorted(education),
        sorted(music),
        sorted(fashion),
        sorted(play),
    ]


# print(all_names_by_hobby("villagers.csv"))


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    data_log = open(filename)

    for line in data_log:

        name, species, personality, hobby = line.rstrip().split("|")

        all_data.append(tuple(name, species, personality, hobby))
        # all_data.append(tuple(line.rstrip().split("|")))

    return all_data


# print(all_data("villagers.csv"))


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code

#     data_log = open(filename)

#     # motto_result = ""

#     # for line in filename:
#     #     name, _, _, _, motto = line.rstrip(), line.split("|")

#     #     if villager_name == name:
#     #         motto_result = motto

#     # return motto_result

#     for name, _, _, _, motto in data_log(filename):
#         if name == villager_name:
#             return motto


# print(find_motto("villagers.csv", "Tutu"))


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code

    # likeminded = set()

    # target_personality = None
    # for villager_data in all_data(filename):
    #     name, _, personality = villager_data[:3]

    #     if name == villager_name:
    #         target_personality = personality
    #         break

    # if target_personality:
    #     for villager_data in all_data(filename):
    #         name, _, personality = villager_data[:3]
    #         if personality == target_personality:
    #             likeminded.add(name)

    # return likeminded

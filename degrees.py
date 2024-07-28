import csv
import sys
from util import Node, StackFrontier, QueueFrontier


# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set(),
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set(),
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    """
    Main function to execute the program.
    """
    # Check for correct command-line usage
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    # Get source and target actors
    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")

    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    # Find shortest path between source and target
    path = shortest_path(source, target)

    # Print the results
    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    # Number of states explored
    states_explored = 0

    # Initialize the starting node
    start = Node(state=source, parent=None, action=None)

    # Initialize the frontier using a queue (BFS - Breadth-First Search)
    frontier = QueueFrontier()
    frontier.add(start)

    # Initialize an empty explored set
    explored = set()

    # Loop until a solution is found
    while True:
        # If the frontier is empty, no path exists
        if frontier.empty():
            return None

        # Remove a node from the frontier
        node = frontier.remove()
        states_explored += 1

        # Add the node's state to the explored set
        explored.add(node.state)

        # Expand node, adding neighbors to the frontier
        for movie_id, person_id in neighbors_for_person(node.state):
            # If the neighbor has not been explored and is not in the frontier
            if not frontier.contains_state(person_id) and person_id not in explored:
                # Create a new node for the neighbor
                child = Node(state=person_id, parent=node, action=movie_id)
                # If the neighbor is the target, return the path
                if child.state == target:
                    path = []
                    # Follow parent pointers to generate the path
                    while child.parent is not None:
                        path.append((child.action, child.state))
                        child = child.parent
                    path.reverse()
                    return path

                # Add the child to the frontier
                frontier.add(child)


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()



# Usage Example

# RUN: python degrees.py large
# Example names: Emma Watson and Jennifer Lawrence; Kevin Bacon and Tom Hanks; Juliane Banse and Julian Acosta.
# Or you can check the large and small datasets to get the names you want.


# python degrees.py large
# Loading data...
# Data loaded.
# Name: Emma Watson
# Name: Jennifer Lawrence
# 3 degrees of separation.
# 1: Emma Watson and Meryl Streep starred in Little Women
# 2: Meryl Streep and Robert De Niro starred in Falling in Love
# 3: Robert De Niro and Jennifer Lawrence starred in Joy

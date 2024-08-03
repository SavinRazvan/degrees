# Degrees

Created a social network analysis tool to determine the degrees of separation between actors using the Breadth-First Search (BFS) algorithm. The program processes data from IMDb, computes the shortest path of connections through shared movie roles, and outputs the sequence of movies that connect any two actors.

### Objective

Write a program that computes the shortest path between any two actors by identifying the sequence of movies that connects them.

### Data

The project uses datasets based on IMDb, containing information about actors, movies, and the relationships between them. These datasets include `people.csv`, `movies.csv`, and `stars.csv`, which provide the necessary details to compute the degrees of separation.

### How It Works

1. **Data Input**: Load data from CSV files into memory. The files include `people.csv`, `movies.csv`, and `stars.csv`.
2. **Data Structures**: Use dictionaries to map names to person IDs, person IDs to details (name, birth year, movies), and movie IDs to details (title, year, stars).
3. **User Input**: Prompt the user to input two actor names.
4. **Shortest Path Calculation**: Implement the `shortest_path` function to find the shortest path using BFS. The function returns a list of (movie_id, person_id) pairs representing the path.
5. **Output**: Display the sequence of movies that connects the two actors.

### Example Usage

```console
$ python degrees.py large
Loading data...
Data loaded.
Name: Emma Watson
Name: Jennifer Lawrence
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
```

### Getting Started

1. **Download the distribution code**: Download from [CS50 AI Degrees project](https://cdn.cs50.net/ai/2023/x/projects/0/degrees.zip) and unzip it.
2. **Load Data**: Run the script with the appropriate data directory, e.g., `python degrees.py large`.

### Detailed Instructions

1. **Loading Data**: The script reads from `people.csv`, `movies.csv`, and `stars.csv` to build the necessary mappings and sets for people and movies.
2. **Finding Connections**: The `shortest_path` function utilizes BFS to explore connections between actors via movies. Each node in the search represents an actor, and edges represent movies connecting actors.
3. **Efficiency Considerations**: To optimize, check for the goal when adding nodes to the frontier rather than when removing them. This can reduce unnecessary expansions.

### Additional Information

For more details on the project, its background, and specific implementation requirements, visit the [CS50 AI 2024 Degrees Project Page](https://cs50.harvard.edu/ai/2024/projects/0/degrees).

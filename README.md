# Six Degrees of Kevin Bacon
## Overview
The "Six Degrees of Kevin Bacon" project is a Python-based exploration of the Hollywood universe, inspired by the popular game that suggests any actor can be linked through their film roles to Kevin Bacon in six steps or fewer. This project analyzes connections between actors in movies, building a graph network to calculate the degrees of separation.

## Features
### Data Parsing: Reads and processes cast data from movie files.
### Graph Construction: Builds a graph where vertices represent actors and movies, and edges represent the participation of an actor in a movie.
### Path Finding: Implements Breadth-First Search (BFS) to find the shortest path (minimum degrees of separation) between Kevin Bacon and any other actor.
### Average Degree Calculation: Computes the average degree of separation for Kevin Bacon to all other actors in the network.


## Installation
   Clone the repository:
   git clone https://github.com/swarba015/Six-Degrees-of-Kevin-Bacon/tree/main


## Usage
1. Load your movie and actor data into the specified format.
2. Run the main script to build the graph and perform analyses:
   python main.py




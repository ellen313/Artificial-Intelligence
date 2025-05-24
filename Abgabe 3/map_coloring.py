from constraint import *

problem = Problem()

federal_states = ["Schleswig-Holstein", "Mecklenburg-Vorpommern", "Bremen", "Hamburg",
                  "Brandenburg", "Berlin", "Sachsen-Anhalt", "Nordrhein-Westfalen",
                  "Rheinland-Pfalz", "Saarland", "Hessen", "Thüringen",
                  "Sachsen", "Bayern", "Baden-Württemberg", "Niedersachsen"]

neighbours = {"Schleswig-Holstein": ["Hamburg", "Mecklenburg-Vorpommern", "Niedersachsen"],
              "Mecklenburg-Vorpommern": ["Schleswig-Holstein", "Niedersachsen", "Brandenburg"],
              "Bremen": ["Niedersachsen"],
              "Hamburg": ["Schleswig-Holstein", "Niedersachsen"],
              "Brandenburg": ["Berlin", "Mecklenburg-Vorpommern", "Sachsen-Anhalt", "Sachsen"],
              "Berlin": ["Brandenburg"],
              "Sachsen-Anhalt": ["Brandenburg", "Niedersachsen", "Thüringen", "Sachsen"],
              "Nordrhein-Westfalen": ["Niedersachsen", "Hessen", "Rheinland-Pfalz"],
              "Rheinland-Pfalz": ["Saarland", "Nordrhein-Westfalen", "Hessen", "Baden-Württemberg"],
              "Saarland": ["Rheinland-Pfalz"],
              "Hessen": ["Baden-Württemberg", "Bayern", "Rheinland-Pfalz",
                         "Thüringen", "Niedersachsen", "Nordrhein-Westfalen"],
              "Thüringen": ["Sachsen", "Sachsen-Anhalt", "Niedersachsen", "Hessen", "Bayern"],
              "Sachsen": ["Berlin", "Sachsen-Anhalt", "Thüringen"],
              "Bayern": ["Baden-Württemberg", "Hessen", "Thüringen", "Sachsen"],
              "Baden-Württemberg": ["Bayern", "Hessen", "Rheinland-Pfalz"],
              "Niedersachsen": ["Bremen", "Hamburg", "Nordrhein-Westfalen", "Hessen", "Thüringen",
                                "Sachsen-Anhalt", "Brandenburg", "Mecklenburg-Vorpommern", "Schleswig-Holstein"]
              }

colours = ["pink", "green", "blue", "magenta"]
# colours_4 = ["red", "green", "blue", "magenta"]

for federal_state in federal_states:
    problem.addVariable(federal_state, colours)

# ---------- Constraints definieren ---------------
# kein aneinandergrenzendes Land darf die gleiche Farbe haben
for federal_state, neighbour_list in neighbours.items():
    for neighbour in neighbour_list:
        problem.addConstraint(lambda a, b: a != b, (federal_state, neighbour))


solution = problem.getSolution()
solutions = problem.getSolutions()
print(len(solutions))

if solution:
    for federal_state in sorted(solution):
        print(f"{federal_state}: {solution[federal_state]}")
else:
    print("No solution")

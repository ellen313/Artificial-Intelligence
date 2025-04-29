from constraint import Problem, AllDifferentConstraint

problem = Problem()

teachers = ["Maier", "Müller", "Huber", "Schmid"]
subjects = ["Englisch", "Deutsch", "Mathe", "Physik"]
rooms = [1, 2, 3, 4]

# Jedem Lehrer wird ein Raum und ein Fach zugewisen
for teacher in teachers:
    problem.addVariable(f"{teacher}_subject", subjects)
    problem.addVariable(f"{teacher}_room", rooms)

# ---------- Constraints definieren ---------------

# 1. Herr Maier prüft nie in Raum 4
problem.addConstraint(lambda r: r != 4, ["Maier_room"])

# 2. Herr Müller prüft immer Deutsch
problem.addConstraint(lambda s: s == "Deutsch", ["Müller_subject"])


# 3. Herr Schmid und Herr Müller prüfen nicht in benachbarten Räumen
def not_adjacent(r1, r2):
    return abs(r1 - r2) > 1


problem.addConstraint(not_adjacent, ["Schmid_room", "Müller_room"])

# 4. Frau Huber prüft Mathematik
problem.addConstraint(lambda s: s == "Mathe", ["Huber_subject"])

# 5. Physik wird immer in Raum 4 geprüft
def physik_raum4(*args):
    for i in range(0, len(args), 2):
        subject = args[i]
        room = args[i+1]
        if subject == "Physik" and room != 4:
            return False
    return True


phsyik_vars = []
for t in teachers:
    phsyik_vars.extend([f"{t}_subject", f"{t}_room"])

problem.addConstraint(physik_raum4, phsyik_vars)

# 6. Deutsch und Englisch werden nicht in Raum 1 geprüft
def de_en_nicht_raum1(*args):
    for i in range(0, len(args), 2):
        subject = args[i]
        room = args[i + 1]
        if subject in ["Deutsch", "Englisch"] and room == 1:
            return False
    return True


de_en_vars = []
for t in teachers:
    de_en_vars.extend([f"{t}_subject", f"{t}_room"])

problem.addConstraint(de_en_nicht_raum1, de_en_vars)

# jeder Lehrer prüft anderes Fach
problem.addConstraint(AllDifferentConstraint(), [f"{t}_subject" for t in teachers])


# jeder Lehrer prüft in anderem Raum
problem.addConstraint(AllDifferentConstraint(), [f"{t}_room" for t in teachers])

# ---------- CSP lösen -------------
solutions = problem.getSolutions()

for solution in solutions:
    for teacher in teachers:
        print(f"{teacher} prüft {solution[f'{teacher}_subject']} in Raum {solution[f'{teacher}_room']}")
    print("-" * 40)


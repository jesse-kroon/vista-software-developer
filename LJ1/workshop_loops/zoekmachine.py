results = []
students = [
    "Liam Johnson", "Emma Thompson", "Noah Williams", "Olivia Brown",
    "Mason Davis", "Ava Wilson", "Ethan Taylor", "Sophia Anderson",
    "Logan Martinez", "Isabella Thomas", "Lucas Hernandez", "Mia Moore",
    "Jacob Martin", "Charlotte Lee", "Benjamin Perez", "Amelia Harris",
    "Henry Clark", "Ella Lewis", "Jack Robinson", "Grace Walker",
    "Alexander Young", "Chloe King", "Samuel Wright", "Harper Scott",
    "Daniel Green"
]
# Start een infinite loop
while (True):
  # Vraag de gebruiker voor een naam
  query = input("Zoek naar een student: ")

  # Loop over alle studenten heen
  for student in students:
    # Komt de naam (deels) overeen met de query?
    if query.lower() == student.lower() or student.lower().find(query.lower()) >= 0:
      # Voeg de gevonden naam toe aan de lijst van resultaten
      results.append(student)

  # Laat zien hoeveel resultaten er gevonden zijn
  print(str(len(results)) + ' resultat(en) gevonden')

  # Loop over alle gevonden studenten heen en laat de naam zien
  for result in results:
    print(result)

  # Reset de gevonden resultaten
  results = []

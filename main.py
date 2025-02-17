mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]


total_missions = 0
successful_missions = 0
missions_before_2000 = []
success_rate = 0 

for i in range(len(mission_names)):
    total_missions += 1
    if mission_success[i]:
        successful_missions += 1
    if mission_years[i] < 2000:
        missions_before_2000.append(mission_names[i])

#the success rate as a percentage.
success_rate = (successful_missions / total_missions) * 100

print(f"\nthe total number of missions:\n{total_missions}\n")
print(f"the number of successful missions:\n{successful_missions}\n")
print(f"the success rate as a percentage:\n{success_rate:.2f}\n")
print(f"the names of the missions launched before the year 2000.\n{missions_before_2000}\n")



# epidemic_simulation

👋I created a simple simulation in python using pygame library that shows how people are infected with each other

colors means in wich state is a person:
-green - healthy person - can be infected
-red - ill person, can infects others with 50% chance
-purple - ill person, can infects others with 100% chance
-blue - immune person - can't be infected

to get infected 2 points (persons) have to be within 2m range for 2 seconds 
ill person gains immune after random time between 20-30s

the number of people is constant, if a person leaves the area, a new person with a random state will replace it

https://user-images.githubusercontent.com/72728316/151714198-d822d27c-1afb-4b5d-9a97-a56a5aa6a6f6.mp4

import json 
import matplotlib.pyplot as plt
from os import system
from datetime import datetime

EXERCISE_FILE = "exerciseFile.json"
SAVED_WORKOUTS = "savedWorkouts.json"
MUSCLEGROUP = ["back and bicep", "back", "chest and tricep", "legs and shoulders", "legs", "shoulders"]
    
class Exercise:
    exercises = []
    
    def __init__(self, muscleGroup, weight, reps, sets):
        self.muscleGroup = muscleGroup
        self.weight = weight
        self.reps = reps
        self.sets = sets
    
    def __str__(self):
        return f"{self.muscleGroup}\n {self.weight}KG\n {self.reps}\n {self.sets}\n"
    
    def __repr__(self):
        return f"{self.muscleGroup}\n {self.weight}KG\n {self.reps}\n {self.sets}\n"
    
    def printExercise(self):
        if len(self.exercises[0]) == 0:
            print("No exercises to print")
            return
        for exercises in self.exercises:
            if exercises[0]["muscleGroup"]:
                print("=" * 66)
                print("=" * 66)
                print("Day: {:<30}".format(exercises[0]["day"]))
                for exercise in exercises:
                    print("Exercise: {:<30} Reps: {:>5} Sets: {:>5}".format
                          (exercise["muscleGroup"], exercise["reps"], exercise["sets"]))
        print()
    
    def printExerciseList(self, muscleGroup):
        for exercises in self.exercises:
            if len(self.exercises[0]) == 0:
                print("No exercises to print")
                return
            if muscleGroup == "all":
                for exercises in self.exercises:
                    if exercises[0]["muscleGroup"]:
                        print("=" * 66)
                        print("=" * 66)
                        print("Day: {:<30}".format(exercises[0]["day"]))
                    for exercise in exercises:
                        print("Exercise: {:<30} Reps: {:>5} Sets: {:>5}".format
                            (exercise["muscleGroup"], exercise["reps"], exercise["sets"]))
            print()
            
    def getExercises(self, muscleGroup):
        data = importExercises()
        exerciseList = []
        for group in data[muscleGroup].items():
            for exerciseData in group:
                exercise = {}
                exercise["Musclegroup"] = muscleGroup
                exercise["Reps"] = exerciseData ["reps"]
                exercise["Sets"] = exerciseData ["sets"]
        self.exercises.append(exerciseList)
        return exerciseList
    
    def runExercise(self):
        data = importExercises()
        exerciseNumber = {
            "back and bicep": 1,
            "back": 2,
            "chest and tricep": 3,
            "legs and shoulders": 4,
            "legs": 5,  
            "shoulders": 6
        }
        muscleGroups = data.keys()
        
        print("Choose a muscle group: ")
        for i, muscleGroups in enumerate(muscleGroups):
            print(f"{i+1}. {muscleGroups}")
        
        choice = int(input())
        selectedMuscleGroup = [muscleGroups for muscleGroups, number in exerciseNumber.items() if number == choice][0]
        exercises = data.get(selectedMuscleGroup, [])
        
        sets = 0
        for exercise in exercises:
            print(f"Exercise: {exercise['exercise']}")
            
            while True:
                weight = float(input("Enter weight: "))
                reps = float(input("Enter reps: "))
                
                sets += 1
                
                continueExercise = input("Continue exercise? (y/n)")
                if continueExercise.lower() == "n":
                    break
                
                saveWorkout(exercise, weight, reps, sets)
                
        print("Workout is saved")
            
             
def getInput():
    while True:
        userInput = input().lower()
        userInput = userInput.split()
        if len(userInput) >= 1:
            return userInput
        else:
            return "Error"

# this opens exerciseFile.json
def importExercises():
    with open(EXERCISE_FILE, "r") as f:
        data = json.load(f)  
        f.close()
        return data

# this open and read savedWorkouts.json
def openSavedWorkout():
    with open(SAVED_WORKOUTS, "r") as f:
        data = json.load(f)
        f.close()
        return data

# this saves to savedWorkouts.json
def saveWorkout(muscleGroup, weight, reps, sets):
    now = datetime.now()
    dateString = now.strftime("%Y-%m-%d")
    with open(SAVED_WORKOUTS, "r") as f:
        data = json.load(f)
        
    exerciseData = {
        "Date": dateString,
        "Musclegroup": muscleGroup,
        "Weight": weight,
        "Reps": reps,
        "Sets": sets
    }
    data.insert(0, exerciseData)
    
    with open(EXERCISE_FILE, "w") as f:
        json.dump(data, f, indent=4)
        f.close()
    
def welcomeMsg():
    print("\nWelcome to your Workout Log")
    print("Choose what you want to do\n")
    print("> Workout")
    print("> Progress")
    print("> Quit")
      
def main():
    welcomeMsg()
    
    while True:
        userInput = getInput()
        if userInput[0] == "workout":
            Exercise.runExercise(userInput)
        elif userInput[0] == "progress":
            Exercise.printExerciseList(userInput)
        elif userInput[0] == "quit":
            # TODO: implement autosave
            print("Log is shutting down")
            exit()
        elif userInput[0] == "clear":
            system("clear")
        else:
            print("Error, could not run main")      

if __name__ == "__main__":
     main()
    
main()


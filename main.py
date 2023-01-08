import json
import matplotlib.pyplot as plt
import os
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

    def runExercise():
        data = loadExerciseFile()
        exerciseNumber = {
            "back and bicep": 1,
            "back": 2,
            "chest and tricep": 3,
            "legs and shoulders": 4,
            "legs": 5,  
            "shoulders": 6
        }
        muscleGroups = data.keys()
        
        clear()
        
        print("\nChoose a muscle group: \n")
        for i, muscleGroups in enumerate(muscleGroups):
            print(f"{i+1}) {muscleGroups}")
        
        choice = int(input())
        selectedMuscleGroup = [muscleGroups for muscleGroups, number in exerciseNumber.items() if number == choice][0]
        exercises = data.get(selectedMuscleGroup, [])
        now = datetime.now()
        dateString = now.strftime("%Y-%m-%d")
        dataArray = []
        
        clear()
        
        sets = 0
        
        for exercise in exercises:
            print(f"\nExercise: {exercise['exercise']}")
            exData = {
                "Name": exercise["exercise"],
                "Weight": 0.0,
                "Reps": 0,
                "Sets": 0
            }
            while True:
                weight = float(input("\nEnter weight: "))
                reps = int(input("Enter reps: "))
                
                sets += 1
                
                exData["Weight"] = weight
                exData["Reps"] = reps
                exData["Sets"] = sets
                dataArray.append(exData)
                
                while True:
                    continueExercise = input("\n> Continue exercise? (y/n): ")
                    if continueExercise.lower() == "y":
                        break
                    elif continueExercise.lower() == "n":
                        sets = 0
                        clear()
                        break
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
                if continueExercise.lower() == "n":
                    break
    
            
        dataToSave = {
            "Date": dateString,
            "Exercises": dataArray
        }
        
        with open(SAVED_WORKOUTS, "r") as f:
            newData = json.load(f)
        newData[selectedMuscleGroup].insert(0, dataToSave)
        
        with open(SAVED_WORKOUTS, "w") as f:
            json.dump(newData, f, indent=4)
        
        print("Workout is saved")
        clear()
                
             
def getInput():
    while True:
        userInput = input(": ").lower().split()
        if len(userInput) >= 1:
            return userInput
        else:
            return "Error"


def loadExerciseFile():
    with open(EXERCISE_FILE, "r") as f:
        data = json.load(f)  
        return data


def loadSavedWorkoutFile():
    with open(SAVED_WORKOUTS, "r") as f:
        data = json.load(f)
        return data


def saveWorkoutFile(muscleGroup, exercise, weight, reps, sets):
    now = datetime.now()
    dateString = now.strftime("%Y-%m-%d")
    with open(SAVED_WORKOUTS, "r") as f:
        data = json.load(f)
        
    exerciseData = {
        "Date": dateString,
        "Musclegroup": muscleGroup,
        "Exercise": exercise["exercise"],
        "Weight": weight,
        "Reps": reps,
        "Sets": sets
    }
    data[muscleGroup].insert(0, exerciseData)
    
    with open(SAVED_WORKOUTS, "w") as f:
        json.dump(data, f, indent=4) 


def plotProgress():
    # load the exercise data from the JSON file
    exerciseData = loadSavedWorkoutFile()
    
    # show a list of all muscle groups
    print("\nSelect a muscle group:")
    muscleGroups = list(exerciseData.keys())
    for i, muscleGroup in enumerate(muscleGroups):
        print(f"{i+1}: {muscleGroup}")
    selectedMuscleGroup = muscleGroups[int(input()) - 1]

    # show a list of all exercises
    exerciseNames = []
    for item in exerciseData[selectedMuscleGroup]:
        for ex in item.get("Exercises", []):
            exerciseNames.append(ex["Name"])
    exerciseNames = list(set(exerciseNames))
    print("\nSelect an exercise:")
    for i, exerciseName in enumerate(exerciseNames):
        print(f"{i+1}: {exerciseName}")
    selectedExerciseName = exerciseNames[int(input()) - 1]

    # create a list of all the unique dates
    dates = []
    for sublist in exerciseData.values():
        for item in sublist:
            for ex in item.get("Exercises", []):
                if ex["Name"] == exerciseName:            
                    try:
                        dates.append(item["Date"])
                    except KeyError:
                        pass
    dates = list(set(dates))

    # create a list of reps and weights for the specified exercise
    weights = []
    reps = []
    for musclegroup in exerciseData:
        for item in exerciseData[musclegroup]:
            for ex in item.get('Exercises', []):
                if ex['Name'] == selectedExerciseName:
                    weights.append(ex['Weight'])
                    reps.append(ex['Reps'])
                    break

    if len(dates) == 0:
        print("Error, exercise not found")
        return
    if len(dates) < 2:
        print("Error, not enought data to plot")
        return
    
    # plot the data
    fig, ax = plt.subplots()
    ax.plot(dates, weights, label=selectedExerciseName + " (Weights)")
    ax.plot(dates, reps, label=selectedExerciseName + " (Reps)")
    ax.legend()
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()


def printMenu():
    print("\nWhat you want to do?\n")
    print("> Workout")
    print("> Progress")
    print("> Help")
    print("> Quit")


def printHelp():
    print("\n #1 - If you want to start a new workout, write 'workout' and press enter.")
    print("\n #2 - If you want to see your progress, write 'progress', the musclegroup and press enter.")
    print("      Here is an example: 'progress squats' - then will a graph show up")
    print("\n #3 - If you want to exit the program, write guit and press enter.")   
    print("\n #4 - If you want to clean the teminal, write 'clean' and press enter.")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print("\nWelcome to your Workout Log")
    
    while True:
        printMenu()
        userInput = getInput()
        
        if userInput[0] == "workout":
            Exercise.runExercise()
        elif userInput[0] == "progress":
                plotProgress()
        elif userInput[0] == "help":
            printHelp()
        elif userInput[0] == "quit":
            print("Log is shutting down")
            exit()
        else:
            print("Error, could not valuate input")    
            
      

if __name__ == "__main__":
     main()
    
main()


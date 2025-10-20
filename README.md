# 🥗 Kcal Tracker

A simple **Python-based calorie tracking program** that allows users to log their meals, record the calories for each food item, and view a **tabular summary** of their daily calorie intake.

---

## THE PROBLEM 
Project Goal: The objective is to build a basic Command-Line Interface (CLI) tool using Python that allows a user to quickly log their meals and view a summary of their total and average calorie consumption for the session. 

Problem Statement: Many students and health-conscious individuals lack a simple, fast, and accessible tool to monitor their daily calorie intake

---

## 📜 Features

- Log multiple meals in a day.  
- Add multiple food items under each meal.  
- Automatically records the time when a meal is logged.  
- Displays a clean, tabular summary of all meals and total calories.  
- Input validation to ensure only valid numbers are entered for counts and calories.

---

## CORE LOGIC

### Data Structure
A Python **list of dictionaries** is used to store the structured data for the session.  
Each dictionary represents a single meal and contains its name, a timestamp, and its calculated total calories.

---

### Calculation Logic

- The total calories for a single meal are calculated within the `get_meal_calories()` function.
- The grand total for the day is calculated using a generator expression and the `sum()` function:
  ```python
  sum(meal['calories'] for meal in daily_log)

  ---

## ⚙️ How It Works

1. The program first asks how many meals you want to log.  
2. For each meal:
   - You enter a meal name (e.g., Breakfast, Lunch, Dinner).
   - The current time is recorded automatically.
   - You specify how many food items were in that meal.
   - For each item, you provide its name and calorie count.
3. After all meals are entered, the program prints a **formatted summary table** with:
   - Time of meal  
   - Meal name  
   - Total calories per meal  
   - Grand total calories of the day  

---

## 💻 Example Output

# 1

<img width="706" height="829" alt="image" src="https://github.com/user-attachments/assets/c150ead3-3f85-4bbc-83e1-394fc9373680" />

# 2
<img width="865" height="1739" alt="2ndoutput" src="https://github.com/user-attachments/assets/853ddcc0-c6ee-4dcd-9aa1-7e926b4cfd21" />



# 3
<img width="957" height="2053" alt="output 333" src="https://github.com/user-attachments/assets/1da73255-37df-47b4-85ce-9c10d8f1c761" />




## 🪄 Future Improvements

- Save daily logs to a file (CSV)

- Add calorie goals and progress tracking.

- Option to delete or edit meals.

- GUI version using Tkinter or PyQt.






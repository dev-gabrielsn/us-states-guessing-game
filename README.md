# 🗺️ U.S. States Guessing Game

An interactive Python guessing game where users try to identify all 50 U.S. states.  
As correct answers are entered, the state names are displayed directly on a graphical map of the United States.

This project focuses on combining **data handling**, **user interaction**, and **basic graphical interfaces** using Python.

---
<p align="center">
  <img src="https://github.com/user-attachments/assets/1228c21e-b7d4-424d-9841-4a3e35088203" alt="us-states-gif">
</p>   

## 🎯 Project Purpose

The goal of this project is to practice and demonstrate:

- Python programming fundamentals
- Working with CSV files using Pandas
- Building simple graphical applications with Turtle
- User input validation and game state tracking
- Data persistence through file generation

---

## 🧠 How It Works

1. A blank map of the United States is displayed on the screen.
2. The user types the name of a U.S. state.
3. If the answer is correct:
   - The state name appears at the correct location on the map
   - The score counter is updated
4. The game continues until:
   - The user types **Exit**, or
   - All 50 states are correctly guessed
5. When exiting the game, a CSV file is automatically generated containing the states that were not guessed.

## 📁 Project Structure
  
us-states-guessing-game/  
│   
├── main.py # Main game logic  
├── 50_states.csv # Dataset with state names and coordinates  
├── blank_states_img.gif # Blank U.S. map image  
├── States_to_learn.csv # Generated file with missing states  
└── README.md  

---

## 🛠️ Technologies Used

- **Python 3**
- **Pandas** – for CSV data handling
- **Turtle Graphics** – for the graphical interface

---

## ▶️ How to Run the Project

1. Make sure Python 3 is installed on your system.
2. Install the required dependency:
   pip install pandas
3. Run the application:
   python main.py

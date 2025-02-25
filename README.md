# Student Progression Outcome Predictor

## Overview
This Python program predicts student progression outcomes at the end of an academic year based on the number of credits achieved in the pass, defer, and fail categories. The program validates inputs, classifies students into different progression categories, and provides a graphical histogram representation using the `graphics.py` library.

## Features
- **User Input Validation:** Ensures correct credit values and total credits sum up to 120.
- **Progression Classification:** Determines if a student:
  - Progresses
  - Is a module trailer
  - Retrieves modules
  - Is excluded
- **Two Modes:**
  - **Student Mode:** Allows a single student to check their progression outcome.
  - **Teacher Mode:** Enables entry of multiple student records and generates a histogram.
- **Data Storage:** Saves student outcomes to `progression_data(student&staff).txt`.
- **Graphical Representation:** Displays a histogram of student outcomes using `graphics.py`.

## Installation
Ensure Python is installed and install any required libraries if not already available:
```
pip install tkinter
```

## How to Use
### Running the Program
1. Execute the Python script:
   ```
   python w2051623_student_and_staff_(PART 1,2,3).py
   ```
2. Choose a mode:
   - Enter "S" for **Student Mode** to check a single outcome.
   - Enter "T" for **Teacher Mode** to input multiple student records and generate a histogram.

### Example Input & Output
#### Student Mode:
```
Enter your Credits at pass: 100
Enter your Credits at defer: 20
Enter your Credits at fail: 0
-Progress Module Trailer-
```
#### Teacher Mode:
```
Please enter your Credits at pass: 80
Please enter your Credits at defer: 20
Please enter your Credits at fail: 20
-Do not Progress(module retriever)-
```
At the end, a histogram is displayed showing the number of students in each category.

## File Structure
- `w2051623_student_and_staff_(PART 1,2,3).py`: Main program script.
- `graphics.py`: Graphics library for histogram visualization.
- `progression_data(student&staff).txt`: Stores student progression data.

## License
This project is open-source and free to use.


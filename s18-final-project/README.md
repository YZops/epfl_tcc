# MY FINAL PROJECT
A one or two sentence description of your project here.

- What does it do?  
  This is a "Money Saving App". All savings can be added in the app.
  For example: When you buy something at the supermarket, you can see how much you have saved at the checkout or on the receipt. This information can be added in the app.
  You can see how much money you have saved over a period of time.

- What is the "new feature" which you have implemented that we haven't seen before?  
  - Deleting entries from a database textfile with a more complex datastructure.
  - Working with Dates in Python and JavaScript.
  - More complex server-side checks of user input with regex -> Used Tool for testing: https://regex101.com/
  - More extensive use of the Flask framework with multi request handling and render_template and a better file structure. Thanks to this guy who explained Flask in more detail: https://www.youtube.com/watch?v=lIGKKnfLobA
  - General: More detailed success and error messages and better user experience.

## Prerequisites
Did you add any additional modules that someone needs to install (for instance anything in Python that you `pip install-ed`)? 
List those here (if any).
- No additional modules added that require installation.

## Project Checklist
- [x] It is available on GitHub.
- [x] It uses the Flask web framework.
- [x] It uses at least one module from the Python Standard Library other than the random module.
  Please provide the name of the module you are using in your app.
  - Module name: datetime, re
- [x] It contains at least one class written by you that has both properties and methods. It uses `__init__()` to let the class initialize the object's attributes (note that  `__init__()` doesn't count as a method). This includes instantiating the class and using the methods in your app. Please provide below the file name and the line number(s) of at least one example of a class definition in your code as well as the names of two properties and two methods.
  - File name for the class definition: moneysavingapp.py
  - Line number(s) for the class definition: 14
  - Name of two properties: store_name, store_type
  - Name of two methods: add_store, remove_store
  - File name and line numbers where the methods are used: moneysavingapp.py, add_store: 376, remove_store: 411
- [x] It makes use of JavaScript in the front end and uses the localStorage of the web browser. Please provide the file name and line number(s) where the localStorage is used.
  - script.js, line: 8-11, 16, 34. index.html, line: 17
- [x] It uses modern JavaScript (for example, let and const rather than var).
- [x] It makes use of the reading and writing to the same file feature.
- [x] It contains conditional statements. Please provide below the file name and the line number(s) of at least
  one example of a conditional statement in your code.
  - File name: moneysavingapp.py
  - Line number(s): 25, 41, 75...
  - File name: index.html
  - Line number(s): 9-13
  - File name: script.js
  - Line number(s): 14-35
- [x] It contains loops. Please provide below the file name and the line number(s) of at least
  one example of a loop in your code.
  - File name: moneysavingapp.py
  - Line number(s): 76, 86, 99...
- [x] It lets the user enter a value in a text box at some point.
  This value is received and processed by your back end Python code.
- [x] It doesn't generate any error message even if the user enters a wrong input.
- [x] It is styled using your own CSS.
- [x] The code follows the code and style conventions as introduced in the course, is fully documented using comments and doesn't contain unused or experimental code. 
  In particular, the code should not use `print()` or `console.log()` for any information the app user should see. Instead, all user feedback needs to be visible in the browser.  
- [x] All exercises have been completed as per the requirements and pushed to the respective GitHub repository.

## **Academic Integrity and Learning Statement**

By submitting my work, I confirm that:

- The code, analysis, and documentation in this notebook are my own work and reflect my own understanding.
- I am prepared to explain all code and analysis included in this submission.


If I used assistance (e.g., AI tools, tutors, or other resources), I have:

- Clearly documented where and how external tools or resources were used in my solution.
- Included a copy of the interaction (e.g., AI conversation or tutoring notes) in an appendix.

I acknowledge that:

- I may be asked to explain any part of my code or analysis during evaluation.
- Misrepresenting assisted work as my own constitutes academic dishonesty and undermines my learning.
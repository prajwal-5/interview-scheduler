# Interview Scheduler Project

### This is a single page interview scheduling application powered by Django as backend and uses SQLite3 database for development and demonstrates Many to many relationship between interview and participant table. It also takes care of cases of multiple scheduled interviews and the correct set of participants selected at the correct time while editing too. 

### HOME VIEW: ![Home page image](resources/home.PNG)

### Case 01: Creating and Interview:

1. Enter Details:
    ![Form filling image](resources/entering-details.PNG) 

2. Interview Scheduled:
    ![Interview created image](resources/interview-created.PNG)


### Case 02: Try to Schedule an interview where atleast one of the participant is not available in that time slot:

1. Enter Details:
    ![Form filling image](resources/case-2-details.PNG) 

2. Error Message from backend:
    ![Error message image](resources/case-2-response.PNG)


### Case 03: Try to edit with wrong credentials:

1. Wrong set of people (not having at least one interviewr and one candidate):
    ![error message image](resources/case-3.PNG) 

2. Wrong timing of selected people:
    ![error message image](resources/case-4.PNG)



### Case 04: Checking link:

1. Enter Details:
    ![Form filling image](resources/link-details.PNG) 

2. Interview check result:
    ![Resultant message](resources/link-message.PNG)


## Admin Section of the Web App:

### Admin panel:
![admin panel image](resources/admin-panel.PNG) 

### Interview table:
1. Interview table:
![interview table image](resources/interview-table.PNG) 

2. Interview table details:
![interview table details](resources/interview-details.PNG)

### Participant table:
1. Participant table:
![participant table image](resources/participant-table.PNG) 

2. Participant table details:
![participant table details](resources/participant-details.PNG)


Hope you like it. Suggestions are welcome.
# TimeTableTuner

## a simple flask app that:
- cleans an excel file's sheet
- creates json file named as `jsontt_division_number.json`
  - the division number is given from users when they click on the division button
- sends the cleaned data into these json files
- prints the correct class and other info onto the html
  - if no class is currently running it would relevant response that is either classes have not started or they ended already 
![image](https://user-images.githubusercontent.com/76813100/220707536-8ec932d1-9511-412a-b528-775a06e40c2a.png)




## usage:

- make sure you have python and pip installed.
- run the setup.sh file
- open the /app/ folder in the terminal
- run the command `flask run` to deploy the app onto the localhost or use `--host=0.0.0.0` with the command to deploy into your network

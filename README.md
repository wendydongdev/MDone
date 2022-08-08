# MDone

MDone is a group task management + synchronization system for students.

#Specical note
This project was running a few days ago, and I haven't run it successfully since I switched to a cloud-based server. After my blind change, I'm not sure how much of it is left to run. You can check my github page to see the latest version.

#Giuhub
[wendydongdev/MDone] (https://github.com/wendydongdev/MDone)

# Features

Register and login to your account. Add tasks, join tasks. Sync task status to Gmail.
Features that will be developed in the future: task deadline reminders. Task completion analysis.

# Development Notes

The current system is in MVC style. Use the obeserver pattern to observe the task change status. Notifications will be sent to users as the tasks they subscribe to change in status. Different task states have different methods, so the state pattern is used.

My biggest challenge at the moment is that the code of many different functions are wrapped together, which does not meet the requirement of simplicity. But the volume of the software is not too big, so I feel that splitting it will increase the complexity. I'm working on adding new features.

## Installation

run the following command when you open the application folder and then redirect to page "http://127.0.0.1:5000/index"

```bash
flask run 
```

# Credit
frame work: [Flask](https://flask.palletsprojects.com/en/2.2.x/)

css layout : [Paper-Dashboard](https://github.com/creativetimofficial/paper-dashboard)

email validating API: [Company URL Finder](https://companyurlfinder.com/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
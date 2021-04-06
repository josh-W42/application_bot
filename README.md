# ApplicationBot 🥷🏽
This is a bot that manages job applications

1. *Fork* and *clone* this repo
2. Create a **Project** board called *Job Applications*
3. You need to select the *Basic Kanban* template after doing step 2.
4. Be sure to have 3 columns: `To do`, `In Progress`, `Done`

Add a `.env` file and put the following inside:
```text
GITHUB_USERNAME=username
GITHUB_PASSWORD=password
```

When you complete an application during the job search, run the following command:
```text
python3 app.py
```
The terminal (app) will prompt you for three questions:
```text
Enter the name of the company: Facebook Inc
Enter the title of the job: Internal Software Engineer
Enter the link of the application: https: https://www.facebook.com/careers/v2/jobs/186900152946376/
```
Then the app will make a job card for each application.

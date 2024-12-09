# CSC-3155-Group-Project

Description:
  Chrome extension that connects to the Chrome browser that is able to track jobs to make sure that they are not fake job postings.  
  It uses an algorithm to track jobs to make sure that they fail to meet requirements of a fake job based on the criteria that     
  Indeed.com has posted which are the following:

    1) Company is clear about the post being a "job opening" or "job posting". 
    2) Company requiring payment in order to get the job.
    3) False promises of high wealth aquisition and unrealistic high wage start ups.
    4) Unprofessional Communication in the job description.
    5) Contact information for the company or employer doesn't exist.


Technologies used (Before changes):
  Frontend: HTML, Javascript
  Backend: FastAPI, Python

Technologies used (After changes):
  Frontend: HTML, Javascript, CSS
  Backend: Python, Django Framework, SQL

Sprint 0: Nov 4 - Nov 8

Working on implementing some pages using Javascript and HTML.
Still figuring out how to implement the backend in order to make sure that the email verification system works.
Working on making sure that the filter system also is meeting our requiprements but not familiar enough with how to make it work.

Spring 1: Nov 11 - Nov 15

Transition project from Javascript into Python to meet with class expectations.
Fixing some of the sites so that it transitions into HTML
Working on backend using Django Framework from the tutorial.

Sprint 2: November 16 - November 31
Finish implementing test cases for the project
Making sure that the project runs and the test data is properly compiling.
Publish final project

=======
--> Move into the directory where we have the project files : 


```bash
cd CSC-3155-Group-Project

```

--> Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

```

--> Activate the virtual environment :
```bash
envname\scripts\activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

#

### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

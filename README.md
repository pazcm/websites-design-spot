[![Build Status](https://travis-ci.com/pazcm/websites-design-spot.svg?branch=master)](https://travis-ci.com/pazcm/websites-design-spot)

# Websites Design Spot

In this Django project, I built a full-stack website based around web development services business, where the work of the company is displayed to potential customers and public in general.
I setup an authentication system and a contact page, so users and company's staff are able to interact with each other to suit their goals.
 
## UX
 
The design thinking approach of this site started writing the user stories to learn about the needs of the future users, as well as the requirements and needs of
the owner of the site, in this case a web development company. Next to this, I created the wireframes, that depict the layouts for the main pages and their responsive views, to have an idea about how to allocate the content and the possible behaviours of the functionalities that will be available.

The site allows users to explore different designs and communicate their goals with the company via contact page, to order a specific web design and pay for the development of it. The compamny is able to logging as admin in the backend of the site and manage the orders and users through an administrator panel and create, update and delete the web designs and details that will be showcased along the site.

- **User stories** and **wireframes** created and followed for the project can be found [here](https://github.com/pazcm/websites-design-spot/tree/master/static/mockups).

## Features
### Existing Features
- Home/
  - Welcome block and Gallery of images showcasing the work of the company

- Main Navigation/
  - Allows users to navigate in a simple and intuitive way widesite which makes easy to find the content available and move along the site with fluency.

- Search box/
  - Allows users to find quickly designs by looking for a keyword.

- Categories/
  - Users can filter designs by category to get specific designs for their needs.

- Contact/
  - Provide information to the users and a form to contact with the company.

- Footer/
  - Give information About the company, Services links, Social links.

- Authentication: Registration (Sign up) and Log in / Log out /
  - Users can register in the site, once their are authenticated they are able to order and pay for a design.

- Cart/
  - Authenticated users have access to a cart page where they can edit their selections and checkout.

- Payment
  - Allows Authenticted users to have information about their orders and make a payment.

### Features Left to Implement
-  TBC ...

## Technologies Used

- [Git/GitHub](https://github.com)
    - The project uses Git version control to manage and track the changes in the code.

- [Balsamiq_Cloud](https://balsamiq.com/wireframes/cloud/)
    - The wireframes for the project were created using Balsamiq GUI wireframe builder cloud application.

- [Visual_Studio_IDE](https://visualstudio.microsoft.com/)
    - The project uses an Visual Studio IDE for development.

- [Python](https://www.python.org/)
    - The project uses Python BE framework to create the app alongs with the Python templates' engine [Jinja2](http://jinja.pocoo.org/) for the structure.

- [Bootstrap](https://getbootstrap.com/)
    - The project uses Bootstrap as a responsive FE framework taking advantage of some default stylings and components.

- [CSS3](https://www.w3.org/Style/CSS/)
    - The project uses CSS3 to create custom style.

- [JQuery](https://jquery.com)
    - The project uses JQuery to initialize some site elements and components.

- [Font_Awesome](https://fontawesome.com/)
    - The project uses Fontawesome javascript to get the Social Icons widesite.

- [Travis](https://travis-ci.org/)
    - The project uses Travis service for Continuous Integration testing.

- [AWS](https://signin.aws.amazon.com/)
    - The project uses AWS cloud server for serve the static files.

- [Stripe](https://stripe.com/ie)
    - The project uses Stripe platform to accept payments from the website.

- [Heroku](https://www.heroku.com/home)
    - The project uses the hosting platform Heroku to deploy and run the app.


## Testing

During the development I drove constantly manual testing for checking work functionalities and behaviours as well as I continuosly used several devices emulators with different screen sizes for Responsive testing; such as Nexus 5X, Nexus 10, Galaxy S5, iPhone 6/7/8, iPhone 6/7/8 Plus, iPhone X, iPad and iPad Pro,...
In addition, I crossbrowser testing the site in Firefox and Safari browsers using developer tools.
[incluir tabla]


Travis .- I used this service by automatically building and testing small code changes

[incluir Test case:]

Automate test (explain approach + link to the test and how to run)


- - HTML was validated using the Markup Validation Service provided by The World Wide Web Consortium: https://validator.w3.org/

- - CSS was validated using the CSS Validation Service provided by The World Wide Web Consortium: https://jigsaw.w3.org/css-validator/

Bugs/Issues ...


## Deployment

To **Setup my virtual local environment**,  I installed [Django](https://www.djangoproject.com/) v1.11.17 and created [GitHub repo](https://github.com/pazcm/websites-design-spot). The steps that I went after were the following:

1. `brew update`

2. `xcode-select --install`

3. `brew install python3`

4. install Pip package management system -> `sudo easy_install pip`

5. install virtualenv for python -> `sudo pip install virtualenv`

6. create a project folder -> `mkdir websites-design-spot`

7. then inside the project folder, create the virtual env -> `python3.7 -m venv vE0`

8. activate it to install the required project packages -> `source vE0/bin/activate` ~ shorthand `. vE0/bin/activate` || to exit (vE0) use : `deactivate`

9. use pip to install the package django ('vE0'activate):
  - `sudo pip install django==1.11.17`
  - `pip list`

10. in root directory add requirements file -> `pip freeze > requirements.txt`

11. `django-admin startproject <website_design_spot>`

12. inside the repo to run the dev server -> `python3.7 manage.py runserver`

13. `http://127.0.0.1:8000/`



Then:

1. I created a [Travis](https://travis-ci.org/) account and **.travis.yml** file at the top level of the project (with language, version, install and a dummy secret key) for Continuous Integration so it will run tests on my code every time it is pushed to GitHub. It is connected to my GitHub account.

2. I added **Procfile** => `webgunicorn websites_design_spot.wsgi:application` at the same level that manage.py.

3. I run the app in the local environment to make sure everything is in order with the Procfile and the Requirements file before try to deploy.

4. In **settings.py** file, I updated the ALLOWED_HOSTS variable from an empty list to `ALLOWED_HOSTS = ['127.0.0.1', 'websites-design-spot.herokuapp.com']`.

5. I Pushed the changes from Git to GitHub.

6. I login to [Heroku](https://www.heroku.com/home) platform and 'Create a new app' via the dashboard. It provided a cloud Postgres database.

7. In Heroku dashboard settings, I configured the variables for AWS, DataBase and Stripe.

8. I **'Deploy Branch'** and **'Open app'** from Heroku dashboard => [Website](https://websites-design-spot.herokuapp.com/)



## Credits / Resources
TBC ...

- https://towardsdatascience.com/virtual-environments-104c62d48c54

- https://www.freecodecamp.org/news/manage-multiple-python-versions-and-virtual-environments-venv-pyenv-pyvenv-a29fb00c296f/

- https://medium.com/agatha-codes/9-straightforward-steps-for-deploying-your-django-app-with-heroku-82b952652fb4










### Media
- The photos used in this site were obtained from the Web for testing/studying propositus, not for production or comercial uses.

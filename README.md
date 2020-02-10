[![Build Status](https://travis-ci.com/pazcm/websites-design-spot.svg?branch=master)](https://travis-ci.com/pazcm/websites-design-spot)

# Websites Design Spot

In this Django project, I built a full-stack website based around web development services business, where the work of the company is displayed to potential customers and public in general.
I setup an authentication system and a contact page, so users and company's staff are able to interact with each other to suit their goals.
 
## UX
 
The design thinking approach of this site started writing the user stories to learn about the needs of the future users, as well as the requirements and needs of
the owner of the site, in this case a web development company. Next to this, I created the wireframes, that depict the layouts for the main pages, responsive views, to have an idea about how to allocate the content, the functionalities that will be available and the possible behaviours.

The site allows users to explore different designs and communicate their goals with the company via contact page, to order a specific web design and pay for the development of it. The compamny is able to logging as admin in the backend of the site and manage the orders and users through an administrator panel and create, update and delete the web designs details that will be showcased along the site.

[user_stories]
[wireframes]

## Features
### Existing Features
- Home
Welcome block and Gallery of images showcasing the work of the company

Main Navigation
allows users ... Simple and intuitive Navigation bar widesite which makes easy to find the content available and navigate with fluency.

Search box
Allows users to find quickly designs by using a keyword.

Categories
Users can filter designs by category to get specific designs for their needs.

Contact
Provide information to the users and a form to contact with the company.

Footer
About the company, Services links, Social links

Authentication: Registration (Sign up) Log in / Log out
Users can register in the site, once their are authenticated they are able to order and pay for a design.

Cart
Authenticated users have access to a cart page where they can edit their selections and checkout.

Payment
Allows Authenticted users to have information about their order and make a payment

### Features Left to Implement
-  ...

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [Git/GitHub]
    - The project uses Git version control to manage and track the changes in the code.

- [Balsamiq_Cloud]
    - The wireframes for the project were created using Balsamiq GUI wireframe builder cloud application.

- [Visual_Studio_IDE]
    - The project uses an Visual Studio IDE for development.

- [Python]
    - The project uses Python BE framework to create the app alongs with the Python templates' engine [Jinja2](http://jinja.pocoo.org/) for the structure.

- [Bootstrap]
    - The project uses Bootstrap as a responsive FE framework taking advantage of some default stylings and components.

- [CSS3]
    - The project uses CSS3 to create custom style.

- [JQuery]
    - The project uses JQuery to initialize some site elements and components.

- [Font_Awesome]
    - The project uses Fontawesome javascript to get the Social Icons widesite.

- [Travis]
    - The project uses Travis service for Continuous Integration testing.

- [AWS]
    - The project uses AWS cloud server for serve the static files.

- [Stripe]
    - The project uses Stripe platform to accept payments from the website.

- [Heroku]
    - The project uses the hosting platform Heroku to deploy and run the app.


## Testing

During the development I drove constantly manual testing for checking work functionalities and behaviours as well as I continuosly used several devices emulators with different screen sizes for Responsive testing; such as Nexus 5X, Nexus 10, Galaxy S5, iPhone 6/7/8, iPhone 6/7/8 Plus, iPhone X, iPad and iPad Pro,...
In addition, I crossbrowser testing the site in Firefox and Safari browsers using developer tools.
[incluir tabla]


Travis .- I used this service by automatically building and testing small code changes

[incluir Test case:]

Automate test (explain approach + link to the test and how to run)
https://docs.djangoproject.com/en/3.0/topics/testing/overview/#running-tests
https://www.youtube.com/watch?v=IaiMDO88mpg&list=PL4652EHGfSYgTJxZoP8cffouScRLFB8A3&index=5&t=0s


HTML was validated using the Markup Validation Service provided by The World Wide Web Consortium: https://validator.w3.org/
CSS was validated using the CSS Validation Service provided by The World Wide Web Consortium: https://jigsaw.w3.org/css-validator/

Bugs/Issues ...


## Deployment

First I installed Django, created [github repo](https://github.com/pazcm/websites-design-spot) and created Travis account.

For **setup my local environment**, the steps that I went after were the following:

<blockquote class="trello-card"><a href="https://trello.com/c/iicb3wrA/213-setup-local-environment">setup local environment</a></blockquote><script src="https://p.trellocdn.com/embed.min.js"></script>

- I created .travis.yml file at the top level of the project (with language, version, install and a dummy secret key) for [Travis](https://travis-ci.org/) Continuous Integration.

Then:
I added requiremntes.txt and Procfile at the same level directory that manage.py.
Procfile => webgunicorn websites_design_spot.wsgi:application

- I run the app in the local environment to make sure everything is in order with the Procfile and the requirements file locally before try to deploy.

In *settings.py* file, I updated the ALLOWED_HOSTS variable from an empty list to `ALLOWED_HOSTS = ['127.0.0.1', 'websites-design-spot.herokuapp.com']`.

I Pushed the changes from Git to GitHub.

- I login to [Heroku](https://www.heroku.com/home) platform and 'Create a new app' via the dashboard. It provided a cloud Postgres database.

In Heroku dashboard settings tab, I configured the variables for AWS, DataBase and Stripe.

I 'Deploy Branch' and 'Open app' from Heroku dashboard => [website](https://websites-design-spot.herokuapp.com/)



## Credits


### Media
- The photos used in this site were obtained from the Web for testing/studying propositus, not for production or comercial uses.

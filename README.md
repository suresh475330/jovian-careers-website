# Make-careers-website

## Run app

* git clone <url>
* Go to project folder create a vertual env in project
* Activate the vertual env
* Run pip install -r requirements.txt
* Run flask run or gunicorn app:app

## .env config

* Go To your planatScale platform and get the mysql database connection string to added to dbString
* Enter your email in MAIL_USERNAME
* Go to your gmail app password section and generate a new app password 16 letter and enter in MAIL_PASSWORD
* Go To hCaptcha website and register a account get a HCAPTCHA_SITE_KEY and  HCAPTCHA_SECRET_KEY

```bash
    dbString="mysql+<drivername>://<username>:<password>@<server>:<port>/dbname"

    MAIL_USERNAME="yourGmail@gmail.com"
    MAIL_PASSWORD="your gmail app password"
    
    HCAPTCHA_SITE_KEY="your-site-key"
    HCAPTCHA_SECRET_KEY="your-secret-key"
```

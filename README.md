# Labs DS template

[Docs](https://docs.labs.lambdaschool.com/data-science/)


pipenv install joblib
pipenv install sklearn

to run locally
uvicorn app.main:app --reload

to deploy to aws elastic beanstalk

 eb init --platform docker --region us-east-1 group-ja07
 eb create --region us-east-1 group-ja07
 eb open
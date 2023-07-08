cd "C:\bot_you_do"
git init
heroku git:remote -a youdobot
git add .
git commit -am "make it better"
git push heroku main
@ECHO OFF
cd ../
set /P test="Commit Info: "
set commit="%test%" 
git add *
git commit -m "%commit%" 
git push --set-upstream origin master
echo Update Pushed!
echo Check for commit on github!
pause
all the Python script
python3 ./collectCIDRList.py

# Get the current date in the format "year/month/day"
commit_date=$(date +%Y/%m/%d)

# add to git
git add .

# Commit the changes with the date as the message
git commit -m "$commit_date"

#push to github
git push -uf origin main



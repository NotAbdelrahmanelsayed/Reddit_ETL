# Clone the repo or update local changes
git pull origin main

# Switch to  the base branch of pull request
git checkout main

# merge the head into the base branch
git merge actions/black

# push the changes 
git push -u origin main
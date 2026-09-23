#Repos
python --version or py --version

#To see the online list of actual Python versions
py list --online 

#Install the latest Python 3 version
py install --configure
py install 3

#to create a virtual environment named .venv
python -m venv .venv 

#to navigate to the root of your C drive and create the repos folder
cd C:\ && mkdir repos && cd repos

git clone https://github.com/shrutisey-gif/Repos.git

cd YOUR-REPOSITORY-NAME

#Configure your Git Identity (First-Time Only)
git config --global user.name "Your GitHub Username"
git config --global user.email "your-email@example.com"

#Check your repository status
git status

#Stage your files
git add .          #The dot . means "add everything in the current directory"

git commit -m "Complete Project 1: Python fundamentals and OS library scripts"

git push origin dev



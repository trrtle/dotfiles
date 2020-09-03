# pyenv
export PATH="/home/turtle/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# Virtualenvwrapper
export WORKON_HOME=/var/lib/virtualenv
export PROJECT_HOME=$HOME/Devel
source /home/turtle/.pyenv/versions/3.8.5/bin/virtualenvwrapper.sh



echo 'Setting up virtualenv...'
virtualenv -p $(which python3) .venv
source .venv/bin/activate

echo 'Installing requirements...'
pip3 install -r ./requirements.txt
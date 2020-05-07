# bee-racers

## Installation
### Requirements
Python 3.8

### Building
Building is not necessary. Beeracers comes with a distribution folder (dist) which contains a wheel that allows you to quickly install the game using pip. If you would like to build the project anyway, navigate to your copy of the repo in the commandline and run the following commands:
```
pip install setuptools wheel
python setup.py bdist_wheel
```

### Installing
Navigate to where your wheel is stored (default: bee-racers/dist) and run:
```
pip install <filename>.whl
```
The default filename is: `bee_racers-0.0.1-py3-none-any.whl`

## Playing the Game
### Launching
The game can be launched anywhere on your machine by opening a commandline and entering:
```
python -m beeracer
```
### Chosing an Assembly File
When the game first loads, a file menu will open up. This is to allow you to choose your own assembly file. You can exit it without picking something to have the game default to the `basicbee` assembly AI.
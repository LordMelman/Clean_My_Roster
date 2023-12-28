# Clean My Roster!!!
This script can be utilized to reformat standard BattleScribe roster .html files to add a few convenience features and reduce scrolling

## Dependencies

### python3
https://realpython.com/installing-python/#how-to-install-python-on-windows

### Beautiful Soup package
In a command prompt run the following command:
```
pip install beautifulsoup4 
```

## Running the Script

1. Open a command prompt in the Roster_Rework directory
2. Run the following command:
```
python Roster_Rework.py
```
3. When prompted, enter the path to the roster .html file you'd like reformatted and press *enter*
4. The reformatted file will appear as rostername_reformated.html
5. double-click the _reformated.html file to open in your web browser

## Roster Features

### Collapsable Units
Click a unit's name to expand/collapse its stats and features

### Removable Units
Remove a unit after death by clicking its associated "remove" button
(To bring back removed units, refresh the page)

### Group Leaders w Followers (COMING SOON)
Make Leaders and the units they're leading appear side-by-side in the roster

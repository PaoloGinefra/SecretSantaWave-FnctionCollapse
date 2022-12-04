# Secret Santa matching using Wave Function Collapse
With this script you can generate Secret Santa matches taking into account everybody's preferences.
All you need to do is constructing the adjacency Matrix of your preferences and call the $findMatches$ function. It will return an array of matches $Matches$ such that the i-th person will have to give a present to the $Matches[i]$-th person 
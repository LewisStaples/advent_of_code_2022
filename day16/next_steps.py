"""
Do brute force for all paths that may be followed by player one

Do brute force for all possible paths that my be followed by player two
	player one's chosen both narrows the choices for player two
	
Use memoization to track prior states, tracking
	Elapsed time
	Valve states
		Convert the list of open valves into a single int value
        sample:  open_valves = {'BB': 2, 'JJ': 3, 'CC': 4, 'DD': 7, 'EE': 9, 'HH': 13}
            For each index (valve ID), look up the index in NONZERO_VALVES
            The NONZERO_VALVES index has a known upper limit (the number of valves)
            The value in open_valves has an upper limit (TIME_LIMIT)
            
	Positions of both players (note players are indistinguishable)
		Include case where player two hasn't started yet
"""




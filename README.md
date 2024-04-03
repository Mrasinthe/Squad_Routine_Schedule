# Squad_Routine_Schedule-
 Python 3 Program

Background:

In the army, a camp of soldiers must submit 2 schedules every night:
1) Patrols (to keep civilians away and the camp secured)
2) "Stove-watch"  - To keep the fire going during the night for every tent (squad). 
Those schedules are sometimes somewhat complicated as it must be taken into account that car drivers are required to have 6 hours of consecutive sleep, and schedules should be optimized for everyone in a similar way, the more consecutive hours of sleep the better. 
Specifications:
Patrols are usually divided equally among squads, so if there is 6 hours of patrol and 2 squads, both do 3 hours. A patrol consists of 2 people. 
Some rules:
•	Stove-watch is separate for each squad and the post must be manned the entire night routine.
•	Patrol is shared between squads but must include 2 members of the same squad. 
•	In the current setting, a squad consists a minimum of 5 and a maximum of 12 members. Every squad has 0 to 2 drivers, but there must at least two drivers for the set of squads.
•	Drivers are required to have 6 hours of consecutive sleep time.
•	No person should be "on-duty" more than 2-3 (maybe 4) hours unless necessary. The more equally among divided among the squad, the better.
Main task:
Build a program as described above using Python 3. Feel free to use any libraries, but consider that fewer dependencies are better.
1)	Have the program accept the following input:
o	Squad line-ups, consisting of multiple squads
	Every soldier has a parameter that indicates if he/she is a driver or not
o	The total length of the patrol routine (i.e 20:00 to 06:00)
o	It must be possible to give the input to the program in two ways:
	From a text file provided via an argument:
•	The first line of the file contains the timeframe of the patrol (i.e 20:00 - 06:00). 
•	Each next line consists of one rank, name and designation (driver or not) and an empty line denotes a different squad i.e squads are seperated by an empty line.
	If no file is provided as an argument, the program must ask the user for the input via command line.
2)	Have the program return a nightly routine schedule as output on the screen and ask the user if they want to save the output as a file. The output must be formatted in JSON, similar to a REST API response in a readable manner. 
EXAMPLE
20:00 to 06:00 
(SQUAD #1)	(SQUAD #2)
Sgt. Boomer	Sgt. Ferretti
Sgt. Athena	Sgt. Kawalsky
Pvt. Starbuck (Driver)	Pvt. Raynolds
Pvt. Apollo (Driver)	Pvt. Siler (Driver)
Pvt. Zac	Pvt Pierce 
Pvt. Tigh	Pvt. Makepeace

SQUAD #1 TIMETABLE		
Time	Stove-Watch	Patrol
22:00	Sgt Boomer	Pvt. Starbuck (Driver), Pvt. Apollo (Driver)
23:00	Sgt Boomer	Pvt. Starbuck (Driver), Pvt. Apollo (Driver)
0:00	Sgt. Athena	Pvt. Zac, Pvt. Tigh
1:00	Sgt. Athena	Pvt. Zac, Pvt. Tigh
2:00	Pvt. Zac	-
3:00	Pvt. Zac	-
4:00	Pvt. Tigh	-
5:00	Pvt. Tigh	-
		
SQUAD #2 TIMETABLE		
Time	Stove-Watch	Patrol
22:00	Sgt. Ferretti	-
23:00	Sgt. Ferretti	-
0:00	Sgt. Kawalsky	-
1:00	Sgt. Kawalsky	-
2:00	Pvt. Raynolds	Sgt. Ferretti / Sgt. Kawalsky
3:00	Pvt. Raynolds	Sgt. Ferretti / Sgt. Kawalsky
4:00	Pvt. Makepeace	Pvt. Siler (Driver), Pvt Pierce (Driver)
5:00	Pvt. Makepeace	Pvt. Siler (Driver), Pvt Pierce (Driver)
 


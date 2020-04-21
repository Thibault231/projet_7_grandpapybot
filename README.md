# Projet_7_GrandpapyBot
										Projet_7_GrandpapyBot
								Créez GrandPy Bot, le papy-robot
								 OpenClassroom's project number 7
										
     Flask_Ajax_Heroku                           

SUM UP: 
	Projet_7_GrandpapyBot is a school project program answering geographical questions in using Flask framework.
	Once running the run.py a "get" request is send to the programme displaying a front interface on the web browser.
	After completing and validating the web formular a "post" request is send to the programm wich clean the datas and call Googlemap's
	and Wikipedia's API's to contruct a correct answer.
	The answer is then return to the front part and prettyly displayed by javascript.
	This programme is also deployed on heroku. 

	In  Projet_7_GrandpapyBot te user have first to connect to https://projet-grandpapybot.herokuapp.com.
		-Then ask a question to Papy Bot in the question area.
		-Click on "soumettre ma question" or press "entry".
		-Consult the thre answer.

	The answer is composed of three parts:
	-The adress.
	-The GoogleMap map with marker for indicating the location.
	-The Papy Bot story about the adress.

	The question is also stock in an history log under le formular, for the session only.
	There is no save fonction in this program.

	Settings:
	Settings are contained in the file "requirement.txt".

	Running program:
	For running this program on the web connect to https://projet-grandpapybot.herokuapp.com. 

	For running it localy, install the requirements.txt settings.
	A GoogleMap's API key is also requiered. Get it on https://developers.google.com/maps/documentation/maps-static/get-api-key?hl=fr
	Open the file config.py and insert your GoogleMap's key in the line 6. replace "Your GOOGLEMAP's API KEY" by your key.
	Then run the file "run.py" to start the program.
	The client side is being displayed at port:5000.

AUTHOR:
T.Salgues.

LICENCE:
Projet_7_GrandpapyBot is a public project without any licence.

CONVENTIONS:
	Python code:
		Python code respect the PEP8 convention.
		Each class have its file.
		
		For docstring apply the following field
		"""" <Description>
		<Arguments>
			Arg 1: type (default value, description)
			Arg 2: type (default value, description)
			...
		<Return>
			Return 1: type (default value, description)
			Return 2: type (default value, description)
			...
		<Example>
		"""

CONTRIBUTIONs:
Source code is on https://github.com/Thibault231/projet_7_grandpapybot.
Use a  CONTRIBUTING.md type file to contribute.

CREDITS:
Special thanks for Openclassrooms, Wikipedia and GoogleMap.
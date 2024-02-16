# PYTHON-PLAYWRIGHT TEST FRAMEWORK

This is a **Python/Pytest/Cucumber** Based Test automation Project :
> We'll test our dummy **'[JobBot](https://ray-xxx-eee.github.io/jobBot-UI/#/)'** App.

# App Architecture
 - **UI :**  Hosted as static React App (Vite) in **GitHub Pages**
	 - Using React **Hash Router** to keep it static
	 -  API call only for **Login & Registration** for now.
 - **API :**  Hosted as an **Express** function in **AWS Lambda (sls)**
	 - Auth implemented using JWT with access/refresh token 
 - **DB :**  MongoDB Atlas, SQL
 - **CI/CD :** Github Actions
	 - UI : `vite build` --> `Publish in Gh-Pages
	 - API : **************************************

![Architecture Overview](https://github.com/truePositives/PY-TEST-APP/assets/160166466/923cb2b5-cc51-40d2-b672-add79c74e201)

# Test Architecture 



|END POINTS      |CODES		                     |RESPONSE                     |
|------------------|-------------------------------|--------------------------------|
|/v1/user/login    |`'200 ok'`		                 |`{'message': 'Success'}`        |
|				   |`'404 not found'`	             |`{'message': 'page not found'}` |
|/v1/user/register |`"200 ok"`              		 |{'message': 'User created'}     |
|           	   |`'404 not found'`	             |`{'message': 'page not found'}` |
|                  |  |	|


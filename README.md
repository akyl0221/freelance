<h1>Welcome to Freelance</h1>
<h2>Requarements</h2>
<ul>
  <li>Django v 2.2.2</li>
  <li>Python v 3.6</li>
  <li>Django Rest Framework v 3.9.4</li>
  <li>Python-decouple v 3.1</li>
</ul>
<h2>How does it work</h2>
<p>Clone this repository with command: $git clone https://github.com/akyl0221/freelance.git</p>
<p>pip install virtualenv<p/>
<p>python3 -m venv env<p/>
<p>source env/bin/activate<p/>
<p>pip install -r requirements.txt<p/>
<p>cd freelance</p>
<p>create file .env and add: SECRET_KEY= YourKey</p>
<p>python manage.py migrate</p>
<p>python manage.py runserver</p>
<h2>Routes</h2>
<p>Sign up: 127.0.0.1:8000/api/v1/sign_up</p>
<p>Login: 127.0.0.1:8000/api/v1/login</p>
<p>Create task: 127.0.0.1:8000/api/v1/task</p>
<p>List tasks: 127.0.0.1:8000/api/v1/tasks</p>
<p>Replenish or Withdrawal : 127.0.0.1:8000/api/v1/update_balance</p>
<p>Balance history: 127.0.0.1:8000/api/v1/balance_history</p>
<p>Accept task: 127.0.0.1:8000/api/v1/tasks/<int:pk>/accept</p>
<p>Finish task: 127.0.0.1:8000/api/v1/tasks/<int:pk>/done</p>
<p>Task detail: 127.0.0.1:8000/api/v1/tasks/<int:pk></p>
  

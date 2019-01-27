# django-router-interface-list
Display Cisco router interface list using [Django](https://www.djangoproject.com/). There is also a function to switch an individual interface `on` or `off`.

Here is an example display of the interface list for a Cisco router.

<img src='https://github.com/arrosid/django-router-interface-list/blob/master/django-router-interface.png'>

If you click the `switch` button, the status of interface will turn `on` or `off`. 

If you want to try this project, you can follow these instructions.

<ol>
    <li>Clone the repository <i>git clone git@github.com:arrosid/django-router-interface-list.git</i></li>
    <li>Create virtual environtment <i>virtualenv -p python3 env</i></li>
    <li>Activate the virtual environtment <i>source env/bin/activate</i></li>
    <li>Install the requirement package <i>pip install -r requirements.txt</i></li>
    <li>Run the project</li>
        <ul>
            <li><i>cd django_network</i></li>
            <li><i>python manage.py runserver</i></li>
        </ul>
    <li>Open browser and type <i>localhost:8000</i> in the address bar</li>
</ol>
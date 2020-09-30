#This is just a solution to help a friend in a community

### The link of concern is: https://stackoverflow.com/questions/57061964/how-to-dynamically-create-input-fields-in-vuejs

and this is an implementation of flask api to get the data

dependencies of python:
pip install flask_cors

dependencies on javascript stuff is on the script tags

to run you can do python app.py
also run the index.html in a live server
adjust the ports (it may run differently depending on the machine)

data will be returned as a messy string like:
b'{"my_prop_name":"[{\\"name\\":\\"aa\\",\\"party\\":\\"aaaa\\"},{\\"name\\":\\"23\\",\\"party\\":\\"12\\"},{\\"name\\":\\"ww\\",\\"party\\":\\"ewew\\"}]","headers":{"crossorigin":true}}'

but can be treated as an array in the python wherein you can access it by array[index]

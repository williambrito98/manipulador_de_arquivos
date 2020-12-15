import re


email = 'Will<script/>@gmail.com'

print(re.match(r'^[\w|\d]+@[\w]+.[\w]+(.[\w]+)', email))
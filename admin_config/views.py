from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def current_datetime(request):
    now = datetime.datetime.now()
    html = """<html><body><h2>HTML Forms</h2><form action="/action_page.php">  First name:<br>  <input type="text" name="firstname" value="Mickey">  <br>  Last name:<br>  <input type="text" name="lastname" value="Mouse">  <br><br>  <input type="submit" value="Submit">
</form> <p>If you click the "Submit" button, the form-data will be sent to a page called "/action_page.php".</p></body></html>"""
    return HttpResponse(html)

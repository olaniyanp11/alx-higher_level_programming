#!/bin/bash
# a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -s 0.0.0.0:5000/route_6 -d "email=test@gmail.com&subject=I will always be here for PLD"

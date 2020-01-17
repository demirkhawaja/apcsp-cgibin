#!/bin/bash

echo -e "Content-type: text/html\n\n"

echo "<h1>Rasberry Pi Status: $(sp1b)</h1>"

echo "<pre>$(./piisalive)</pre>" 
 

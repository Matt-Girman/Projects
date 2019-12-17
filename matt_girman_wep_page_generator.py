# -*- coding: utf-8 -*-
"""
Matt Girman

Personal Web Page Generator
11/18/19
"""

name = input("Enter your name: ")
description = input("Describe yourself: ")

file = open('webpage.html','w')

message = """<html>
<head>
</head>
<body>
   <center>
      <h1>""" +name +"""</h1>
   </center>
   <hr />""" +description +"""<hr />
</body>
</html>"""

file.write(message)
file.close()
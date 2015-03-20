#!/usr/bin/python
import cgi,cgitb, template, bleach, os
cgitb.enable()

def is_semicolon(s):
  if ';' in s:
    return True
  else:
    return False

print ("Content-Type: text/html; charset=utf-8\r\n")
print

print template.header()
print template.navbar()


print (""" 
  <div class="page-header"> 
  <h1> LITE 2015: Files</h1>
  </div>
  """)

form = cgi.FieldStorage()
filename = form.getvalue("filename", "")

print ("""

  <div class="panel panel-primary">
  <div class="panel-heading">
    <h5 class="panel-tittle">File Name</h5>
  </div>
  <div class="panel-body">
    <p> Access the content of a file by entering its name.</p>
    <form method="get">
      <div class="input-group">
        <span class="input-group-addon" id="basic-addon1"><span class = "glyphicon glyphicon-user"></span></span>
        <input type="text" value="%s" class="form-control" name="filename" aria-describedby="basic-addon1" placeholder="File Name"></input>
        <span class="input-group-btn">
          <button class="btn btn-default" type="submit">Search</button>
        </span>
      </div>
    </form>
  </div>
  </div> <!-- panel-primary -->

  """ % bleach.clean(filename))

if filename != '' and not is_semicolon(filename):

  try:
    thefile = os.popen("cat %s" % filename)
    print """<p>
               <div class="panel panel-success">
                 <div class="panel-heading">
                  File Content
                 </div>
               <div class="panel-body">
             <pre> """
    for line in thefile.readlines():
      line = line.replace('<', '&lt;')
      print line
    print """</pre>
             </div>
             </div>"""
      
  except IOError:
    print "Could not find the file"

elif is_semicolon(filename) and filename !="":
  print("""<div id="alert" class="alert alert-danger" role="alert"> You must submit a file name.</div>""")



print template.footer()


class info:
  def commands():
    print("The commands are: \nequation.quadsolve() - For quadratic equations. \nequation.slopesolve() - For slope-intercept equations. - NOTE: This one does not work at the moment (Still in developement) \ninfo.help() - Brings up the help page.")

class equation:
  def quadsolve():
    import re
    printed = ""
    quadratic = input("Enter the quadratic equation: ")
    if "x**2" in quadratic:
      a = quadratic.split("x**2")
    elif "x^2" in quadratic:
      a = quadratic.split("x^2")
    if a[0] == "":
      a[0] = "1"
    c = a[1].split("x")
    b = re.sub("[^0-9-.*()/]", "", c[0])
    if b == "":
      b = "1"
    elif b == "-":
      b = "-1"
    a = re.sub("[^0-9-.*()/]", "", a[0])
    c = re.sub("[^0-9-.*()/]", "", c[1])
    try:
      a = float(a)
    except:
      if "/" in a:
        a = a.split("/")
        a = float(int(a[0]) / int(a[1]))
    try:
      b = float(b)
    except:
      if "/" in b:
        b = b.split("/")
        b = float(int(b[0]) / int(b[1]))
    try:
      c = float(c)
    except:
      if "/" in c:
        c = c.split("/")
        c = float(int(c[0]) / int(c[1]))
    try:
      x1p1 = -b
      x1p2 = b**2
      x1p3 = -4*(a*c)
      x1p4 = (x1p2 + x1p3)**0.5
      x1 = (x1p1 + x1p4)/(2*a)
      x2 = (x1p1 - x1p4)/(2*a)
    except:
      pass
    if str(type(x1)) == "<class 'complex'>":
      print("\nNo Solution (Negative Radical)")
      printed = True
    if x1 == x2:
      print("\nSolution:",x1)
    elif printed != True:
      print("\nSolution 1:",x1)
      print("Solution 2:",x2)
    
    
  def slopesolve():
    import re
    slopeeq = input("Enter the Slope Intercept Equation (form: y = mx + b): ")
    m = slopeeq.split("x")
    b = re.sub("[^0-9-]", "", m[1])
    m = re.sub("[^0-9-]", "", m[0])
    print(m)
    print(b)
    def solve(number):
      for i in range(number):
        print(f"x:")

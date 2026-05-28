def handle(user):

    # =========================
    # EXTENSION DETECT
    # =========================
    if ".html" in user or "html" in user:
        lang = "html"
    elif ".css" in user or "css" in user:
        lang = "css"
    elif ".js" in user or "javascript" in user:
        lang = "javascript"
    elif ".py" in user or "python" in user:
        lang = "python"
    else:
        lang = "html"

    # =========================
    # LOGIN PAGE
    # =========================
    if "login" in user or "login page" in user:

        code = """<!DOCTYPE html>
<html>
<head>
<title>Business Login</title>
<style>
*{
  margin:0;
  padding:0;
  box-sizing:border-box;
  font-family:Arial;
}
body{
  height:100vh;
  display:flex;
  align-items:center;
  justify-content:center;
  background:linear-gradient(135deg,#0f172a,#2563eb);
}
.box{
  width:380px;
  background:white;
  padding:35px;
  border-radius:22px;
  box-shadow:0 20px 60px rgba(0,0,0,.45);
}
h2{
  text-align:center;
  color:#1e3a8a;
  margin-bottom:25px;
}
input{
  width:100%;
  padding:14px;
  margin:10px 0;
  border:1px solid #ccc;
  border-radius:12px;
  font-size:15px;
}
button{
  width:100%;
  padding:14px;
  margin-top:12px;
  border:none;
  border-radius:12px;
  background:#2563eb;
  color:white;
  font-size:16px;
  font-weight:bold;
  cursor:pointer;
}
button:hover{
  background:#1d4ed8;
}
</style>
</head>
<body>

<div class="box">
  <h2>Business Login</h2>
  <input type="email" placeholder="Email Address">
  <input type="password" placeholder="Password">
  <button>Login</button>
</div>

</body>
</html>"""

        return f"Okk babu 😎 {lang} code le:\n\n{code}"

    # =========================
    # PYTHON CALCULATOR
    # =========================
    if "calculator" in user and (".py" in user or "python" in user):

        code = """num1 = float(input("First number: "))
num2 = float(input("Second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division possible nahi hai")"""

        return f"Okk babu 😎 python code le:\n\n{code}"

    return None
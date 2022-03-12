function myfunction()
{
var un = document.forms["myForm"]["uname"].value;
var pw = document.forms ["myForm"]["psw"].value;
if(un=="student" && pw=="1234")
{alert("Login Successfully");
 return false; 
}
else
{
alert("Invalid UserName and Password");
}
  
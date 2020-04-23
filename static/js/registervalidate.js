function register()
{
    var Username=document.getElementById("email");
    var password=document.getElementById("pass");
    var repass=document.getElementById("re_pass");
    var phno=document.getElementById("phno");
    var regx=/^[6-9]\d{9}$/;
    var re =  /^\w+([\.-]?\w+)+@\w+([\.:]?\w+)+(\.[a-zA-Z0-9]{2,3})+$/;
    if(Username.value.trim()=="")
    {
        alert("Email is Empty");
        return false;
    }
    
    else if(!re.test(Username.value.trim())){
    	alert("Please Enter a valid Email")
    	return false;
    }
    else if(password.value.trim()=="" || repass.value.trim()=="" )
    {
        alert("Password is Empty");
        return false;
    }
    else if(password.value.trim().length<5 || repass.value.trim().length<5)
    {
        alert("Password must be at least 5 characters");
        return false;
    }
    else if(password.value.trim()!=repass.value.trim())
    {
        alert("Password do not Match!");
        return false;
    }
    else if(!regx.test(phno.value.trim())){
    	        alert("Invalid Phone Number");
    	    	return false;
    		}

    else{
//    	alert("Registration Successful by "+ Username.value);
//    	   	document.getElementById("signup").style.display='none';
    	   
        return true;
    }
    
    
    
   
    
}


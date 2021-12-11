function Validate(){
    let phoneOK = document.getElementById("tel").checkValidity()
    let phMsg = ""
    if (phoneOK){
        phMsg = "OK";
    }
    else{
        phMsg = "Not OK";
    }
    document.getElementById("phoneValid").innerHTML = phMsg;
    let emailOK = document.getElementById("email").checkValidity()
    let emailMsg = ""
    if (emailOK){
        emailMsg = "OK";
    }
    else{
        emailMsg = "Not OK";
    }
    document.getElementById("emailValid").innerHTML = emailMsg;
    if (emailOK && phoneOK){
        alert("OK!")
    }
}
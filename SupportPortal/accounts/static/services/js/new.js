
function myFunction() {


    alert("Action Completed Successfully.");
    window.opener.location.href="ReqFull.html";
      window.top.close();
	}

function chclick() {
    var checkBox = document.getElementById("myCheck");
    var text = document.getElementById("text");
    if (checkBox.checked == true){
        text.style.display = "block";
    } else {
       text.style.display = "none";
    }
}


function myFunction_show_User() {

    myVar2=setTimeout(function () {document.getElementById('imgToHide').style.display='block';document.getElementById('imgToHide1').style.display='block'}, 1000);
    myVar = setTimeout(alertFunc, 5000);
}

function alertFunc() {
              var y= document.getElementById('imgToHide');
              var z= document.getElementById('imgToHide1');
    var x = document.getElementById("MainDiv");
    if (x.style.display === "none") {
              y.style.display = "none";
              z.style.display = "none";
        x.style.display = "block";
   }
}


function myFunction_show_Action() {
    var x = document.getElementById("myDIV");
    if (x.style.display === "none") {
        x.style.display = "block";
    }
}


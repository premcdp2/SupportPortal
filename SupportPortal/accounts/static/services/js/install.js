function myFunction() {
   alert("Action Completed Successfully.");
    window.opener.location.href="ReqFull.html";
      window.top.close();
  }

  function myFunction_show_Action() {
    var x = document.getElementById("myDIV");
    if (x.style.display === "none") {
        x.style.display = "block";
    }
}
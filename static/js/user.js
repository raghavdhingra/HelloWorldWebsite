//User.js
"use strict";
let togVal = 0
document.getElementById("leftPaneToggleBtn").addEventListener("click",()=>{
    if (togVal == 0){
        for ( var i = 1; i <= 6; i++ ){
            document.getElementById(`left-active${i}`).classList.add("activeIt");
        }
        togVal+=1;
        document.getElementById("turnAround").style.transition = "0.2s";
        document.getElementById("turnAround").style.transform = "rotate(180deg)";
    }
    else{
        for (var i = 1; i <= 6; i++ ){
            document.getElementById(`left-active${i}`).classList.remove("activeIt");
        }
        togVal = 0;
        document.getElementById("turnAround").style.transform = "rotate(0)";
    }
});
"use strict";
//Declaring constants
const main_nav = document.getElementById("main_nav");
const nav_more = document.getElementById("nav_more");
const nav_dropdown = document.getElementById("nav_dropdown");
const nav_logo_text = document.getElementById("nav-logo-text");
const plusCircle = document.getElementById("fa-plus-circle");
const mobile_nav_bar = document.getElementById("mobile_nav_bar");

let posX = 0;


//Main NavBar Height Control Function
const mainNavHeightControl = () => {
    //Main NavBar After Scroll
    if (document.body.scrollTop > 15 || document.documentElement.scrollTop > 15) {
        main_nav.classList.add("main_nav_add");
        nav_dropdown.classList.add("nav_drop_add");
    }
    //Main NavBar Before Scroll
    else {
        main_nav.classList.remove("main_nav_add");
        nav_dropdown.classList.remove("nav_drop_add");
    }
}


//Mobile NavBar
const openMobileNav = () => {
    if (plusCircle.style.transform === "rotate(315deg)"){
        plusCircle.style.transform = "rotate(0)";
        document.getElementsByClassName("mobile_nav_bar_inner")[0].style.display = "grid";
        document.getElementsByClassName("mobile_nav_bar2")[0].style.animation = "decreaseHeight 0.5s ease-in-out 1 forwards";
    }
    else{
        document.getElementsByClassName("mobile_nav_bar_inner")[0].style.display = "none";
        plusCircle.style.transition = "0.5s";
        document.getElementsByClassName("mobile_nav_bar2")[0].style.animation = "increaseHeight 0.5s ease 1 forwards";
        plusCircle.style.transform = "rotate(315deg)";
    }
}
//Mobile NavBar


//NavBar More Button OffSet Checker on X-Axis
nav_more.onmouseover = () => {
    posX = nav_more.offsetLeft;
    nav_dropdown.style.left = `${posX}px`;
    nav_dropdown.style.display = 'block';
}

nav_more.onmouseout = () => {
    nav_dropdown.style.display = 'none';
}

nav_dropdown.onmouseover = () => {
    nav_dropdown.style.display = 'block';
}

nav_dropdown.onmouseout = () => {
    nav_dropdown.style.display = 'none';
}
//NavBar More Button OffSet Checker on X-Axis


//Window OnScroll Event
window.onscroll = () => {
    mainNavHeightControl();
}

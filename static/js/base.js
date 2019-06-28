//Declaring constants
const main_nav = document.getElementById("main_nav");
const nav_more = document.getElementById("nav_more");
const nav_dropdown = document.getElementById("nav_dropdown");
const drop_contact = document.getElementById("drop_contact");
const drop_login = document.getElementById("drop_login");


//Main NavBar Height Control Function
const mainNavHeightControl = () => {
    //Main NavBar After Scroll
    if (document.body.scrollTop > 15 || document.documentElement.scrollTop > 15) {
        main_nav.style.minHeight = "5em";
        main_nav.style.maxHeight = "5em";
        main_nav.style.lineHeight = "5em";
        main_nav.style.color = "5em";
        main_nav.style.background = "#eee";
        main_nav.style.boxShadow = "0 3px 30px 0.5px rgba(51, 51, 51, 0.589)";
    }
    //Main NavBar Before Scroll
    else {
        main_nav.style.minHeight = "7em";
        main_nav.style.maxHeight = "7em";        
        main_nav.style.lineHeight = "7em";
        main_nav.style.background = "rgba(0,0,0,0)";
        main_nav.style.boxShadow = "none";
    }
}


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


//Window OnScroll Event
window.onscroll = () => {
    mainNavHeightControl();
}

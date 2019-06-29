//Declaring constants
const main_nav = document.getElementById("main_nav");
const nav_more = document.getElementById("nav_more");
const nav_dropdown = document.getElementById("nav_dropdown");
const nav_dropdown2 = document.getElementById("nav_dropdown2");
const signedIn_more = document.getElementById("signedIn_more");
const drop_contact = document.getElementById("drop_contact");
const drop_login = document.getElementById("drop_login");
const nav_logo_text = document.getElementById("nav-logo-text");
const nav_logo = document.getElementById("nav-logo");


//Main NavBar Height Control Function
const mainNavHeightControl = () => {
    //Main NavBar After Scroll
    if (document.body.scrollTop > 35 || document.documentElement.scrollTop > 35) {
        main_nav.style.minHeight = "3.7em";
        main_nav.style.maxHeight = "3.7em";
        main_nav.style.lineHeight = "3.7em";
        main_nav.style.color = "5em";
        main_nav.style.background = "#eee";
        main_nav.style.boxShadow = "0 3px 30px 0.5px rgba(51, 51, 51, 0.589)";
        nav_dropdown.style.top = "3.7em";
        nav_dropdown2.style.top = "3.7em";
        if (window.innerWidth >= 500) {
            nav_logo_text.style.fontSize = "1.5em";
            nav_logo.style.height = "75px";
        }
    }
    //Main NavBar Before Scroll
    else {
        main_nav.style.minHeight = "7em";
        main_nav.style.maxHeight = "7em";        
        main_nav.style.lineHeight = "7em";
        main_nav.style.background = "rgba(0,0,0,0)";
        nav_dropdown.style.top = "5em";
        nav_dropdown2.style.top = "5em";
        main_nav.style.boxShadow = "none";
        if (window.innerWidth >= 500) {
            nav_logo_text.style.fontSize = "2em";
            nav_logo.style.height = "100px";
        }
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
//NavBar More Button OffSet Checker on X-Axis



//Nav Drop Down 2 Login/SignUp Mobile View
signedIn_more.onmouseover = () => {
    posX = signedIn_more.offsetLeft;
    nav_dropdown2.style.left = `${posX}px`;
    nav_dropdown2.style.display = 'block';    
}

signedIn_more.onmouseout = () => {
    nav_dropdown2.style.display = 'none';
}

nav_dropdown2.onmouseover = () => {
    nav_dropdown2.style.display = 'block';
}

nav_dropdown2.onmouseout = () => {
    nav_dropdown2.style.display = 'none';
}

//Nav Drop Down 2 Login/SignUp Mobile View


//Window OnScroll Event
window.onscroll = () => {
    mainNavHeightControl();
}

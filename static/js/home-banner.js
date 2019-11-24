const closeHomeBanner = () => {
    document.getElementById("home-banner-overlay").classList.add("bannerNone");
}

const openHomeBanner = () => {
    document.getElementById("home-banner-overlay").classList.remove("bannerNone");
}

window.onload = () => {
    setTimeout(() => {
        openHomeBanner();
    }, 1000);
}
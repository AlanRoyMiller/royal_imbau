const menuHamburger = document.querySelector(".menu-hamburger");
const navLinks = document.querySelector(".nav-links");

menuHamburger.addEventListener('click', () => {
    // Toggle mobile menu class for the nav links
    navLinks.classList.toggle('mobile-menu');

    // Toggle no-scroll class on the body
    document.body.classList.toggle("no-scroll");
});



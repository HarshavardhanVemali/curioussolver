window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar-collapse');
    const scrollToTopBtn = document.getElementById('scrollToTopBtn');

    if (window.scrollY > 100) {
        navbar.classList.add('fixed-top');
    } else {
        navbar.classList.remove('fixed-top');
    }

    if (window.scrollY > 300) {
        scrollToTopBtn.classList.add('show');
    } else {
        scrollToTopBtn.classList.remove('show');
    }
});



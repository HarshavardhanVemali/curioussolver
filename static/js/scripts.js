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

function isWhatsAppInstalled() {
    return navigator.userAgent.toLowerCase().indexOf('whatsapp') > -1;
  }
  const whatsappLink = document.querySelector('.whatsapp-link');
  if (isWhatsAppInstalled()) {
    whatsappLink.href = "whatsapp://send?phone=+917675922209&text=Hello";
  } else {
    whatsappLink.href = "https://wa.me/+917675922209?text=Hello";
  }
  document.addEventListener('DOMContentLoaded', function() {

    var dropdownButtons = document.querySelectorAll('.navbar-nav .nav-item.dropdown');
    dropdownButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            button.querySelector('.dropdown-menu').classList.toggle('show');
        });
    });
    document.addEventListener('click', function(event) {
        dropdownButtons.forEach(function(button) {
            var dropdownMenu = button.querySelector('.dropdown-menu');
            if (!button.contains(event.target) && dropdownMenu.classList.contains('show')) {
                dropdownMenu.classList.remove('show');
            }
        });
    });
});

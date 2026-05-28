// Init AOS animations
AOS.init({ duration: 800, once: true, offset: 80 });

// Navbar shrink on scroll
const nav = document.querySelector('.custom-navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 40) nav.classList.add('scrolled');
  else nav.classList.remove('scrolled');
});

// Close mobile nav after click
document.querySelectorAll('.navbar-nav .nav-link').forEach(link => {
  link.addEventListener('click', () => {
    const menu = document.getElementById('navMenu');
    if (menu.classList.contains('show')) {
      new bootstrap.Collapse(menu).hide();
    }
  });
});

// Auto-dismiss flash messages
setTimeout(() => {
  document.querySelectorAll('.alert').forEach(a => bootstrap.Alert.getOrCreateInstance(a).close());
}, 5000);

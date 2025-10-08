// Mobile nav toggle
const navToggle = document.getElementById('navToggle');
const mainNav = document.getElementById('mainNav');

navToggle?.addEventListener('click', () => {
  mainNav.classList.toggle('open');
  if (mainNav.classList.contains('open')) {
    mainNav.style.display = 'flex';
    navToggle.textContent = '✕';
  } else {
    mainNav.style.display = '';
    navToggle.textContent = '☰';
  }
});

// Simple intersection observer for reveal animations
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('revealed');
      observer.unobserve(e.target);
    }
  });
}, {threshold: 0.12});

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

// Smooth internal link scrolling (for older browsers)
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', function(e){
    const href = this.getAttribute('href');
    if(href.length > 1){
      e.preventDefault();
      const el = document.querySelector(href);
      el?.scrollIntoView({behavior: 'smooth', block: 'start'});
      // close mobile nav if open
      if (mainNav.classList.contains('open')) {
        mainNav.classList.remove('open');
        mainNav.style.display='';
        navToggle.textContent='☰';
      }
    }
  });
});
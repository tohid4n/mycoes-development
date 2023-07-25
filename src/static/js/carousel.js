
// for scroll effect

// Wait for the DOM content to load
document.addEventListener('DOMContentLoaded', () => {
  const carousel = document.querySelector('.carousel');

  const applyScrollEffect = () => {
    const isLgScreen = window.matchMedia('(min-width: 1024px)').matches;
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (isLgScreen && scrollTop > 0) {
      carousel.classList.add('scroll-effect');
    } else {
      carousel.classList.remove('scroll-effect');
    }
  };

  window.addEventListener('scroll', applyScrollEffect);
  window.addEventListener('resize', applyScrollEffect);

  // Initial check on page load
  applyScrollEffect();
});








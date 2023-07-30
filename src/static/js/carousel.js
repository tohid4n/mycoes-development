// for scroll effect

// Wait for the DOM content to load
document.addEventListener('DOMContentLoaded', () => {
  const scroll = document.querySelector('.scroll');
  const applyScrollEffect = () => {
    const isLgScreen = window.matchMedia('(min-width: 1024px)').matches;
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    if (isLgScreen && scrollTop > 0) {
      scroll.classList.add('scroll-effect');
    } else {
      scroll.classList.remove('scroll-effect');
    }
  };
  window.addEventListener('scroll', applyScrollEffect);
  window.addEventListener('resize', applyScrollEffect);
  // Initial check on page load
  applyScrollEffect();
});





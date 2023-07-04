// Variables
const slides = document.querySelectorAll('.carousel-slide');
const dots = document.querySelectorAll('.carousel-indicator-dot');
const prevButton = document.querySelector('.carousel-nav-prev');
const nextButton = document.querySelector('.carousel-nav-next');
let currentSlide = 0;

// Function to show the current slide
function showSlide() {
  // Hide all slides and remove active class from dots
  slides.forEach((slide) => {
    slide.classList.add('hidden');
  });
  dots.forEach((dot) => {
    dot.classList.remove('active');
  });

  // Display current slide and add active class to corresponding dot
  slides[currentSlide].classList.remove('hidden');
  dots[currentSlide].classList.add('active');
}

// Function to move to the next slide
function nextSlide() {
  currentSlide++;
  if (currentSlide >= slides.length) {
    currentSlide = 0;
  }
  showSlide();
}

// Function to move to the previous slide
function prevSlide() {
  currentSlide--;
  if (currentSlide < 0) {
    currentSlide = slides.length - 1;
  }
  showSlide();
}

// Event listeners for navigation buttons
nextButton.addEventListener('click', nextSlide);
prevButton.addEventListener('click', prevSlide);

// Start the carousel
function startCarousel() {
  setInterval(nextSlide, 3000);
}

// Call the startCarousel function to begin automated sliding
startCarousel();



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








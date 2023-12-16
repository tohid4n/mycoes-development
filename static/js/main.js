//Start of Tawk.to Script

var Tawk_API = Tawk_API || {},
  Tawk_LoadStart = new Date();
(function () {
  var s1 = document.createElement("script"),
    s0 = document.getElementsByTagName("script")[0];
  s1.async = true;
  s1.src = "https://embed.tawk.to/64bdece7cc26a871b02ac7ad/1h62uaqpq";
  s1.charset = "UTF-8";
  s1.setAttribute("crossorigin", "*");
  s0.parentNode.insertBefore(s1, s0);
})();


// Alert messagess

// Function to close the alert and its parent div
function closeAlert(alertElement) {
  alertElement.style.display = "none";
  alertElement.parentElement.removeChild(alertElement);
}

// Automatically close the alert after 3 seconds
document.addEventListener("DOMContentLoaded", () => {
  const alerts = document.querySelectorAll(".alert");
  alerts.forEach((alert) => {
    setTimeout(() => {
      closeAlert(alert);
    }, 3000);
  });
});






// Dark and Light mode
// On page load or when changing themes, best to add inline in `head` to avoid FOUC
// Function to set the dark theme
// Function to set the dark theme
function setDarkTheme() {
  document.documentElement.classList.add("dark");
  localStorage.theme = "dark";
}

// Function to set the light theme
function setLightTheme() {
  document.documentElement.classList.remove("dark");
  localStorage.theme = "light";
}

// Check if the theme is stored in localStorage, otherwise set the default to dark
if (localStorage.theme !== "light") {
  setDarkTheme();
}

// Function to handle theme switcher item click
function onThemeSwitcherItemClick(event) {
  const theme = event.target.dataset.theme;

  if (theme === "system") {
    // Handle setting system theme if needed
  } else if (theme === "dark") {
    setDarkTheme();
  } else {
    setLightTheme();
  }
}

// Attach click event listeners to theme switcher items
const themeSwitcherItems = document.querySelectorAll("#theme-switcher");
themeSwitcherItems.forEach((item) => {
  item.addEventListener("click", onThemeSwitcherItemClick);
});



//navbar and footer gap calulate and assign to profile pages sidebar

document.addEventListener('DOMContentLoaded', function () {
    // Calculate the height of the window
    const windowHeight = window.innerHeight;

    // Apply the height to the sidebar
    const sidebar = document.getElementById('default-sidebar');
    sidebar.style.height = windowHeight + 'px';
});






// scrolling effect to the bottom

document.addEventListener('DOMContentLoaded', function () {
  // Variables to control scroll animation
  var scrollStep = 500; // Adjust the step size as needed
  var isAnimating = false;

  // Show/hide the scroll-to-bottom icon based on the user's scroll position
  window.addEventListener('scroll', function () {
    var scrollToBottom = document.getElementById('scrollToBottom');
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 20) {
      scrollToBottom.classList.add('hidden');
    } else {
      scrollToBottom.classList.remove('hidden');
    }
  });

  // Scroll to the bottom with animation when the icon is clicked
  document.getElementById('scrollToBottom').addEventListener('click', function () {
    if (!isAnimating) {
      isAnimating = true;
      scrollToBottom();
    }
  });

  // Function to scroll to the bottom with animation
  function scrollToBottom() {
    var currentScrollPosition = window.scrollY;
    var targetScrollPosition = currentScrollPosition + scrollStep;

    // Recursive function for smooth animation
    function animateScroll() {
      if (currentScrollPosition >= targetScrollPosition) {
        isAnimating = false;
      } else {
        window.scrollTo({
          top: currentScrollPosition,
          behavior: 'smooth'
        });
        currentScrollPosition += 10; // Adjust the step size as needed
        requestAnimationFrame(animateScroll);
      }
    }

    // Start the animation
    animateScroll();
  }

  // Show the scroll-to-bottom icon when the user scrolls back up
  var lastScrollPosition = window.scrollY;
  window.addEventListener('scroll', function () {
    var currentScrollPosition = window.scrollY;
    if (currentScrollPosition < lastScrollPosition) {
      document.getElementById('scrollToBottom').classList.remove('hidden');
    }
    lastScrollPosition = currentScrollPosition;
  });
});

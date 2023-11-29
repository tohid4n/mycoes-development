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




// On page load or when changing themes, best to add inline in `head` to avoid FOUC
if (
  localStorage.theme === "dark" ||
  (!("theme" in localStorage) &&
    window.matchMedia("(prefers-color-scheme: dark)").matches)
) {
  document.documentElement.classList.add("dark");
} else {
  document.documentElement.classList.remove("dark");
}

function setDarkTheme() {
  document.documentElement.classList.add("dark");
  localStorage.theme = "dark";
}

function setLightTheme() {
  document.documentElement.classList.remove("dark");
  localStorage.theme = "light";
}

function onThemeSwitcherItemClick(event) {
  const theme = event.target.dataset.theme;

  if (theme === "system") {
    localStorage.removeItem("theme");
    setSystemTheme();
  } else if (theme === "dark") {
    setDarkTheme();
  } else {
    setLightTheme();
  }
}

const themeSwitcherItems = document.querySelectorAll("#theme-switcher");
themeSwitcherItems.forEach((item) => {
  item.addEventListener("click", onThemeSwitcherItemClick);
});




// for hero page background video

document.addEventListener("DOMContentLoaded", function () {
  var video = document.getElementById("bgVideo");
  var playIcon = document.getElementById("playIcon");
  var pauseIcon = document.getElementById("pauseIcon");

  function updatePlayPauseIcons() {
    if (video.paused) {
      playIcon.style.display = "block";
      pauseIcon.style.display = "none";
    } else {
      playIcon.style.display = "none";
      pauseIcon.style.display = "block";
    }
  }

  function playVideo() {
    video.play().then(updatePlayPauseIcons);
  }

  function pauseVideo() {
    video.pause();
    updatePlayPauseIcons();
  }

  playIcon.addEventListener("click", playVideo);
  pauseIcon.addEventListener("click", pauseVideo);

  // Set initial visibility of play/pause icons based on video state
  video.addEventListener("loadeddata", updatePlayPauseIcons);

  // Listen for window resize events and update button state
  window.addEventListener("resize", function () {
    if (window.innerWidth < 768) {
      // For small screens, hide the video and show play button
      video.style.display = "none";
      playIcon.style.display = "block";
      pauseIcon.style.display = "none";
    } else {
      // For larger screens, show the video and update button state
      video.style.display = "block";
      updatePlayPauseIcons();
    }
  });
});





// navbar scroll effect

document.addEventListener("DOMContentLoaded", function () {
  var navBar = document.getElementById("navbar");

  function toggleScrollClass() {
    var scrolled = window.scrollY;
    var windowWidth = window.innerWidth;

    // Remove all classes related to scrolling and small screens
    navBar.classList.remove(
      "bg-white", "dark:bg-black", 
      "scrolled"
    );

    if (windowWidth >= 768) {
      // Toggle the 'scrolled' class based on the scroll position
      navBar.classList.toggle("scrolled", scrolled > 10);
    } else {
      // For small screens, always add bg-white and dark:bg-black
      navBar.classList.add("bg-white", "dark:bg-black");
    }
  }

  // Initial call to set classes on page load
  toggleScrollClass();

  window.addEventListener("scroll", toggleScrollClass);
  window.addEventListener("resize", toggleScrollClass);
});






//navbar and footer gap calulate and assign to profile pages sidebar

document.addEventListener('DOMContentLoaded', function () {
    // Calculate the height of the window
    const windowHeight = window.innerHeight;

    // Apply the height to the sidebar
    const sidebar = document.getElementById('default-sidebar');
    sidebar.style.height = windowHeight + 'px';
});

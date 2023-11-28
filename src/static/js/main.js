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

  playIcon.addEventListener("click", function () {
    video.play().then(updatePlayPauseIcons);
  });

  pauseIcon.addEventListener("click", function () {
    video.pause();
    updatePlayPauseIcons();
  });

  // Set initial visibility of play/pause icons based on video state
  video.addEventListener("loadeddata", function () {
    updatePlayPauseIcons();
  });
});




// navbar scroll effect

document.addEventListener("DOMContentLoaded", function () {
  var navBar = document.getElementById("navbar");

  window.addEventListener("scroll", function () {
    var scrolled = window.scrollY;

    if (scrolled > 10) {
      navBar.classList.add("bg-white", "dark:bg-black");
    } else {
      navBar.classList.remove("bg-white", "dark:bg-black");
    }
  });
});



//navbar and footer gap calulate and assign to profile pages sidebar
document.addEventListener('DOMContentLoaded', function () {
    // Calculate the height of the window
    const windowHeight = window.innerHeight;

    // Apply the height to the sidebar
    const sidebar = document.getElementById('default-sidebar');
    sidebar.style.height = windowHeight + 'px';
});

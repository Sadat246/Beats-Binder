// On page load set the theme.
(function() {
    let onpageLoad = localStorage.getItem("theme") || "";
    let element = document.body;
    element.classList.add(onpageLoad);
    // document.getElementById("theme").textContent =
    //   localStorage.getItem("theme") || "light";
  })();
  
  function themeToggle() {
    let element = document.body;
    let navBar = document.querySelector(".navbar");

    element.classList.toggle("dark_mode");
    navBar.classList.toggle("navbar-dark");

    let theme = localStorage.getItem("theme");
    if (theme && theme === "dark_mode") {
        localStorage.setItem("theme", "");
    } else {
        localStorage.setItem("theme", "dark_mode");
    }
}

    // document.getElementById("theme").textContent = localStorage.getItem("theme");

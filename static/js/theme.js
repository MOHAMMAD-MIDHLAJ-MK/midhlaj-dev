document.addEventListener("DOMContentLoaded", function () {

    const themeToggle = document.getElementById("themeToggle");

    if (!themeToggle) {
        console.log("Theme button not found");
        return;
    }


    /* ==========================================
       GET SAVED THEME
    ========================================== */

    let savedTheme = localStorage.getItem("theme");

    if (!savedTheme) {
        savedTheme = "light";
    }


    applyTheme(savedTheme);


    /* ==========================================
       TOGGLE THEME
    ========================================== */

    themeToggle.addEventListener("click", function () {

        const currentTheme =
            document.documentElement.getAttribute("data-bs-theme");

        const newTheme =
            currentTheme === "dark"
                ? "light"
                : "dark";

        applyTheme(newTheme);

        localStorage.setItem(
            "theme",
            newTheme
        );

    });


    /* ==========================================
       APPLY THEME
    ========================================== */

    function applyTheme(theme) {

        document.documentElement.setAttribute(
            "data-bs-theme",
            theme
        );

        document.body.classList.toggle(
            "dark",
            theme === "dark"
        );


        const icon =
            themeToggle.querySelector("i");

        if (icon) {

            if (theme === "dark") {

                icon.className =
                    "bi bi-sun-fill";

            } else {

                icon.className =
                    "bi bi-moon-fill";

            }

        }

    }

});
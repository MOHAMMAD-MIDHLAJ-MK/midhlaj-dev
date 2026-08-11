document.addEventListener("DOMContentLoaded", function () {

    const menuToggle =
        document.getElementById("navMenuToggle");

    const mobileMenu =
        document.getElementById("mobileMenu");


    if (!menuToggle || !mobileMenu) {
        return;
    }


    /* =====================================================
       OPEN
    ===================================================== */

    function openMenu() {

        mobileMenu.classList.add("active");

        menuToggle.setAttribute(
            "aria-expanded",
            "true"
        );

        menuToggle.setAttribute(
            "aria-label",
            "Close menu"
        );

        menuToggle.innerHTML =
            '<i class="bi bi-x-lg"></i>';
    }


    /* =====================================================
       CLOSE
    ===================================================== */

    function closeMenu() {

        mobileMenu.classList.remove("active");

        menuToggle.setAttribute(
            "aria-expanded",
            "false"
        );

        menuToggle.setAttribute(
            "aria-label",
            "Open menu"
        );

        menuToggle.innerHTML =
            '<i class="bi bi-list"></i>';
    }


    /* =====================================================
       TOGGLE
    ===================================================== */

    menuToggle.addEventListener(
        "click",
        function (event) {

            event.stopPropagation();

            if (
                mobileMenu.classList.contains(
                    "active"
                )
            ) {

                closeMenu();

            } else {

                openMenu();

            }

        }
    );


    /* =====================================================
       DON'T CLOSE INSIDE MENU
    ===================================================== */

    mobileMenu.addEventListener(
        "click",
        function (event) {

            event.stopPropagation();

        }
    );


    /* =====================================================
       OUTSIDE CLICK
    ===================================================== */

    document.addEventListener(
        "click",
        function (event) {

            if (
                mobileMenu.classList.contains(
                    "active"
                ) &&
                !mobileMenu.contains(event.target) &&
                !menuToggle.contains(event.target)
            ) {

                closeMenu();

            }

        }
    );


    /* =====================================================
       TOUCH OUTSIDE
    ===================================================== */

    document.addEventListener(
        "touchstart",
        function (event) {

            if (
                mobileMenu.classList.contains(
                    "active"
                ) &&
                !mobileMenu.contains(event.target) &&
                !menuToggle.contains(event.target)
            ) {

                closeMenu();

            }

        },
        {
            passive: true
        }
    );


    /* =====================================================
       LINK CLICK
    ===================================================== */

    const links =
        mobileMenu.querySelectorAll(
            "a"
        );


    links.forEach(function (link) {

        link.addEventListener(
            "click",
            function () {

                closeMenu();

            }
        );

    });


    /* =====================================================
       LOGOUT FORM
    ===================================================== */

    const logoutForm =
        mobileMenu.querySelector(
            ".mobile-logout-form"
        );


    if (logoutForm) {

        logoutForm.addEventListener(
            "submit",
            function () {

                closeMenu();

            }
        );

    }


    /* =====================================================
       ESCAPE
    ===================================================== */

    document.addEventListener(
        "keydown",
        function (event) {

            if (
                event.key === "Escape"
            ) {

                closeMenu();

            }

        }
    );


    /* =====================================================
       RESIZE
       Desktop → close menu
    ===================================================== */

    window.addEventListener(
        "resize",
        function () {

            if (
                window.innerWidth > 800
            ) {

                closeMenu();

            }

        }
    );


    /* =====================================================
       INITIAL
    ===================================================== */

    closeMenu();

});

/* =========================================================
   MIDHLAJ DEV — MAIN JS
========================================================= */

document.addEventListener(
    "DOMContentLoaded",
    function () {


        /* =================================================
           CURRENT YEAR
        ================================================= */

        const yearElements =
            document.querySelectorAll(
                "[data-current-year]"
            );


        yearElements.forEach(
            function (element) {

                element.textContent =
                    new Date().getFullYear();

            }
        );


        /* =================================================
           SMOOTH ANCHOR SCROLL
        ================================================= */

        const anchors =
            document.querySelectorAll(
                'a[href^="#"]'
            );


        anchors.forEach(
            function (anchor) {

                anchor.addEventListener(
                    "click",
                    function (event) {

                        const targetId =
                            this.getAttribute(
                                "href"
                            );


                        if (
                            !targetId ||
                            targetId === "#"
                        ) {
                            return;
                        }


                        const target =
                            document.querySelector(
                                targetId
                            );


                        if (!target) {
                            return;
                        }


                        event.preventDefault();


                        target.scrollIntoView({
                            behavior: "smooth",
                            block: "start"
                        });

                    }
                );

            }
        );


        /* =================================================
           BACK TO TOP
        ================================================= */

        const backToTop =
            document.getElementById(
                "backToTop"
            );


        if (backToTop) {

            function updateBackToTop() {

                if (
                    window.scrollY > 500
                ) {

                    backToTop.classList.add(
                        "show"
                    );

                } else {

                    backToTop.classList.remove(
                        "show"
                    );

                }

            }


            window.addEventListener(
                "scroll",
                updateBackToTop,
                { passive: true }
            );


            backToTop.addEventListener(
                "click",
                function () {

                    window.scrollTo({
                        top: 0,
                        behavior: "smooth"
                    });

                }
            );


            updateBackToTop();

        }


        /* =================================================
           IMAGE ERROR HANDLING
        ================================================= */

        const images =
            document.querySelectorAll(
                "img"
            );


        images.forEach(
            function (image) {

                image.addEventListener(
                    "error",
                    function () {

                        this.classList.add(
                            "image-error"
                        );

                    }
                );

            }
        );

    }
);
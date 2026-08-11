/* =========================================================
   MIDHLAJ DEV — HOME JS
   ========================================================= */

document.addEventListener("DOMContentLoaded", function () {


    /* =====================================================
       TYPING ANIMATION
       ===================================================== */

    const typingElement =
        document.querySelector("[data-typing]");


    if (typingElement) {

        const words = [
            "Python Full Stack Developer",
            "Django Developer",
            "Web Developer",
            "Software Developer"
        ];


        let wordIndex = 0;
        let charIndex = 0;
        let deleting = false;

        let typingTimer = null;


        function typeText() {

            const currentWord =
                words[wordIndex];


            if (!deleting) {

                charIndex++;

                typingElement.textContent =
                    currentWord.substring(
                        0,
                        charIndex
                    );


                if (charIndex >= currentWord.length) {

                    deleting = true;

                    typingTimer =
                        setTimeout(
                            typeText,
                            1800
                        );

                    return;
                }


                typingTimer =
                    setTimeout(
                        typeText,
                        85
                    );

            } else {

                charIndex--;

                typingElement.textContent =
                    currentWord.substring(
                        0,
                        charIndex
                    );


                if (charIndex <= 0) {

                    charIndex = 0;

                    deleting = false;

                    wordIndex =
                        (wordIndex + 1)
                        % words.length;


                    typingTimer =
                        setTimeout(
                            typeText,
                            350
                        );

                    return;
                }


                typingTimer =
                    setTimeout(
                        typeText,
                        45
                    );
            }
        }


        /*
         * Start only once.
         * No page reload.
         */

        typeText();


        /*
         * Stop timer if page is being
         * unloaded.
         */

        window.addEventListener(
            "beforeunload",
            function () {

                if (typingTimer) {
                    clearTimeout(typingTimer);
                }

            }
        );

    }



    /* =====================================================
       COUNTER ANIMATION
       ===================================================== */

    const counters =
        document.querySelectorAll(
            "[data-counter]"
        );


    if (counters.length) {

        const counterObserver =
            new IntersectionObserver(
                function (entries, observer) {

                    entries.forEach(
                        function (entry) {

                            if (
                                !entry.isIntersecting
                            ) {
                                return;
                            }


                            const element =
                                entry.target;


                            const target =
                                parseInt(
                                    element.dataset.counter,
                                    10
                                );


                            if (
                                Number.isNaN(target)
                            ) {
                                return;
                            }


                            let start = 0;

                            const duration = 1000;

                            const startTime =
                                performance.now();


                            function animateCounter(
                                currentTime
                            ) {

                                const elapsed =
                                    currentTime -
                                    startTime;


                                const progress =
                                    Math.min(
                                        elapsed /
                                        duration,
                                        1
                                    );


                                /*
                                 * Smooth easing
                                 */

                                const eased =
                                    1 -
                                    Math.pow(
                                        1 - progress,
                                        3
                                    );


                                start =
                                    Math.floor(
                                        target * eased
                                    );


                                element.textContent =
                                    start + "+";


                                if (
                                    progress < 1
                                ) {

                                    requestAnimationFrame(
                                        animateCounter
                                    );

                                } else {

                                    element.textContent =
                                        target + "+";

                                }
                            }


                            requestAnimationFrame(
                                animateCounter
                            );


                            observer.unobserve(
                                element
                            );

                        }
                    );

                },
                {
                    threshold: 0.35
                }
            );


        counters.forEach(
            function (counter) {

                counterObserver.observe(
                    counter
                );

            }
        );
    }



    /* =====================================================
       SCROLL REVEAL
       ===================================================== */

    const revealElements =
        document.querySelectorAll(
            ".reveal"
        );


    if (revealElements.length) {

        const revealObserver =
            new IntersectionObserver(
                function (entries, observer) {

                    entries.forEach(
                        function (entry) {

                            if (
                                entry.isIntersecting
                            ) {

                                entry.target.classList.add(
                                    "revealed"
                                );


                                observer.unobserve(
                                    entry.target
                                );

                            }

                        }
                    );

                },
                {
                    threshold: 0.12
                }
            );


        revealElements.forEach(
            function (element) {

                revealObserver.observe(
                    element
                );

            }
        );
    }



    /* =====================================================
       PROJECT IMAGE ERROR HANDLING
       ===================================================== */

    const projectImages =
        document.querySelectorAll(
            ".project-image img"
        );


    projectImages.forEach(
        function (image) {

            image.addEventListener(
                "error",
                function () {

                    /*
                     * Prevent broken image icon
                     * from disturbing the card.
                     */

                    image.style.display =
                        "none";

                    image.parentElement.classList.add(
                        "image-missing"
                    );

                }
            );

        }
    );



    /* =====================================================
       SMOOTH INTERNAL LINKS
       ===================================================== */

    const internalLinks =
        document.querySelectorAll(
            'a[href^="#"]'
        );


    internalLinks.forEach(
        function (link) {

            link.addEventListener(
                "click",
                function (event) {

                    const targetId =
                        link.getAttribute(
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

});
/* =========================================================
   MIDHLAJ DEV — PROJECT FILTER
========================================================= */

document.addEventListener(
    "DOMContentLoaded",
    function () {

        const filterButtons =
            document.querySelectorAll(
                ".filter-btn"
            );


        const projectItems =
            document.querySelectorAll(
                ".project-item"
            );


        if (
            !filterButtons.length ||
            !projectItems.length
        ) {
            return;
        }


        filterButtons.forEach(
            function (button) {

                button.addEventListener(
                    "click",
                    function () {


                        /* =================================
                           ACTIVE BUTTON
                        ================================= */

                        filterButtons.forEach(
                            function (btn) {

                                btn.classList.remove(
                                    "active"
                                );

                            }
                        );


                        button.classList.add(
                            "active"
                        );


                        /* =================================
                           FILTER VALUE
                        ================================= */

                        const filter =
                            button.dataset.filter;


                        /* =================================
                           FILTER PROJECTS
                        ================================= */

                        projectItems.forEach(
                            function (item) {

                                const categories =
                                    item.dataset.category || "";


                                const shouldShow =
                                    filter === "all" ||
                                    categories
                                        .split(" ")
                                        .includes(filter);


                                if (shouldShow) {

                                    item.style.display =
                                        "";

                                    requestAnimationFrame(
                                        function () {

                                            item.style.opacity =
                                                "1";

                                            item.style.transform =
                                                "translateY(0)";

                                        }
                                    );

                                } else {

                                    item.style.opacity =
                                        "0";

                                    item.style.transform =
                                        "translateY(15px)";


                                    setTimeout(
                                        function () {

                                            item.style.display =
                                                "none";

                                        },
                                        200
                                    );

                                }

                            }
                        );

                    }
                );

            }
        );

    }
);
document.addEventListener("DOMContentLoaded", function () {

    const filterButtons =
        document.querySelectorAll(".project-filter-btn");

    const projectItems =
        document.querySelectorAll(".project-item");

    const noResults =
        document.getElementById("noFilterResults");


    filterButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            const filter =
                this.dataset.filter;


            filterButtons.forEach(function (btn) {

                btn.classList.remove("active");

            });


            this.classList.add("active");


            let visibleCount = 0;


            projectItems.forEach(function (item) {

                const category =
                    item.dataset.category;


                if (
                    filter === "all" ||
                    category === filter
                ) {

                    item.classList.remove(
                        "filter-hidden"
                    );

                    visibleCount++;

                } else {

                    item.classList.add(
                        "filter-hidden"
                    );

                }

            });


            if (noResults) {

                noResults.style.display =
                    visibleCount === 0
                        ? "block"
                        : "none";

            }

        });

    });

});
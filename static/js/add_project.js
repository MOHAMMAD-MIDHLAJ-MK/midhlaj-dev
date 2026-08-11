document.addEventListener("DOMContentLoaded", function () {

    /* =====================================================
       ELEMENTS
    ===================================================== */

    const form =
        document.getElementById("projectForm");

    const container =
        document.getElementById("contentContainer");

    const addImageBtn =
        document.getElementById("addImageBtn");

    const addVideoBtn =
        document.getElementById("addVideoBtn");

    const limitText =
        document.getElementById("contentLimit");


    let imageCount = 0;
    let videoCount = 0;
    let contentCount = 0;



    /* =====================================================
       COVER IMAGE PREVIEW
    ===================================================== */

    const coverInput =
        document.querySelector(
            "#id_cover_image"
        );

    const coverPreview =
        document.getElementById(
            "coverPreview"
        );


    if (coverInput) {

        coverInput.addEventListener(
            "change",
            function () {

                coverPreview.innerHTML = "";

                const file =
                    this.files[0];

                if (!file) {
                    return;
                }


                if (
                    !file.type.startsWith(
                        "image/"
                    )
                ) {
                    return;
                }


                const reader =
                    new FileReader();


                reader.onload =
                    function (event) {

                        coverPreview.innerHTML = `
                            <div class="preview-image-wrap">

                                <img
                                    src="${event.target.result}"
                                    alt="Cover Preview"
                                >

                                <button
                                    type="button"
                                    class="remove-cover"
                                >
                                    <i class="bi bi-x"></i>
                                </button>

                            </div>
                        `;


                        const removeBtn =
                            coverPreview.querySelector(
                                ".remove-cover"
                            );


                        removeBtn.addEventListener(
                            "click",
                            function () {

                                coverInput.value = "";

                                coverPreview.innerHTML = "";

                            }
                        );

                    };


                reader.readAsDataURL(file);

            }
        );

    }



    /* =====================================================
       UPDATE LIMIT
    ===================================================== */

    function updateLimit() {

        limitText.textContent =
            `${imageCount}/10 images • ${videoCount}/10 videos`;


        addImageBtn.disabled =
            imageCount >= 10;


        addVideoBtn.disabled =
            videoCount >= 10;

    }



    /* =====================================================
       CREATE CONTENT
    ===================================================== */

    function addContent(type) {

        if (
            type === "image" &&
            imageCount >= 10
        ) {
            alert(
                "You can add maximum 10 images."
            );

            return;
        }


        if (
            type === "video" &&
            videoCount >= 10
        ) {
            alert(
                "You can add maximum 10 videos."
            );

            return;
        }


        contentCount++;


        if (type === "image") {
            imageCount++;
        } else {
            videoCount++;
        }


        const card =
            document.createElement("div");


        card.className =
            "content-builder-card";


        card.dataset.type =
            type;


        const mediaLabel =
            type === "image"
                ? "Project Image"
                : "Project Video";


        const mediaIcon =
            type === "image"
                ? "bi-image"
                : "bi-play-circle";


        const accept =
            type === "image"
                ? "image/png,image/jpeg,image/jpg,image/webp,image/gif"
                : "video/mp4,video/webm,video/ogg";


        const fileName =
            type === "image"
                ? "content_image"
                : "content_video";


        card.innerHTML = `

            <div class="content-card-top">

                <div class="content-card-title">

                    <span class="content-number">
                        ${String(contentCount).padStart(2, "0")}
                    </span>

                    <div>

                        <span class="content-type-badge">
                            <i class="bi ${mediaIcon}"></i>
                            ${mediaLabel}
                        </span>

                        <h3>
                            ${type === "image"
                                ? "Image Section"
                                : "Video Section"}
                        </h3>

                    </div>

                </div>


                <button
                    type="button"
                    class="remove-content"
                    title="Remove"
                >
                    <i class="bi bi-trash3"></i>
                </button>

            </div>


            <div class="content-card-body">


                <!-- FILE -->

                <div class="content-media-column">

                    <label class="media-upload-label">

                        <i class="bi ${mediaIcon}"></i>

                        <span>
                            Choose ${type}
                        </span>

                        <small>
                            ${type === "image"
                                ? "PNG / JPG / WEBP"
                                : "MP4 / WEBM / OGG"}
                        </small>

                        <input
                            type="file"
                            name="${fileName}"
                            class="media-input"
                            accept="${accept}"
                            required
                        >

                    </label>


                    <div class="media-preview"></div>

                </div>


                <!-- DETAILS -->

                <div class="content-details-column">


                    <div class="field">

                        <label>
                            Content Title
                        </label>

                        <input
                            type="text"
                            name="content_title"
                            class="form-input"
                            placeholder="Example: Login Page"
                        >

                    </div>


                    <div class="field">

                        <label>
                            Description
                        </label>

                        <textarea
                            name="content_paragraph"
                            class="form-input"
                            rows="5"
                            placeholder="Explain this ${type}..."
                        ></textarea>

                    </div>


                    <div class="field order-field">

                        <label>
                            Display Order
                        </label>

                        <input
                            type="number"
                            name="content_order"
                            class="form-input"
                            value="${contentCount}"
                            min="1"
                        >

                    </div>


                </div>

            </div>

        `;


        container.appendChild(card);


        /* =================================================
           FILE PREVIEW
        ================================================= */

        const fileInput =
            card.querySelector(
                ".media-input"
            );


        const preview =
            card.querySelector(
                ".media-preview"
            );


        fileInput.addEventListener(
            "change",
            function () {

                preview.innerHTML = "";


                const file =
                    this.files[0];


                if (!file) {
                    return;
                }


                if (type === "image") {

                    const reader =
                        new FileReader();


                    reader.onload =
                        function (event) {

                            preview.innerHTML = `

                                <div class="content-preview-wrap">

                                    <img
                                        src="${event.target.result}"
                                        alt="Preview"
                                    >

                                    <span class="preview-check">
                                        <i class="bi bi-check-circle-fill"></i>
                                    </span>

                                </div>

                            `;

                        };


                    reader.readAsDataURL(file);

                } else {

                    const video =
                        document.createElement(
                            "video"
                        );


                    video.controls = true;

                    video.preload = "metadata";

                    video.src =
                        URL.createObjectURL(
                            file
                        );


                    preview.appendChild(
                        video
                    );

                }

            }
        );



        /* =================================================
           REMOVE
        ================================================= */

        const removeBtn =
            card.querySelector(
                ".remove-content"
            );


        removeBtn.addEventListener(
            "click",
            function () {

                if (
                    type === "image"
                ) {
                    imageCount--;
                } else {
                    videoCount--;
                }


                card.remove();


                updateNumbers();

                updateLimit();

            }
        );


        updateNumbers();

        updateLimit();

    }



    /* =====================================================
       UPDATE NUMBERS
    ===================================================== */

    function updateNumbers() {

        const cards =
            container.querySelectorAll(
                ".content-builder-card"
            );


        cards.forEach(
            function (card, index) {

                const number =
                    card.querySelector(
                        ".content-number"
                    );


                if (number) {

                    number.textContent =
                        String(
                            index + 1
                        ).padStart(2, "0");

                }


                const order =
                    card.querySelector(
                        ".order-field input"
                    );


                if (order) {

                    order.value =
                        index + 1;

                }

            }
        );

    }



    /* =====================================================
       ADD BUTTONS
    ===================================================== */

    addImageBtn.addEventListener(
        "click",
        function () {

            addContent("image");

        }
    );


    addVideoBtn.addEventListener(
        "click",
        function () {

            addContent("video");

        }
    );



    /* =====================================================
       CATEGORY
    ===================================================== */

    const categoryInput =
        document.getElementById(
            "categoryInput"
        );


    const categoryButtons =
        document.querySelectorAll(
            ".category-option"
        );


    categoryButtons.forEach(
        function (button) {

            button.addEventListener(
                "click",
                function () {

                    categoryInput.value =
                        this.textContent.trim();

                }
            );

        }
    );



    /* =====================================================
       TECHNOLOGY TAGS
    ===================================================== */

    const technologyInput =
        document.getElementById(
            "technologyInput"
        );


    const technologyTags =
        document.getElementById(
            "technologyTags"
        );


    const technologiesHidden =
        document.getElementById(
            "technologiesHidden"
        );


    const techButtons =
        document.querySelectorAll(
            ".tech-option"
        );


    let technologies = [];


    /* Existing */

    const existing =
        technologiesHidden.value.trim();


    if (existing) {

        technologies =
            existing
                .split(",")
                .map(
                    item =>
                        item.trim()
                )
                .filter(
                    item =>
                        item !== ""
                );

    }



    /* =====================================================
       RENDER TECHNOLOGIES
    ===================================================== */

    function renderTechnologies() {

        technologyTags.innerHTML = "";


        technologies.forEach(
            function (
                technology,
                index
            ) {

                const tag =
                    document.createElement(
                        "span"
                    );


                tag.className =
                    "technology-tag";


                tag.innerHTML = `

                    <span>
                        ${technology}
                    </span>

                    <button
                        type="button"
                        data-index="${index}"
                        class="remove-tech"
                    >
                        <i class="bi bi-x"></i>
                    </button>

                `;


                technologyTags.appendChild(
                    tag
                );

            }
        );


        technologiesHidden.value =
            technologies.join(", ");

    }



    /* =====================================================
       ADD TECHNOLOGY
    ===================================================== */

    function addTechnology(value) {

        const technology =
            value.trim();


        if (!technology) {
            return;
        }


        const duplicate =
            technologies.some(
                item =>
                    item.toLowerCase() ===
                    technology.toLowerCase()
            );


        if (duplicate) {

            technologyInput.value = "";

            return;

        }


        technologies.push(
            technology
        );


        technologyInput.value = "";


        renderTechnologies();

    }



    /* ENTER */

    technologyInput.addEventListener(
        "keydown",
        function (event) {

            if (
                event.key === "Enter"
            ) {

                event.preventDefault();

                addTechnology(
                    technologyInput.value
                );

            }

        }
    );



    /* OPTIONS */

    techButtons.forEach(
        function (button) {

            button.addEventListener(
                "click",
                function () {

                    addTechnology(
                        this.textContent
                    );

                }
            );

        }
    );



    /* REMOVE */

    technologyTags.addEventListener(
        "click",
        function (event) {

            const button =
                event.target.closest(
                    ".remove-tech"
                );


            if (!button) {
                return;
            }


            const index =
                Number(
                    button.dataset.index
                );


            technologies.splice(
                index,
                1
            );


            renderTechnologies();

        }
    );


    renderTechnologies();



    /* =====================================================
       FORM SUBMIT LOADING
    ===================================================== */

    form.addEventListener(
        "submit",
        function () {

            const button =
                document.getElementById(
                    "createProjectBtn"
                );


            if (button) {

                button.classList.add(
                    "loading"
                );


                button.disabled = true;

            }

        }
    );


    /* =====================================================
       DRAG & DROP COVER
    ===================================================== */

    const coverZone =
        document.getElementById(
            "coverUploadZone"
        );


    if (coverZone && coverInput) {

        [
            "dragenter",
            "dragover"
        ].forEach(
            eventName => {

                coverZone.addEventListener(
                    eventName,
                    function (event) {

                        event.preventDefault();

                        coverZone.classList.add(
                            "dragging"
                        );

                    }
                );

            }
        );


        [
            "dragleave",
            "drop"
        ].forEach(
            eventName => {

                coverZone.addEventListener(
                    eventName,
                    function (event) {

                        event.preventDefault();

                        coverZone.classList.remove(
                            "dragging"
                        );

                    }
                );

            }
        );


        coverZone.addEventListener(
            "drop",
            function (event) {

                const files =
                    event.dataTransfer.files;


                if (
                    files.length
                ) {

                    coverInput.files =
                        files;


                    coverInput.dispatchEvent(
                        new Event(
                            "change"
                        )
                    );

                }

            }
        );

    }



    /* =====================================================
       INITIAL
    ===================================================== */

    updateLimit();

});
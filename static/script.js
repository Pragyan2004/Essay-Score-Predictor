document.addEventListener("DOMContentLoaded", function () {
    const textarea = document.querySelector("#essay");
    const wordCountDisplay = document.querySelector("#word-count");
    const charCountDisplay = document.querySelector("#char-count");
    const fileInput = document.querySelector("#file-input");
    const sampleBtn = document.querySelector("#sample-btn");

    function updateCounts() {
        const text = textarea.value.trim();
        const words = text.split(/\s+/).filter(word => word.length > 0);
        wordCountDisplay.textContent = `Word Count: ${words.length}`;
        charCountDisplay.textContent = `Character Count: ${text.length}`;
    }

    textarea.addEventListener("input", updateCounts);

    fileInput.addEventListener("change", function () {
        const file = fileInput.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                textarea.value = e.target.result;
                updateCounts();
            };
            reader.readAsText(file);
        }
    });

    sampleBtn.addEventListener("click", function () {
        textarea.value = "This is a sample essay demonstrating excellent structure, coherence, and depth of thought. It includes diverse vocabulary and clear argumentation.";
        updateCounts();
    });
});
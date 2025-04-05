let editor, afteditr, afteditr2;
const uploadButton = document.getElementById("uploadButton");
const fileInput = document.getElementById("fileInput");
const result = document.getElementById("result");

window.onload = function () {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/python"); 
    editor.setFontSize(16);

    afteditr = ace.edit("afteditr");
    afteditr.setTheme("ace/theme/monokai");
    afteditr.session.setMode("ace/mode/python");
    afteditr.setReadOnly(true);
    afteditr.setFontSize(15);

    afteditr2 = ace.edit("afteditr2");
    afteditr2.setTheme("ace/theme/monokai");
    afteditr2.session.setMode("ace/mode/text");
    afteditr2.setReadOnly(true);
    afteditr2.setFontSize(15);
};

function changeLanguage() {
    const language = $("#languages").val();
    if (language === "c" || language === "cpp") {
        editor.session.setMode("ace/mode/c_cpp");
    } else if (language === "php") {
        editor.session.setMode("ace/mode/php");
    } else if (language === "python") {
        editor.session.setMode("ace/mode/python");
    } else if (language === "node") {
        editor.session.setMode("ace/mode/javascript");
    }
}

function runCode() {
    const code = editor.getValue();

    fetch(`${window.location.origin.replace(/:\d+$/, ":5000")}/api/bugfix`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.fixed_code) {
            afteditr.setValue(data.fixed_code, -1);
            afteditr2.setValue(data.logs || "AI-generated fix applied.", -1);
        } else {
            afteditr.setValue("// Fix failed", -1);
            afteditr2.setValue(data.error || "Unknown error", -1);
        }
    })
    .catch(error => {
        afteditr.setValue("// Server error", -1);
        afteditr2.setValue("Error: " + error.message, -1);
    });
}

// Upload button
uploadButton.addEventListener("click", () => {
    fileInput.click();
});

fileInput.addEventListener("change", async () => {
    const file = fileInput.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function (e) {
        editor.setValue(e.target.result, -1);
    };
    reader.readAsText(file);
});

<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $language = strtolower($_POST['language']);
    $code = $_POST['code'];

    $random = substr(md5(mt_rand()), 0, 7);
    $ext = ($language === "python") ? "py" : (($language === "node") ? "js" : $language);
    $filePath = "temp/" . $random . "." . $ext;

    if (!is_dir("temp")) {
        mkdir("temp", 0777, true);
    }

    $programFile = fopen($filePath, "w");
    fwrite($programFile, $code);
    fclose($programFile);

    echo json_encode(["status" => "success", "filePath" => $filePath]);
} else {
    echo json_encode(["status" => "error", "message" => "Invalid request."]);
}
?>

<?php
header('Content-Type: text/html; charset=utf-8');

$to = 'info@spadeluxe.cz'; // Target email
$subject_prefix = '[WEBSITE INQUIRY]';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect and sanitize input data
    $name = strip_tags(trim($_POST["fullname"]));
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $phone = strip_tags(trim($_POST["phone"]));
    $program_type = strip_tags(trim($_POST["program_type"])); // From dropdown
    $date_pref = strip_tags(trim($_POST["date_pref"]));
    $message = strip_tags(trim($_POST["message"])); // "How can we help you"
    $diet_needs = strip_tags(trim($_POST["diet_needs"])); // Specific needs

    // Validation
    if (empty($name) || empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "<script>alert('Please fill in all required fields correctly.'); window.history.back();</script>";
        exit;
    }

    // Email Subject
    $subject = "$subject_prefix New booking request from $name";

    // Email Body
    $email_content = "Name: $name\n";
    $email_content .= "Email: $email\n";
    $email_content .= "Phone: $phone\n\n";
    $email_content .= "--- REQUEST DETAILS ---\n";
    $email_content .= "Program Type: $program_type\n";
    $email_content .= "Preferred Date: $date_pref\n";
    $email_content .= "Message/Help: $message\n";
    $email_content .= "Diet/Specific Needs: $diet_needs\n";

    // Email Headers
    $headers = "From: no-reply@spadeluxe.cz\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Send logic
    if (mail($to, $subject, $email_content, $headers)) {
        // Redirect back with success flag
        header("Location: index.html?status=success");
        exit;
    } else {
        echo "<script>alert('System error. Please try again later.'); window.history.back();</script>";
    }
} else {
    // Not a POST request
    header("Location: index.html");
    exit;
}
?>

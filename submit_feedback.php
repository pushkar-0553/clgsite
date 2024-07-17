<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $feedback = htmlspecialchars($_POST['feedback']);

    // Here, you can store the feedback in a database or send it via email
    // Example: Send an email with the feedback
    $to = "pushkarakagitha@gmail.com";
    $subject = "Website Feedback from " . $name;
    $message = "Name: " . $name . "\nEmail: " . $email . "\n\nFeedback:\n" . $feedback;
    $headers = "From: " . $email;

    if (mail($to, $subject, $message, $headers)) {
        echo "Thank you for your feedback!";
    } else {
        echo "Sorry, there was an error sending your feedback. Please try again later.";
    }
}
?>

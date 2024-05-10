<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $name = $_POST["name"];
    $email = $_POST["email"];
    $phone = $_POST["phone"];
    $message = $_POST["message"];

    $to = "vishnuk2259@gmail.com";
    $subject = "New Contact Form Submission";
    $email_body = "Name: $name\nEmail: $email\nPhone: $phone\nMessage: $message";

    
    if (mail($to, $subject, $email_body, $headers)) {
        echo "Email sent successfully.";
    } else {
        echo "Failed to send email.";
    }
} else {
    echo "Form submission error.";
}


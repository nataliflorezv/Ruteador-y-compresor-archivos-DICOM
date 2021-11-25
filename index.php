<?php
  session_start();

  require 'database.php';

  if (isset($_SESSION['user_id'])) {
    $records = $conn->prepare('SELECT id, name, password FROM users WHERE id = :id');
    $records->bindParam(':id', $_SESSION['user_id']);
    $records->execute();
    $results = $records->fetch(PDO::FETCH_ASSOC);

    $user = null;

    if (count($results) > 0) {
      $user = $results;
    }
  }
?>

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Welcome to you WebApp</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    body, html {
      height: 100%;
      margin: 0;

    }

    .bg {
      /* The image used */
      background-image: url(fondo.jpg);
      /* Full height */
      color: white;
      padding: 100px;
      height: 100%; 

      /* Center and scale the image nicely */
      background-position: center;
      background-repeat: no-repeat;
      background-size: cover;
    }
    </style>

  </head>
  <body>
    <div class="bg">
    <?php if(!empty($user)): ?>
      <h1><br> Bienvenido. <?= $user['name']; ?>
      <br>Accediste de manera correcta </h1>
      <h2><br>Elije una opción: </h2>
      
      <h2><a href="inicio.php" style="color: #1ff00c";><br>
        Entrar a la plataforma de ImgMedic
      <a href="logout.php" style="color: red";><br>
        Logout
      </a></h2>
    <?php else: ?>
      <h1>Please Login or SignUp</h1>

      <a href="login.php">Login</a> or
      <a href="signup.php">SignUp</a>
    <?php endif; ?>
    </div>
  </body>
</html>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Formulario Login</title>
    <link href="assets/css/estilos.css" type="text/css" rel="stylesheet" media="">
  </head>
  
  <body>


    <div class="contenedor">
      <h2>Login</h2>
      <form id="forma" name="forma">
        <div class="elemento">
          <label for="usuario">Usuario</label>
          <input type="text" id="usuario" name="usuario" required="true" />
        </div>
        <div class="elemento">
          <label for="password">Password</label>
          <input
            type="password"
            id="password"
            name="password"
            required="true"
          />
        </div>
        <div class="elemento">
          <input type="submit" value="INGRESAR" />
        </div>
      </form>
    </div>

  </body>
</html>
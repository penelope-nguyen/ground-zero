<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title></title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="styles.css" rel="stylesheet">

    <link href="https://fonts.googleapis.com/css?family=Roboto:300|Raleway|Ubuntu|Oswald" rel="stylesheet">

    <style>
       #map {
        height: 400px;
        width: 100%;
       }
    </style>

  </head>

  <body>

    <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
      <a class="navbar-brand" href="#">GROUND ZERO</a>
      <ul class="navbar-nav ml-auto">
        <li class="nav-item active">
          <a class="nav-link" href="#">Sign Up <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Log in</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Log out</a>
        </li>
    </ul>

    </nav>

    <div class = "banner">
      <div class = "img">
        <div class = "text">
          CROWD SOURCED EMERGENCY RELIEF
        </div>
      </div>
    </div>

    <div class = "main">

      <div class ="row">
        <div class = "col-sm-12 col-lg-4 center">
          <p>ping info info about ping please create ping</p>
          <a class="btn btn-danger btn-lg xl" href="submit.html" role="button">Send flare</a>
        </div>

        <div class = "col-sm-12 col-lg-8 center main">
          <div id = "map"></div>
          <div class = "row">
            <div class = "col-sm-6 col-lg-6 center bottom">
              <button type="button" class="btn btn-info round">Filters</button>
            </div>
            <div class = "col-sm-6 col-lg-6 center bottom">
              <a class="btn btn-warning round" href="listings.html" role="button">Listings</a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <script>
      function initMap() {
        var uluru = {lat: -25.363, lng: 131.044};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: uluru
        });
        var marker = new google.maps.Marker({
          position: uluru,
          map: map
        });
      }
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBB-l6MJLNO4Iuev0W_MDsGOY4C0ndtGF8&callback=initMap">
    </script>

    <div class = "footer">

      <div class = "container">

      </div>

    </div>



    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="assets/js/vendor/jquery.min.js"><\/script>')</script>
    <script src="assets/js/vendor/popper.min.js"></script>
    <script src="js/bootstrap.min.js"></script>

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>

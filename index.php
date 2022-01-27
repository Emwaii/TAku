<!doctype html>
<html lang="en">
  <head>
    <link href="css/bootstrap.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <title>MYHome</title>
    <link rel="icon" href="dataset/Yuli/1.jpg">
  </head>
  <body>
    <nav class="navbar navbar-expand-lg bg-dark">
        <div class="container-fluid">
            <h2><a class="navbar-brand text-light" href="#">MYHome</a></h2>
        </div>
    </nav>
    <form method="post"> 
        <div class="container-fluid">      
            <div class="row gap-3 p-3">
                <div class="card col-md-2 p-2" style="width: 14rem;">
                    <div class="card-body">
                        <h5 class="card-title">Tambah Dataset</h5>
                        <p class="card-text">Mengambil beberapa foto dan akan digunakan sebagai sampel pada training data.</p>
                        <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
                        <input type="submit" class="btn btn-primary" name="tambah" value="Tambah data">

                    </div>
                </div> 
                <div class="card col-md-2 p-2" style="width: 14rem;">
                    <!-- <img src="test.jpg" class="card-img-top"> -->
                    <div class="card-body">
                        <h5 class="card-title">Training Dataset</h5>
                        <p class="card-text">Melatih sampel foto sebelumnya dan mengambil nilai histogram dari sampel tersebut.</p>
                        <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
                        <input type="submit" class="btn btn-warning text-light" name="train" value="Melatih data">
                    </div>
                </div>
                <div class="card col-md-2 p-2" style="width: 14rem;">
                    <div class="card-body">
                        <h5 class="card-title">Testing Program</h5>
                        <p class="card-text">Menggunakan data yang sudah dilatih untuk mendeteksi dan mengenali nama seseorang.</p>
                        <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
                        <input type="submit" class="btn btn-success " name="test" value="Testing Program">

                    </div>
                </div>
            </div>
        </div>
        <!-- <input type="submit" class="btn btn-primary btn-lg" name="tambah" value="Tambah data"> -->
        <!-- <input type="submit" class="btn btn-warning btn-lg text-light" name="train" value="Training data"> -->
        <!-- <input type="submit" class="btn btn-success btn-lg" name="test" value="Testing"> -->
        <!-- <input type="submit" class="btn btn-secondary btn-lg" name="prototype" value="Prototype"> -->
        
    </form>
        <?php
         ini_set('MAX_EXECUTION_TIME', 0);

        if(array_key_exists('tambah', $_POST)) {
            tambah();
        }
        else if(array_key_exists('train', $_POST)) {
            train();
        }
        else if(array_key_exists('test', $_POST)) {
            test();
        }
        else if(array_key_exists('prototype', $_POST)) {
            proto();
        }

        function tambah() {
            shell_exec('python dataset_2.py');
        }
        function train() {
            shell_exec('python training.py');
        }
        function test() {
            shell_exec('python Final_Code.py');
        }
        
        // function proto() {
        //     shell_exec('python test.py');
        // }
        ?>  
    </body>
</html>

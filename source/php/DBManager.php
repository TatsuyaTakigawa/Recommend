<?php
    function getDB(){
        $pdo = new PDO('mysql:host=tutorial-db-instance.czkelgm3rry3.us-east-1.rds.amazonaws.com;dbname=sample;charset=utf8'
            ,'tutorial_user'
            ,'tutorial_user');
        return $pdo;
    }
?>
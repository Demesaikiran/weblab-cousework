<?php

    /**
     * Connects to the database and executes the passed query
     * @param {boolean} query The query string
     * @param {isUpdate} Boolean flag to mark if the query updates the database
     */
    function run_query($query, $isUpdate) {
        $conn = new mysqli('localhost', 'root', '', 'bank');
        //debug_to_console($query);
        if ($conn->connect_error) 
            die('Unable to connect to the database : ' . $conn->connect_error);
        else {
            $result = $conn->query($query);
            if ($isUpdate == false) {
                $txt = json_encode(mysqli_fetch_all($result, MYSQLI_ASSOC));
                echo $txt;
            }
            else
                echo "{}";
            $conn->close();
        }
    }


    // cases based on the different possible queries
    switch ($_POST["query"]) 
    {
        case 'get_client':
            run_query("select Name as name from account where AccNo=".$_POST["acno"], false);
        break;
        
        case 'login':
            run_query("select count(AccNo) as entries from account where AccNo=".$_POST["acno"]." and Password='".$_POST["pass"]."'",false);
        break;

        case 'check_acc':
            run_query("select count(AccNo) as present from account where AccNo=".$_POST["acno"],false);
        break;
        
        case 'insert_client':
            run_query("insert into account values(".$_POST["acno"].", '".$_POST["bal"]."', '".$_POST["pass"]."', '".$_POST["name"]."', ".$_POST["phone"].", '".$_POST["addr"]."', ".$_POST["age"].")", true);
            // run_query("insert into balance values(".$_POST["acno"].", ".$_POST["bal"].")", true);
        break;
        
        case 'get_bal' :
            run_query("select balance from account where AccNo=".$_POST["acno"],false);
        break;

        case 'get_debits' :
            run_query("select AccDest as sentTo, TDate as date, Amount as amount from transactions where AccSource=".$_POST["acno"]."",false);
        break;

        case 'get_credits' :
            run_query("select AccSource as receivedFrom, TDate as date, Amount as amount from transactions where AccDest=".$_POST["acno"]."",false);
        break;

        case 'check_ben':
            run_query("select count(*) as beneficiaries from benificiary where AccSource=".$_POST["source"]." and AccDest=".$_POST["dest"],false);
        break;

        case 'add_ben':
            run_query("insert into benificiary values(".$_POST["source"].", ".$_POST["dest"].")", true);
        break;

        case 'del_ben':
            run_query("delete from benificiary where AccSource=".$_POST["source"]." and AccDest=".$_POST["dest"], true);
        break;
        
        case 'get_ben':
            run_query("select AccDest as ben from benificiary where AccSource=".$_POST["acno"],false);
        break;

        case 'transact':
            run_query("insert into transactions values('".$_POST["dat"]."', ".$_POST["source"].", ".$_POST["dest"].", ".$_POST["amount"].")", true);
            run_query("update account set Balance = Balance - ".$_POST["amount"]." where AccNo=".$_POST["source"], true);
            run_query("update account set Balance = Balance + ".$_POST["amount"]." where AccNo=".$_POST["dest"], true);
        break;
    }
?>


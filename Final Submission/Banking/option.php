<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
        <title>SCIS BANK</title>
        <!--BOOTSTRAP LINK-->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">
        <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js"></script>

        <link rel="stylesheet" href="">
        <link
            href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,200;0,400;0,600;1,200;1,400;1,600&display=swap"
            rel="stylesheet">
        

    </head>
    
    <body>
        <section class="text-gray-600 body-font" id = "header">

            <div class="container px-5 py-24 mx-auto">
                <div class="flex flex-col text-center w-full mb-20">
                    <h1 class="sm:text-3xl text-2xl font-medium title-font text-gray-900">Welcome back to the SCIS BANK</h1>
                    <h2 class="text-xs text-blue-500 tracking-widest font-medium title-font mb-1">Choose the below options</h2>
                    <!-- <h3>id="profileName"</h3> -->
                </div>
                <div class="flex flex-wrap -m-4">
                <div class="p-4 md:w-1/3">
                    <div class="flex rounded-lg h-full bg-gray-100 p-8 flex-col">
                        <div class="flex items-center mb-3">
                            <div class="w-8 h-8 mr-3 inline-flex items-center justify-center rounded-full bg-blue-500 text-white flex-shrink-0">
                                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
                                    <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
                                </svg>
                            </div>
                            <h2 class="text-gray-900 text-lg title-font font-medium">Balance</h2>
                        </div>
                    <div class="flex-grow">
                        <p class="leading-relaxed text-base"> Click the below button to check your Account Balance.<br><br></p>
                        <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myModal1" onclick="get_balance()">
                            Click here
                        </button>
                        </a>
                    </div>
                    </div>
                    <!-- The Modal -->
                    <div class="modal fade" id="myModal1">
                            <div class="modal-dialog">
                                <div class="modal-content">

                                    <!-- Modal Header -->
                                    <div class="modal-header">
                                        <h4 class="modal-title">Your Account balance is:</h4>
                                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                                    </div>

                                    <!-- Modal body -->
                                    <div class="modal-body">
                                        <p> Balance (in INR):</p>
                                        <p id="showBal"></p>
                                    </div>

                                </div>
                            </div>
                        </div>
                </div>
                <div class="p-4 md:w-1/3">
                    <div class="flex rounded-lg h-full bg-gray-100 p-8 flex-col">
                    <div class="flex items-center mb-3">
                        <div class="w-8 h-8 mr-3 inline-flex items-center justify-center rounded-full bg-blue-500 text-white flex-shrink-0">
                        <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
                            <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"></path>
                            <circle cx="12" cy="7" r="4"></circle>
                        </svg>
                        </div>
                        <h2 class="text-gray-900 text-lg title-font font-medium">History</h2>
                    </div>
                    <div class="flex-grow">
                        <p class="leading-relaxed text-base"> Click the below button to check your transaction history.<br><br></p>
                        <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myModal2" onclick="get_transactions()">
                            Click here
                        </button>
                        </a>
                    </div>
                    </div>
                    <!-- The Modal -->
                    <div class="modal fade" id="myModal2">
                            <div class="modal-dialog">
                                <div class="modal-content">

                                    <!-- Modal Header -->
                                    <div class="modal-header">
                                        <h4 class="modal-title">Your Account History</h4>
                                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                                    </div>

                                    <!-- Modal body -->
                                    <div class="modal-body">
                                        <p> Online Debit History:</p>
                                        <table id="deb_his" class="table table-striped">
                                            <thead>
                                                <tr>
                                                    <th>Date</th>
                                                    <th>Sent To</th>
                                                    <th>Amount</th>
                                                </tr>
                                            </thead>
                                            <tbody></tbody>
                                        </table>

                                        <p> Online Credit History:</p>
                                        <table id="cred_his" class="table table-striped">
                                            <thead>
                                                <tr>
                                                    <th>Date</th>
                                                    <th>Received From</th>
                                                    <th>Amount</th>
                                                </tr>
                                            </thead>
                                            <tbody></tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </div>
                </div>
                <div class="p-4 md:w-1/3">
                    <div class="flex rounded-lg h-full bg-gray-100 p-8 flex-col">
                    <div class="flex items-center mb-3">
                        <div class="w-8 h-8 mr-3 inline-flex items-center justify-center rounded-full bg-blue-500 text-white flex-shrink-0">
                        <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
                            <circle cx="6" cy="6" r="3"></circle>
                            <circle cx="6" cy="18" r="3"></circle>
                            <path d="M20 4L8.12 15.88M14.47 14.48L20 20M8.12 8.12L12 12"></path>
                        </svg>
                        </div>
                        <h2 class="text-gray-900 text-lg title-font font-medium">Transfer</h2>
                    </div>
                    <div class="flex-grow">
                        <p class="leading-relaxed text-base:"> Click the below button to trnafer the funds to your Benificiaries<br><br></p>
                        <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myModal3">
                            Click here
                        </button>    
                    </div>
                    </div>
                    <!-- The Modal -->
                    <div class="modal fade" id="myModal3" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
                            aria-hidden="true">
                            <div class="modal-dialog">
                                <div class="modal-content">

                                    <!-- Modal Header -->
                                    <div class="modal-header">
                                        <h4 class="modal-title">Transfer Funds</h4>
                                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                                    </div>

                                    <!-- Modal body -->
                                    <div class="modal-body">
                                        <p>You can only send funds to your beneficiaries. For receiving fund contact your beneficiary and request for sending you the fund using this portal.</p> <p><b>Make sure to check balance once before you proceed</b>.</p>
                                        <button type="button" class="btn btn-primary" id="own">Proceed</button>
                                    </div>

                                </div>
                            </div>
                        </div>
                        <!-- second Modal for own acc -->
                        <div class="modal fade" id="myModal31" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
                            aria-hidden="true">
                            <div class="modal-dialog">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h4 class="modal-title" id="myModalLabel">Send Fund</h4>
                                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                                    </div>

                                    <div class="modal-body">
                                        <p>Transfer To Account :</p>
                                        <select id="send_to" class="form-control">
                                            <option value="" disabled selected>Select beneficiary</option>
                                        </select>
                                        <input type="integer" id="amount" class="form-control" placeholder="Transfer amount">
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-primary" onclick="send_fund()">Submit</button>
                                    </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                </div>
                <div class="p-4 md:w-1/3">
                    <div class="flex rounded-lg h-full bg-gray-100 p-8 flex-col">
                        <div class="flex items-center mb-3">
                            <div class="w-8 h-8 mr-3 inline-flex items-center justify-center rounded-full bg-blue-500 text-white flex-shrink-0">
                            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
                                <circle cx="6" cy="6" r="3"></circle>
                                <circle cx="6" cy="18" r="3"></circle>
                                <path d="M20 4L8.12 15.88M14.47 14.48L20 20M8.12 8.12L12 12"></path>
                            </svg>
                            </div>
                            <h2 class="text-gray-900 text-lg title-font font-medium">Add / Remove</h2>
                        </div>
                        <div class="flex-grow">
                            <p class="leading-relaxed text-base"> Click the Below button to add the benificiaries.<br><br></p>
                            <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myModal4">
                                Click here
                            </button>
                            </a>
                        </div>
                    </div>
                
                    <!-- The Modal -->
                    <div class="modal fade" id="myModal4" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
                                aria-hidden="true">
                                <div class="modal-dialog">
                                    <div class="modal-content">

                                        <!-- Modal Header -->
                                        <div class="modal-header">
                                            <h4 class="modal-title">Beneficiary Management</h4>
                                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                                        </div>

                                        <!-- Modal body -->
                                        <div class="modal-body">
                                            <p> Choose any one of them:</p>
                                            <!--<a href="#own">Own Account</a>
                                        <a href="#other">Other Bank</a>-->
                                            <button type="button" class="btn btn-primary" id="add" >Add</button>
                                            <button type="button" class="btn btn-secondary" id="del" >Delete</button>
                                        </div>

                                    </div>
                                </div>
                            </div>
                            <!-- second Modal for add  -->
                            <div class="modal fade" id="myModal41" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
                                aria-hidden="true">
                                <div class="modal-dialog">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <h4 class="modal-title" id="myModalLabel">Add new Beneficiary</h4>
                                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                                        </div>

                                        <div class="modal-body">
                                            <input type="integer" id="addben" class="form-control" name="addben" placeholder="Account Number" />
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-primary" onclick="add_beneficiary()">Submit</button>
                                        </div>
                                        </form>
                                    </div>
                                </div>
                            </div>
                            <!-- second Modal for del -->
                            <div class="modal fade" id="myModal42" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
                                aria-hidden="true">
                                <div class="modal-dialog">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <h4 class="modal-title" id="myModalLabel">Remove existing beneficiary</h4>
                                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                                        </div>

                                        <div class="modal-body">
                                            <select id="added_ben" class="form-control">
                                                <option value="" disabled selected>Select beneficiary</option>
                                            </select>
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-primary" onclick="delete_beneficiary()">Submit</button>
                                        </div>
                                        </form>
                                    </div>
                                </div>
                            </div>
                    </div>  
            </div>
        </section>


        <!--script for transfer section starts-->
        <script type="text/javascript">
            //set button id on click to hide first modal
            $("#own").on("click", function () {
                $('#myModal3').modal('hide');
            });
            //trigger next modal
            $("#own").on("click", function () {
                $('#myModal31').modal('show');
            });
        </script>
        <script type="text/javascript">
            //set button id on click to hide first modal
            $("#other").on("click", function () {
                $('#myModal3').modal('hide');
            });
            //trigger next modal
            $("#other").on("click", function () {
                $('#myModal32').modal('show');
            });
        </script>
        <!--script for transfer section ends-->

        <!--script for add/del section starts-->
        <script type="text/javascript">
            //set button id on click to hide first modal
            $("#add").on("click", function () {
                $('#myModal4').modal('hide');
            });
            //trigger next modal
            $("#add").on("click", function () {
                $('#myModal41').modal('show');
            });
        </script>
        <script type="text/javascript">
            //set button id on click to hide first modal
            $("#del").on("click", function () {
                $('#myModal4').modal('hide');
            });
            //trigger next modal
            $("#del").on("click", function () {
                $('#myModal42').modal('show');
            });
        </script>
        <!--script for add/del section ends-->


        <script type="text/javascript">

            // create an element to hold the account number
            var acno = document.createElement('input');
            acno.id = 'acno';
            acno.type = 'hidden';
            acno.name = 'acno';
            acno.value =  '<?=$_POST['acno']?>';
            document.getElementById("header").appendChild(acno);
            console.log(document.getElementById("acno").value);

            // create an element to hold the blance
            var bal = document.createElement('input');
            bal.id = 'bal';
            bal.type = 'hidden';
            bal.name = 'bal';
            bal.value = 0;
            document.getElementById("header").appendChild(bal);
            
            var del = document.getElementById("del");
            del.addEventListener('click', function(){
                populate_beneficiary("added_ben");
            });

            var own = document.getElementById("own");
            own.addEventListener('click', function(){
                populate_beneficiary("send_to");
            });

            /**
             * Function to send data to another file using HTTP POST method
             * and parse and process the HTTP response
             * @param {string} file Destination file name
             * @param {string} data Data to send
             * @param {string} doSomething Name of the function to process the HTTP response
             */
            function post_data_parse(file, data1, doSomething) {
                var http = new XMLHttpRequest();
                var url = file;
                var params = data1;
                http.open('POST', url, true);
                http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

                http.onreadystatechange = function () {
                    if (http.readyState == 4 && http.status == 200) {
                        console.log(http.responseText);
                        doSomething(JSON.parse(http.responseText));
                    }

                }
                http.send(params);
            }

            /**
             * Function to send data to another file using HTTP POST method
             * @param {string} file Destination file name
             * @param {string} data Data to send
             */
            function post_data(file, data) {
                var http = new XMLHttpRequest();
                var url = file;
                var params = data;
                http.open('POST', url, true);

                //Send the proper header information along with the request
                http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
                http.send(params);
                location.reload();
            }

            /**
             * Populates a dropdown menu 
             * @param {string} elname Name of the dropdown element
             * @param {string} data Data to populate with
             * @param {string} decode_fn Name of the function to decode the data
             */
            function populate_dropdown(elname, data, decode_fn) 
            {
                var select = document.getElementById(elname);
                // reset the dropdown
                let l = select.options.length - 1;
                console.log(l);
                if(l >= 0) {
                    for(let i = l; i >= 0; i--) {
                    select.remove(i);
                    }
                }

                // initialise the dropdown
                for(let i = 0;i < data.length; i++) 
                {
                    let opt = decode_fn(data[i]);
                    let el = document.createElement("option");
                    el.textContent = opt;
                    el.value = opt;
                    select.appendChild(el);
                }
                return select;
            }

            /**
             * Populates the list of beneficiaries in a dropdown element
             * @param {string} elem Name of the dropdown element to populate
             */
            function populate_beneficiary(elem) {
                var acno = encodeURIComponent(document.getElementById("acno").value);
                post_data_parse("query_helper.php", "query=get_ben&acno="+acno, function(x){
                    if(x.length == 0) {
                        alert("No Beneficiary exists!");
                    }
                    else {
                        var select = populate_dropdown(elem, x, function (x) {
                            console.log(x);
                            return x.ben;
                        });
                        select.selectedIndex = 0;
                    }
                });
            }

            /**
             * Validates the input account number
             * @param {string} acno Account number given as input in the page
             */
            function validateAcNo(ac) {
                var regex = /^[0-9]{9}$/;
                if (!regex.test(ac)) {
                    alert("Account Number is incorrect. Please enter your 9 digit Account Number provided by Bank!");
                    return false;
                }
                return true;
            }

            /**
             * Sends a query request to get the current balance of the user
             */
            function get_balance(){
                var acno = encodeURIComponent(document.getElementById("acno").value);
                post_data_parse("query_helper.php", "query=get_bal&acno="+acno, function (response) {
                    document.getElementById("showBal").innerText = response[0].balance;
                    bal.value = document.getElementById("showBal").innerText;
                });
            }

            /**
             * Fills a given table in the page 
             * @param {string} table Name of the table element
             * @param {string} response Data to populate with
             * @param {boolean} send Boolean value to mark which attribute to retrieve from response
             */
            function fill_table(table, response, send) {
                var table = document.getElementById(table).getElementsByTagName('tbody')[0];
                for (let i = 0; i < response.length; i++) {
                    //add a row to the end of the table
                    let row = table.insertRow(-1);
                    // add 3 cells in the new row
                    let cell0 = row.insertCell(0);
                    let cell1 = row.insertCell(1);
                    let cell2 = row.insertCell(2);
                    // set values of the cells
                    cell0.innerText = response[i].date;
                    if(send == true) {
                        //cell1.innerText = response[i].sentTo;
                        var client = encodeURIComponent(response[i].sentTo);
                        post_data_parse("query_helper.php",  "query=get_client&acno="+client, function (res) {
                            cell1.innerText = res[0].name;
                        });
                    }
                    else {
                        var client = encodeURIComponent(response[i].receivedFrom);
                        post_data_parse("query_helper.php",  "query=get_client&acno="+client, function (res) {
                            cell1.innerText = res[0].name;
                        });
                    }
                    cell2.innerText = response[i].amount;
                }
            }

            /**
             * Sends a query request to get the transaction history of the user and
             * fills the transaction tables with the response data
             */
            function get_transactions() {
                var acno = encodeURIComponent(document.getElementById("acno").value);
                post_data_parse("query_helper.php", "query=get_debits&acno="+acno, function (response) {
                    console.log(response);
                    if(response.length == 0) {
                        alert("No Debit History Found!");
                    }
                    else {
                        fill_table("deb_his", response, true);
                    }
                });

                post_data_parse("query_helper.php", "query=get_credits&acno="+acno, function (response) {
                    console.log(response);
                    if(response.length == 0) {
                        alert("No Credit History Found!");
                    }
                    else {
                        fill_table("cred_his", response, false);
                    }
                });      
            }

            /**
             * Adds a new beneficiary if exists
             */
            function add_beneficiary() {
                var acno = encodeURIComponent(document.getElementById("acno").value);
                var benac = encodeURIComponent(document.getElementById("addben").value);
                if(validateAcNo(benac)) {
                    post_data_parse("query_helper.php", "query=check_ben&source="+acno+"&dest="+benac, function (response) {
                        if(response[0].beneficiaries != 0) {
                            alert("Beneficiary already exists!");
                        }
                        else {
                            post_data_parse("query_helper.php", "query=check_acc&acno="+benac, function (res) {
                                if(res[0].present == 0) {
                                    alert("Beneficiary does not exist!");
                                }
                                else {
                                    post_data("query_helper.php", "query=add_ben&source="+acno+"&dest="+benac);
                                    alert("New Beneficiary added!");
                                }
                            });
                        }
                    });
                }
            }

            /**
             * Deletes and existing beneficiary
             */
            function delete_beneficiary() {
                var acno = encodeURIComponent(document.getElementById("acno").value);
                var benac = encodeURIComponent(document.getElementById("added_ben").value);
                if(validateAcNo(benac)) {
                    post_data("query_helper.php", "query=del_ben&source="+acno+"&dest="+benac);
                    alert("Beneficiary deleted!");
                    location.reload();
                }
            }

            /**
             * Transfers funds if enough balance is present
             */
            function send_fund() {
                var acno = encodeURIComponent(document.getElementById("acno").value);
                var benac = encodeURIComponent(document.getElementById("send_to").value);
                var transferAmount = parseInt(encodeURIComponent(document.getElementById("amount").value));
                var currentBal = parseInt(encodeURIComponent(document.getElementById("bal").value));
                console.log(typeof transferAmount);
                console.log(typeof currentBal);
                if(transferAmount >= currentBal) {
                    alert("Transaction Failed due to insufficient balance!");
                }
                else {
                    let today = new Date();
                    let curDate = encodeURIComponent(today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate());
                    post_data("query_helper.php", "query=transact&dat="+curDate+"&source="+acno+"&dest="+benac+"&amount="+transferAmount);
                    alert("Transaction complete!");
                    location.reload();
                }                
            }

            // actions to perfrom when the page loads
            window.onload = (event) => {
                var acno = encodeURIComponent(document.getElementById("acno").value);
                post_data_parse("query_helper.php", "query=get_client&acno="+acno, function (response) {
                    console.log(response);
                    document.getElementById("profileName").innerText = response[0].name;
                });
            };

        </script>
        
    </body>

</html>
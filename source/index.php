<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
        <head>
                <title>Fetch Data from Database</title>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        </head>
        <body bgcolor="#CCFFCC">

                <?php
                        // connect to the database
                        include('connection.php');

                        // get the records from the database
                        if ($result = $mysqli->query("SELECT * FROM servers ORDER BY sn DESC"))
                        {
                                // display records if there are records to display
                                if ($result->num_rows > 0)
                                {
                                        // display records in a table
                                        echo "<table border='1' cellpadding='10'>";
                                        // set table headers
                                        echo "<tr><th>S.No</th><th>Server Name</th><th>IP Address</th><th>Location</th><th>Environment</th><th>Remarks</th></tr>";

                                        while ($row = $result->fetch_object())
                                        {
                                                // set up a row for each record
                                                echo "<tr>";
                                                echo "<td>" . $row->sn . "</td>";
                                                echo "<td>" . $row->servname . "</td>";
                                                echo "<td>" . $row->ip . "</td>";
                                                echo "<td>" . $row->location . "</td>";
                                                echo "<td>" . $row->env . "</td>";
                                                echo "<td>" . $row->remarks . "</td>";
                                                echo "</tr>";
                                        }

                                        echo "</table>";
                                }
                                // if there are no records in the database, display an alert message
                                else
                                {
                                        echo "No results to display!";
                                }
                        }
                        // show an error if there is an issue with the database query
                        else
                        {
                                echo "Error: " . $mysqli->error;
                        }

                        // close database connection
                        $mysqli->close();

                ?>
        </body>
</html>

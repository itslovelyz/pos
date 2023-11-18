<?php
// Step 1: Connect to the database
$servername = "localhost";
$username = "your_username";
$password = "your_password";
$dbname = "gold and perfect";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Step 2: Fetch the data from the database
$sql = "SELECT * FROM dr";
$result = $conn->query($sql);

// Step 3: Create an HTML table to display the data
echo "<table border='1'>
        <tr>
            <th>Column 1</th>
            <th>Column 2</th>
            <th>Column 3</th>
            <th>Column 4</th>
            <th>Column 5</th>
            <th>Column 6</th>
        </tr>";

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo "<tr>";
        echo "<td>" . $row["column1_name"] . "</td>";
        echo "<td>" . $row["column2_name"] . "</td>";
        echo "<td>" . $row["column3_name"] . "</td>";
        echo "<td>" . $row["column4_name"] . "</td>";
        echo "<td>" . $row["column5_name"] . "</td>";
        echo "<td>" . $row["column6_name"] . "</td>";
        echo "</tr>";
    }
} else {
    echo "<tr><td colspan='3'>No results found</td></tr>";
}
echo "</table>";

// Close the database connection
$conn->close();
?>
<?php
$Customer = $_POST['Customer'];
$Address = $_POST['Address'];
$City = $_POST['City'];
$No = $_POST['No'];
$Date = $_POST['Date'];
$TIN = $_POST['TIN'];
$Product = $_POST['Product'];
$Qty = $_POST['Qty'];
$Rate = $_POST['Rate'];
$Total = $_POST['Total'];

$conn = new mysqli('localhost','root','','dr');
if ($conn->connect_error){
    die('Connection Failed : '-$conn->connect_error);
}
else {
    $stmt = $conn->prepare("insert into dr(Customer, Address, City, No, Date, TIN, Product, Qty, Rate, Total) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");
    $stmt->bind_param("sssssssssi", $Customer, $Address, $City, $No, $Date, $TIN, $Product, $Qty, $Rate);
    $stmt->execute();
}
?>
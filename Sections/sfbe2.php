<?php
// filename sfbe2.php
// 2018-08-17 pja made function
// pja 8-2018 original
// input item
// output contents of file named in item
function sfbe1() {
$filename =  $_GET['item'];
$fileToOpen = fopen($filename,"r");
$content = fread($fileToOpen, filesize($filename));
$content = nl2br($content);
fclose($fileToOpen);
return($content);
} // sfbe1
echo(sfbe1());
?>

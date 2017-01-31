<?php
$page = $_SERVER['PHP_SELF'];
$sec = "2";
?>
<html>
<head>
<meta http-equiv="refresh" content="<?php echo $sec?>;URL='<?php echo $page?>'">
<title>
	Showing stats
</title>
</head>
<style>
.style1 {
	margin-left: 50px;
	margin-top: 20px;
	background: #222222;
	color: #ffffff;
}

</style>
<body class="style1">

		<?php 
		system("python ../total.py"); 
		?>
		<p> Total solved cases today: 
			<?php 
 			system("python ../totalall.py")
			?>
		</p>

</body>
</html>

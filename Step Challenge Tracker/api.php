<?php
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json');

$file = __DIR__ . '/data.json';

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    if (file_exists($file)) {
        echo file_get_contents($file);
    } else {
        echo json_encode([
            'currentSteps' => 0,
            'completedStars' => new stdClass(),
            'completionDates' => new stdClass(),
            'lastUpdated' => null
        ]);
    }
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $input = file_get_contents('php://input');
    $data = json_decode($input, true);
    if ($data !== null) {
        $data['lastUpdated'] = date('c');
        $result = file_put_contents($file, json_encode($data));
        if ($result !== false) {
            echo json_encode(['success' => true, 'path' => $file]);
        } else {
            http_response_code(500);
            echo json_encode(['error' => 'Failed to write file', 'path' => $file]);
        }
    } else {
        http_response_code(400);
        echo json_encode(['error' => 'Invalid JSON']);
    }
    exit;
}

http_response_code(405);
echo json_encode(['error' => 'Method not allowed']);
?>

<?php
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json');

$base = __DIR__;
$file = $base . '/data.json';
$excFile = $base . '/exceptions.json';

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

// GET ?type=exceptions -> return exceptions.json
if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['type']) && $_GET['type'] === 'exceptions') {
    if (file_exists($excFile)) {
        echo file_get_contents($excFile);
    } else {
        echo json_encode(['exceptions' => new stdClass()]);
    }
    exit;
}

// GET ?type=data -> return data.json (default)
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

// POST -> update data.json
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

// POST ?type=exceptions -> update exceptions.json
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_GET['type']) && $_GET['type'] === 'exceptions') {
    $input = file_get_contents('php://input');
    $data = json_decode($input, true);
    if ($data !== null) {
        $result = file_put_contents($excFile, json_encode($data, JSON_PRETTY_PRINT));
        if ($result !== false) {
            echo json_encode(['success' => true, 'path' => $excFile]);
        } else {
            http_response_code(500);
            echo json_encode(['error' => 'Failed to write exceptions file', 'path' => $excFile]);
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

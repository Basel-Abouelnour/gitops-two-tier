const express = require('express');
const app = express();
const PORT = 5000;

app.get('/data', (req, res) => {
    res.json({
        status: "success",
        message: "Hello from the backend-service!",
        timestamp: new Date()
    });
});

app.listen(PORT, '0.0.0.0', () => {
    console.log(`Backend service running on port ${PORT}`);
});
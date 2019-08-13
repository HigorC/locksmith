const express = require('express');
const router = express.Router();

router.post('/create', function (req, res) {
    console.log(req.body);
    console.log(req.params);
    
    res.send("Yes, It Works!")
});

module.exports = router;
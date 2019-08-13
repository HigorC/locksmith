const express = require("express");
const app = express();
const port = process.env.PORT || 3000;

const testRoutes = require('./routes/test');

app.use('/', testRoutes);

app.listen(port, () => {
    console.log(`>> A todo vapor na porta ${port}`);
})
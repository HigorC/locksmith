const express = require("express");
const app = express();
const port = process.env.PORT || 3000;

const testRoutes = require('./routes/test');
const creatorRoutes = require('./routes/creator');

app.use('/', testRoutes);
app.use('/', creatorRoutes);

app.use(express.json());

app.listen(port, () => {
    console.log(`>> A todo vapor na porta ${port}`);
})
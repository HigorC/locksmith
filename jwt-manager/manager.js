const jwt = require('jsonwebtoken');

const secretToEntry = process.env.SECRET_TO_ENTRY || "just-in-local";
const secretToCreate = process.env.SECRET_TO_CREATE || "just-in-local";
const timeToExpire = process.env.SECRET_TO_CREATE || 60; //seconds

function createTokenJWT(secret, object) {
    if (secret != secretToEntry) return res.status(401).send({ message: 'Você não tem o que é preciso para me utilizar.' });

    return jwt.sign(object, secretToCreate, { expiresIn: timeToExpire });
}

module.exports = {
    createTokenJWT
}
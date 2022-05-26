const mysql = require("mysql2/promise")

const pool = mysql.createPool({
    host : "aws server ip",
    user : "mysql user name",
    password:"mysql user password",
    database: "mysql database name",
    waitForConnections: true,
    connectionLimit: 10,
    queueLimit: 0,
});

module.exports = {pool};

const express = require("express");
const morgan = require("morgan");

const {pool} = require("./db");
const app = express();
const PORT = 8081;
app.use(morgan("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
const cors = require("cors");
app.use(
	cors({
		origin: true,
	})
);

const server = require("http").createServer(app);
const io = require("socket.io")(server, {
	pingTimeout: 1,
	pingInterval: 10000,
});

io.on("connection", async (socket)=>{
	console.log("user connected");
	try{
		const data = await pool.query("select * from sensing order by time desc limit 15");
		socket.emit("getData", data[0]);
	}catch(error){
		console.log(error);
	}
});

server.listen(PORT, () => console.log(`this server listening on ${PORT}`))
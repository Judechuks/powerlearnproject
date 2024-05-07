const express = require("express");
const bodyParser = require("body-parser");
const app = express();
const PORT = 3100;
const { default: mongoose } = require("mongoose");

app.use(bodyParser.json());

mongoose.connect("mongodb://127.0.0.1:27017/items", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const db = mongoose.connection;

db.on("error", console.error.bind(console, "MongoDB connection error:"));

app.use("/products", require("./routes/products"));

app.listen(PORT, () => {
  console.log(`Server is running on port: ${PORT}`);
  console.log(`alt + click http://localhost:${PORT}/products`);
});

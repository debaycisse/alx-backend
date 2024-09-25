import redis from 'redis';
const kue = require('kue');
const util = require('util');
const express = require('express');

const client = redis.createClient();
const queue = kue.createQueue();
const app = express();
const port = 1245;

let numberOfSeatAvailable = 50;
let reservationEnabled = true;  // it will be turn to false when no seat will be available

const reserveSeat = (number) => {
  // Note that number must be a string
  client.set('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const getAsync = util.promisify(client.get).bind(client);
  const result = await getAsync('available_seats');
  return result;
};

app.get('/available_seats', (req, res) => {
  res.json({ "numberOfAvailableSeats": numberOfSeatAvailable });
});

app.get('/reserve_seat', (req, res) => {
  if(!reservationEnabled) {
    return res.json({ "status": "Reservation are blocked" });
  }
  queue.create('reserve_seat', );
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});

// When launching the application, set the number of available to 50
module.exports = app;

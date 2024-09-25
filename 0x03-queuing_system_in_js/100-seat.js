import redis from 'redis';
const kue = require('kue');
const util = require('util');
import { promisify } from 'util';
const express = require('express');

const client = redis.createClient();
const queue = kue.createQueue();
const app = express();
const port = 1245;
let numberOfSeatAvailable = 50;
let reservationEnabled = true;

const reserveSeat = async (number) => {
  const asyncSet = promisify(client.set).bind(client);
  const _value = await asyncSet('available_seat', String(number));
  numberOfSeatAvailable -= 1;
  return _value;
};

const getCurrentAvailableSeats = async () => {
  const getAsync = util.promisify(client.get).bind(client);
  const availableSeats = await getAsync('available_seats');

  if(availableSeats !== null && availableSeats !== undefined) {
    return availableSeats;
  }
  return numberOfSeatAvailable;
};

app.get('/available_seats', (req, res) => {
  res.json({ 'numberOfAvailableSeats': String(numberOfSeatAvailable) });
});

app.get('/reserve_seat', (req, res) => {
  if(reservationEnabled === false) {
    return res.json({ 'status': 'Reservation are blocked' });
  } else {
    try {
      queue.on('job complete', (id, result) => {
        console.log(`Seat reservation job ${id} completed`);
      });

      queue.on('job failed', (id, error) => {
        console.log(`Seat reservation job ${id} failed: ${error}`);
      });

      const job = queue.create('reserve_seat')
        .save((error) => {
          if(error) {
            console.error('error occured while saving job');
            return;
          } else {
            return res.json({ 'status': 'Reservation in process' });
          };
        });
    } catch(error) {
      res.json({ 'status': 'Reservation failed' });
    }
  }
});

app.get('/process', (req, res) => {
  queue.process('reserve_seat', (job, done) => {
    getCurrentAvailableSeats()
      .then((result) => {
        let availableSeatNum = Number.parseInt(result);
        if(availableSeatNum <= 0) {
          reservationEnabled = false;
          const err = new Error('Not enough seats available');
          done(err.message);
        } else {
          reserveSeat(availableSeatNum - 1)
            .then(() => {
              done();
            });
        };
      });
  });
  res.json({ 'status': 'Queue processing' });
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});

module.exports = app;

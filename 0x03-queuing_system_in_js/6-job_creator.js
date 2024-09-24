const kue = require('kue');

const jobData = {
  phoneNumber: '005868868',
  message: 'Holberton Student #1 course code',
};

const queue = kue.createQueue();

const job = queue.create('push_notification_code', jobData)
  .save((error) => {
    if (!error) console.log(`Notification job created: ${job.id}`);
  });

queue.on('job failed', (id, result) => {
  console.log('Notification job failed');
});

queue.on('job complete', (id, result) => {
  console.log('Notification job completed');
});

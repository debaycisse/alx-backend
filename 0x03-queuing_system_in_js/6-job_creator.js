const kue = require('kue');

const jobData = {
  phoneNumber: '005868868',
  message: 'Holberton Student #1 course code',
};

const push_notification_code = kue.createQueue();

const job = push_notification_code.create('push notification', jobData)
  .save((error) => {
    if (!error) console.log(`Notification job created: ${job.id}`);
  });

push_notification_code.on('job failed', (id, result) => {
  console.log('Notification job failed');
});

push_notification_code.on('job complete', (id, result) => {
  console.log('Notification job completed');
});

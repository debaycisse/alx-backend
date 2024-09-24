const kue = require('kue');

const blackListed = ['4153518780', '4153518781'];
const queue = kue.createQueue()

function sendNotification(phoneNumber, message, job, done) {
  const prg = 100;
  job.progress(0, prg);
  if (blackListed.includes(phoneNumber)) {
    const err = new Error(`Phone number ${phoneNumber} is blacklisted`);
    done(err);
  } else {
    job.progress(50, prg);
    console.log(
      `Sending notification to ${phoneNumber}, with message: ${message}`
    );
    done();
  }
};

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

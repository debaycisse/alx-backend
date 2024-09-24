const kue = require('kue');

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account',
  },
];

const push_notification_code_2 = kue.createQueue();

push_notification_code_2.on('job complete', (id, result) => {
  console.log(`Notification job ${id} completed`);
});

push_notification_code_2.on('job failed', (id, error) => {
  if (error) console.log(`Notification job ${id} failed: ${error}`);
});

push_notification_code_2.on('job progress', (id, progress) => {
  console.log(`Notification job ${id} ${progress}% complete`);
});
  
for (let i = 0; i < jobs.length; i += 1) {
  const job = push_notification_code_2.create(
    'push notification',
    jobs[i]
  )
    .save((error) => {
      if (!error) console.log(`Notification job created: ${job.id}`);
    });
};

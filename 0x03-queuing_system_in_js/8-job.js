module.exports = function createPushNotificationsJobs(jobs, queue) {
  if(!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  queue.on('job complete', (id, result) => {
    console.log(`Notification job ${id} completed`);
  });

  queue.on('job failed', (id, error) => {
    console.log(`Notification job ${id} failed: ${error.message}`);
  });

  queue.on('job progress', (id, progress) => {
    console.log(`Notification job ${id} ${progress}% complete`);
  });

  for(let i = 0; i < jobs.length; i += 1) {
    const job = queue.create('push_notification_code_3', jobs[i])
      .save((error) => {
        if (!error) console.log(`Notification job created: ${job.id}`);
      });
  }
};

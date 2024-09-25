const kue = require('kue');
const createPushNotificationsJobs = require('./8-job');
const { expect } = require('chai');
const sinon = require('sinon');

describe('createPushNotificationsJobs', () => {
  const queue = kue.createQueue();
  let spiedConsole;
  before(() => {
    queue.testMode.enter();
  });

  after(() => {
    queue.testMode.exit();
  });

  beforeEach(() => {
    if (!spiedConsole) spiedConsole = sinon.spy(console, 'log');
  });

  afterEach(() => {
    spiedConsole.resetHistory();
    queue.testMode.clear();
  });

  it('displays error message if job is not an array', () => {
    const job = {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account',
    };
    expect(() => createPushNotificationsJobs(job, queue)).to.throw(
      'Jobs is not an array'
    );
  });

  it('are jobs successfully stored in queue', () => {
    const job1 = {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account',
    };

    const job2 = {
      phoneNumber: '1953518439',
      message: 'This is the code 5678 to verify your account',
    };

    createPushNotificationsJobs([job1, job2], queue);

    expect(queue.testMode.jobs.length).to.be.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');

    expect(queue.testMode.jobs[0].data).to.deep.equal(job1);
    expect(queue.testMode.jobs[1].data).to.deep.equal(job2);
  });

  it('are the type of jobs stored in queue correct', () => {
    const job1 = {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account',
    };

    const job2 = {
      phoneNumber: '1953518439',
      message: 'This is the code 5678 to verify your account',
    };

    createPushNotificationsJobs([job1, job2], queue);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
  });

  it('does a stored job contain the same data as the one stored', () => {
    const jobs = [
      {
        phoneNumber: '1953518439',
        message: 'This is the code 5678 to verify your account',
      },

      {
        phoneNumber: '1953518439',
        message: 'This is the code 5678 to verify your account',
      },

      {
        phoneNumber: '1953518439',
        message: 'This is the code 5678 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
  });
});

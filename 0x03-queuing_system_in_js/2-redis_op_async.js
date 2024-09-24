import redis from 'redis';

const client = redis.createClient()
const util = require('util');

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
};

async function displaySchoolValue(schoolName) {
  const getAsync = util.promisify(client.get).bind(client);
  const result = await getAsync(schoolName);
  console.log(result);
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

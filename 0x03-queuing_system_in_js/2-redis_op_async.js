import { createClient, print } from 'redis';
const util = require('util');

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, res) => {
    if (error) throw new Error(error.message);
    print(res);
  });
};

async function displaySchoolValue(schoolName) {
  const getAsync = util.promisify(client.get).bind(client);
  const result = await getAsync(schoolName);
  console.log(result);
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
